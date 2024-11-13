import os
import time
import random
import logging
from configparser import ConfigParser
from PIL import Image, ImageDraw, ImageFont
import ctypes
from ctypes import wintypes

SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02


def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        image_path,
        # ctypes.c_char_p(ctypes.addressof(wallpaper_info)),
        SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE,
    )


def rounded_rectangle(draw, xy, radius, fill=None, outline=None):
    # 绘制圆角矩形
    x0, y0, x1, y1 = xy
    draw.rectangle([(x0, y0 + radius), (x1, y1 - radius)], fill=fill, outline=outline)
    draw.rectangle([(x0 + radius, y0), (x1 - radius, y1)], fill=fill, outline=outline)
    draw.pieslice(
        [(x0, y0), (x0 + 2 * radius, y0 + 2 * radius)],
        180,
        270,
        fill=fill,
        outline=outline,
    )
    draw.pieslice(
        [(x1 - 2 * radius, y0), (x1, y0 + 2 * radius)],
        270,
        360,
        fill=fill,
        outline=outline,
    )
    draw.pieslice(
        [(x0, y1 - 2 * radius), (x0 + 2 * radius, y1)],
        90,
        180,
        fill=fill,
        outline=outline,
    )
    draw.pieslice(
        [(x1 - 2 * radius, y1 - 2 * radius), (x1, y1)],
        0,
        90,
        fill=fill,
        outline=outline,
    )


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=os.path.abspath("runLog.log"),  # 指定日志文件路径
)


# 读取配置文件
config = ConfigParser()
config.read("todo-config.ini", encoding="utf-8-sig")
logging.info("Config loaded successfully")

# 获取配置信息
todosrc = config.get("src", "todosrc")
update_interval = config.getint("src", "update_interval")

size_basis = config.get("render", "size_basis")
fontname = config.get("render", "fontname")
fontsize_o = config.getint("render", "fontsize")
line_spacing_o = config.getint("render", "spacing")
alignX = config.get("render", "alignX")
alignY = config.get("render", "alignY")
background_color = config.get("render", "backgroud_color")
text_color = config.get("render", "text_color")
radius_o = config.getint("render", "radius")
alpha = config.getint("render", "alpha")
inner_padding_o = config.getint("render", "inner_padding")
outer_padding_o = config.getint("render", "outer_padding")

logging.info("Config loaded successfully")

# 将十六进制背景色转换为RGB
background_rgb = tuple(int(background_color[i : i + 2], 16) for i in (0, 2, 4))
text_rgb = tuple(int(text_color[i : i + 2], 16) for i in (0, 2, 4))

# 无限循环直到关机
last_todo_text = ""
while True:
    logging.info("Starting yet another loop")

    # 读取todo文件内容
    with open(todosrc, "r", encoding="utf-8") as file:
        todo_text = file.read()
        if last_todo_text != todo_text:
            logging.info("todo text changed, drawing new wallpaper ...")
            last_todo_text = todo_text
        else:
            logging.info("todo text not changed, skipping current iteration ...")
            logging.info("Waiting for %d seconds...", update_interval)
            time.sleep(update_interval)
            continue

    # 随机选择一张图片
    wallpaper_dir = "wallpaper"
    wallpapers = [
        f
        for f in os.listdir(wallpaper_dir)
        if os.path.isfile(os.path.join(wallpaper_dir, f))
    ]
    wallpaper_path = os.path.join(wallpaper_dir, random.choice(wallpapers))
    logging.info("Random wallpaper selected: %s", wallpaper_path)

    # 读取图片
    image = Image.open(wallpaper_path)

    if size_basis == "screen":
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        # ratio = (image.width / screen_width + image.height / screen_height) / 2
        image = image.resize((screen_width, screen_height))
        logging.info("Image resized to screen size: %dx%d", image.width, image.height)

    ratio = 1

    fontsize = fontsize_o * ratio
    line_spacing = line_spacing_o * ratio
    radius = radius_o * ratio
    inner_padding = inner_padding_o * ratio
    outer_padding = outer_padding_o * ratio

    # 创建一个绘图对象
    draw = ImageDraw.Draw(image)

    # 设置字体
    font = ImageFont.truetype(fontname, fontsize)

    # 计算文本尺寸
    text_bbox = draw.textbbox((0, 0), todo_text, font=font, spacing=line_spacing)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    logging.info("Text box size: %dx%d", text_width, text_height)

    # 根据对齐方式计算文本位置
    if alignX == "right":
        text_x = image.width - text_width
    else:  # 默认为left
        text_x = 0

    if alignY == "bottom":
        text_y = image.height - text_height
    else:  # 默认为top
        text_y = 0

    # 创建一个透明图层用于绘制底色块和文字
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))  # 完全透明的图层
    draw_overlay = ImageDraw.Draw(overlay)

    # 设置底色块的颜色和透明度
    background_color = (
        background_rgb[0],
        background_rgb[1],
        background_rgb[2],
        int(alpha * 2.55),
    )

    # 计算底色块的位置和大小
    text_bbox = draw_overlay.textbbox(
        (0, 0), todo_text, font=font, spacing=line_spacing
    )
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 计算底色块的总宽度和高度
    block_width = text_width + 2 * inner_padding
    block_height = text_height + 2 * inner_padding

    # 根据配置计算底色块的位置
    if alignX == "center":
        block_x = (image.width - block_width) / 2
    elif alignX == "right":
        block_x = image.width - block_width - outer_padding
    else:  # 默认为left
        block_x = outer_padding

    if alignY == "center":
        block_y = (image.height - block_height) / 2
    elif alignY == "bottom":
        block_y = image.height - block_height - outer_padding
    else:  # 默认为top
        block_y = outer_padding

    # 绘制带圆角的底色块
    draw_overlay.rounded_rectangle(
        [(block_x, block_y), (block_x + block_width, block_y + block_height)],
        radius=min(radius, block_width / 2, block_height / 2),
        fill=background_color,
        outline=None,
    )

    # 绘制文字到透明图层
    draw_overlay.text(
        (
            block_x + inner_padding,
            block_y + inner_padding,
        ),
        todo_text,
        font=font,
        fill=text_rgb,
        spacing=line_spacing,
    )

    # 保存图片前，确保图片是RGBA模式，如果不是，需要转换
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # 将文字图层和图片合并
    image = Image.alpha_composite(image, overlay)

    # 保存图片
    # 使用正确的文件扩展名
    file_extension = wallpaper_path.split(".")[-1]
    # the_wallpaper_path = f"theWallpaper.{file_extension}"
    the_wallpaper_path = f"theWallpaper.png"
    image.save(the_wallpaper_path)
    logging.info("Wallpaper saved to %s", the_wallpaper_path)

    # 设置壁纸
    set_wallpaper(os.path.abspath(the_wallpaper_path))

    # 等待1分钟
    logging.info("Waiting for %d seconds...", update_interval)
    time.sleep(update_interval)
