# todoWallpaper

## 简介 (Introduction)

todoWallpaper 是一个开源的Python脚本，它可以将您的待办事项（todo.txt格式）渲染到桌面壁纸之上，从而在您的工作环境中不断提醒您尚未完成的任务。

todoWallpaper is an open-source Python script that overlays your to-do items (in todo.txt format) onto your desktop wallpaper, providing a constant reminder of pending tasks in your working environment.

实际上，本项目并不依赖于 todo.txt 的独特格式，您可以将数据源指向任何文本文件。但我想其他类型的文件并没有实时渲染到您的壁纸上的必要。

Actually, this project does not rely on the unique format of todo.txt, you can point the data source to any text file. But I guess other types of files are not necessary to be rendered on your wallpaper in real time.

## 特性 (Features)

- 自动读取todo.txt文件中的待办事项。
- 将待办事项渲染到桌面壁纸之上。
- 定时更新壁纸，确保待办事项的时效性。
- 支持多种图片格式作为壁纸。
- 轻松定制字体样式和颜色。

## 使用说明 (Usage)

1. 将您的待办事项按照todo.txt格式保存到todosrc文件中，将您喜欢的一些壁纸（也可以只有一张）放入wallpaper文件夹。
2. 确保脚本有权限读取todosrc文件和写入壁纸文件。
3. 简单运行脚本，或安装为服务，待办事项将显示在您的桌面壁纸之上。

1. Save your todos in todosrc file in todo.txt format, and put some wallpapers you like (or just one) into wallpaper folder.
2. Make sure the script has permission to read todosrc file and write wallpaper files.
3. Simply run the script, or install it as a service, and the todos will appear on top of your desktop wallpaper.

## 安装 (Installation)

### 快速开始 (Quick Start)

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

1. Make sure your system has Python installed.
2. Clone or download this repository locally.
3. Install the necessary Python libraries (if not already installed):

    ```bash
    pip install Pillow
    ```

4. Run the script：

    ```bash
    python wallpaper_todos.py
    ```

### 安装为后台计划任务 (Install as a background task)

#### 安装 `todoWallpaper` 作为 Windows 计划任务项目
以下步骤将指导您如何使用计划任务，将脚本放置于后台，开机自动启动，后台运行。

##### 步骤 1: 准备工作
1. 确保您已经安装了 Python 并配置了环境变量。
2. 克隆或下载此仓库到您的本地计算机。

##### 步骤 2: 配置服务
1. 导航到仓库目录中的 `todoWallpaper.xml` 文件所在位置。
2. 在`Install.ps1`文件上点击右键，并选择 "使用Powershell运行"。
3. 按提示输出用来运行todoWallpaper.py脚本的python解释器路径。一般应使用`pythonw.exe`，以避免运行窗口。
4. 后续工作将自动进行；如果需要更改配置选择，可以选择修改`Install.ps1`文件，或直接修改已经创建的计划任务。
5. 如果重复运行上述命令，将自动删除并重新创建计划任务。
6. 检查服务是否正在运行，这可以通过检查日志文件`runLog.log`来确认。
7. 如果需要卸载程序，需要手动删除已创建的计划任务，并删除文件夹。

#### Install `todoWallpaper` as a Windows Scheduled Task Project
The following steps will guide you on how to use the scheduled task to place the script in the background, automatically start it at boot, and run it in the background.

##### Step 1: Preparation
1. Make sure you have Python installed and configured the environment variables.
2. Clone or download this repository to your local computer.

##### Step 2: Configure the service
1. Navigate to the location of the `todoWallpaper.xml` file in the repository directory.
2. Right-click on the `Install.ps1` file and select "Run with Powershell".
3. Follow the prompts to output the path to the python interpreter used to run the todoWallpaper.py script. Generally, `pythonw.exe` should be used to avoid running the window.
4. Subsequent work will be carried out automatically; if you need to change the configuration selection, you can choose to modify the `Install.ps1` file, or directly modify the already created scheduled task.
5. If you run the above command repeatedly, the scheduled task will be automatically deleted and recreated.
6. Check if the service is running. This can be confirmed by checking the log file `runLog.log`.
7. If you need to uninstall the program, you need to manually delete the created scheduled task and delete the folder.

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

TODOs:

[ ] 更多的测试和错误修复
[ ] 改进说明文档
[ ] 适当地支持多显示器（同时考虑热插拔显示器）
[ ] 支持多种填充方式，而不是简单的resize
[ ] 图形配置界面
[ ] Linux / MacOS 支持

[ ] More testing and bug fixes
[ ] Improved documentation
[ ] Proper support for multiple monitors (also takes hotplugging into account)
[ ] Support for multiple fill modes instead of simple resize
[ ] Graphical configuration interface
[ ] Linux / MacOS support

## 版本历史 (Version History)

2024-11-12 初始发布

## 作者 (Authors)

- [长安码徒](https://www.weiran.ink) - 项目创建者。

## 致谢 (Acknowledgments)

感谢所有贡献者以及使用本项目的人！

Special thanks to all contributors and users of this project!

本项目附带了以下开源软件：

[Sarasa Gothic / 更纱黑体 / 更紗黑體 / 更紗ゴシック / 사라사 고딕](https://github.com/be5invis/Sarasa-Gothic)


[winsw - Windows Service Wrapper in a permissive license](https://github.com/winsw/winsw)

项目开发重度使用了[智谱清言](https://chatglm.cn)。

The project development made heavy use of [Zhipu Qingyan](https://chatglm.cn).
