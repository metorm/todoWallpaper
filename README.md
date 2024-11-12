# todoWallpaper

## 简介 (Introduction)

Wallpaper Todos 是一个开源的Python脚本，它可以将您的待办事项（todo.txt格式）渲染到桌面壁纸之上，从而在您的工作环境中不断提醒您尚未完成的任务。

Wallpaper Todos is an open-source Python script that overlays your to-do items (in todo.txt format) onto your desktop wallpaper, providing a constant reminder of pending tasks in your working environment.

## 特性 (Features)

- 自动读取todo.txt文件中的待办事项。
- 将待办事项渲染到桌面壁纸之上。
- 定时更新壁纸，确保待办事项的时效性。
- 支持多种图片格式作为壁纸。
- 轻松定制字体样式和颜色。

## 安装 (Installation)

1. 确保您的系统已安装Python。
2. 克隆或下载此仓库到本地。
3. 安装必要的Python库（如果尚未安装）：

    ```bash
    pip install Pillow
    ```

4. 运行脚本：

    ```bash
    python wallpaper_todos.py
    ```

## 使用说明 (Usage)

1. 将您的待办事项按照todo.txt格式保存到todosrc文件中。
2. 确保脚本有权限读取todosrc文件和写入壁纸文件。
3. 运行脚本，待办事项将显示在您的桌面壁纸之上。

## 配置 (Configuration)

### 配置文件说明 (Configuration File Instructions)
#### 如何配置 `config.ini` 文件 (How to Configure the `config.ini` File)
以下是对 `config.ini` 文件各部分的详细说明，以帮助您正确配置脚本。
##### [src] 部分 (src Section)
- `todosrc`：设置待办事项文件 `todo.txt` 的路径。
- `update_interval`：设置脚本检查待办事项文件更新的时间间隔（以秒为单位）。
##### [render] 部分 (render Section)
- `size_basis`：设置渲染尺寸的基准，`screen` 表示基于屏幕尺寸进行缩放，其他设置则为绝对尺寸。
- `fontname`：设置字体文件的名称。
- `fontsize`：设置字体的大小。
- `spacing`：设置文本行间距。
- `alignX`：设置文本在水平方向的对齐方式，例如 `left`、`center` 或 `right`。
- `alignY`：设置文本在垂直方向的对齐方式，例如 `top`、`center` 或 `bottom`。
- `backgroud_color`：设置背景颜色，格式为 `RRGGBB`，十六进制颜色但不带`#`。
- `text_color`：设置文本颜色，格式为 `RRGGBB`，十六进制颜色但不带`#`。
- `radius`：设置背景块的圆角半径。
- `alpha`：设置背景块的透明度（0-255，0为完全透明，255为完全不透明）。
- `inner_padding`：设置文本与背景块边缘的内边距。
- `outer_padding`：设置背景块与壁纸边缘的外边距。
例如：
```ini
[src]
todosrc=C:\Users\xxx\todo.todotxt
update_interval = 10
[render]
size_basis=screen
fontname=SarasaMonoSlabSC.ttf
fontsize=18
spacing=8
alignX=left
alignY=top
backgroud_color=ff00ff
text_color=00ff00
radius=10
alpha=80
inner_padding=10
outer_padding=5
```
请根据您的需求调整上述配置。
### How to Configure the `config.ini` File
Below is a detailed explanation of each section of the `config.ini` file to help you configure the script correctly.
##### [src] Section
- `todosrc`: Sets the path to the `todo.txt` file containing the to-do items.
- `update_interval`: Sets the time interval (in seconds) for the script to check for updates to the to-do items file.
##### [render] Section
- `size_basis`: Sets the basis for the render size, `screen` means auto scale on based of the screen size, any other setting means to use absolute size.
- `fontname`: Sets the name of the font file.
- `fontsize`: Sets the size of the font.
- `spacing`: Sets the line spacing for the text.
- `alignX`: Sets the horizontal alignment of the text, e.g., `left`, `center`, or `right`.
- `alignY`: Sets the vertical alignment of the text, e.g., `top`, `center`, or `bottom`.
- `backgroud_color`: Sets the background hex color in the format `RRGGBB`.
- `text_color`: Sets the text hex color in the format `RRGGBB`.
- `radius`: Sets the radius of the rounded corners for the background block.
- `alpha`: Sets the transparency of the background block (0-255, where 0 is fully transparent and 255 is fully opaque).
- `inner_padding`: Sets the inner padding between the text and the edge of the background block.
- `outer_padding`: Sets the outer padding between the background block and the edge of the wallpaper.
For example:
```ini
[src]
todosrc=C:\Users\weiran\Nextcloud\黑曜石库\公务笔记\任务管理.todotxt
update_interval = 10
[render]
size_basis=screen
fontname=SarasaMonoSlabSC.ttf
fontsize=18
spacing=8
alignX=left
alignY=top
backgroud_color=ff00ff
text_color=00ff00
radius=10
alpha=80
inner_padding=10
outer_padding=5
```
Adjust the configurations above according to your needs.


## 许可证 (License)

本项目使用 Anti-CSDN CC 许可证 - 请查看以下链接了解更多信息。

[License: Anti-CSDN CC](https://www.weiran.ink/intro.html)


## 贡献 (Contributing)

欢迎贡献！请发起Pull Request或创建Issue来讨论新功能或改进。

We welcome contributions! Please open a Pull Request or create an Issue to discuss new features or improvements.

## 作者 (Authors)

- [长安码徒](https://www.weiran.ink) - 项目创建者。

## 致谢 (Acknowledgments)

感谢所有贡献者以及使用本项目的人！

Special thanks to all contributors and users of this project!
