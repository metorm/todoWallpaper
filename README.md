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

### 安装为服务 (Install as Service)

#### 安装 `todoWallpaper` 作为 Windows 服务
以下步骤将指导您如何使用 Windows Service Wrapper (winsw) 将 `todoWallpaper` 脚本安装为 Windows 服务。

##### 步骤 1: 准备工作
1. 确保您已经安装了 Python 并配置了环境变量。
2. 克隆或下载此仓库到您的本地计算机。
3. 如果您对仓库中提供的 `todoWallpaper.exe` 有安全顾虑，您可以前往 [winsw 项目页面](https://github.com/winsw/winsw) 下载官方的 `winsw.exe` 可执行文件，并将其重命名为 `todoWallpaper.exe` 来替代仓库中提供的版本。

##### 步骤 2: 配置服务
1. 打开命令提示符或 PowerShell。
2. 导航到仓库目录中的 `todoWallpaper.xml` 文件所在位置。
3. 使用以下命令安装服务（请根据实际情况替换路径）：
```shell
C:\path\to\todoWallpaper.exe install
```
例如，如果 `todoWallpaper.exe` 和 `todoWallpaper.xml` 都位于 `C:\dev\todoWallpaper` 目录下，则运行：
```shell
C:\dev\todoWallpaper\todoWallpaper.exe install
```
这将根据 `todoWallpaper.xml` 文件中的配置将 `todoWallpaper` 安装为 Windows 服务。

##### 步骤 3: 启动服务
1. 打开 Windows 服务管理器。您可以通过在开始菜单搜索 "Services" 来找到它。
2. 找到 `todoWallpaperSrv` 服务。
3. 右键点击服务并选择 "启动" 来启动服务。

##### 步骤 4: 验证服务
1. 检查服务是否正在运行，您可以通过服务管理器查看状态，或者检查日志文件来确认。
2. 如果服务未按预期运行，检查日志文件以获取错误信息。日志文件的位置取决于您的 `todoWallpaper.xml` 配置。

##### 步骤 5: 更新或卸载服务
- 若要更新服务，请先使用上述命令卸载服务，然后重新安装。
- 若要卸载服务，请运行以下命令：
```shell
C:\path\to\todoWallpaper.exe uninstall
```
例如：
```shell
C:\dev\todoWallpaper\todoWallpaper.exe uninstall
```
这将停止并从 Windows 服务列表中移除 `todoWallpaperSrv`。

##### 注意事项
- 确保在 `todoWallpaper.xml` 文件中指定的 `executable`、`arguments` 和 `workingdirectory` 路径与您的系统环境相匹配。
- 如果您更改了 `todoWallpaper.py` 脚本或相关配置文件，可能需要重新启动服务以应用更改。
通过以上步骤，您应该能够成功地将 `todoWallpaper` 安装并运行为一个 Windows 服务。如果遇到任何问题，请参考日志文件以获取更多信息。

#### Installing `todoWallpaper` as a Windows Service
Follow the steps below to install `todoWallpaper` as a Windows service using the Windows Service Wrapper (winsw).

##### Step 1: Preparation
1. Ensure that Python is installed on your system and that the environment variables are configured.
2. Clone or download the repository to your local machine.
3. If you have security concerns about the provided `todoWallpaper.exe` in the repository, you can download the official `winsw.exe` executable from the [winsw project page](https://github.com/winsw/winsw), rename it to `todoWallpaper.exe`, and use it instead of the version provided in the repository.

##### Step 2: Configure the Service
1. Open Command Prompt or PowerShell.
2. Navigate to the directory where the `todoWallpaper.xml` file is located within the repository.
3. Use the following command to install the service (replace the path with the actual path to your executable):
```shell
C:\path\to\todoWallpaper.exe install
```
For example, if `todoWallpaper.exe` and `todoWallpaper.xml` are located in `C:\dev\todoWallpaper`, run:
```shell
C:\dev\todoWallpaper\todoWallpaper.exe install
```
This will install `todoWallpaper` as a Windows service based on the configuration in the `todoWallpaper.xml` file.

##### Step 3: Start the Service
1. Open the Windows Services Manager. You can find it by searching for "Services" in the Start menu.
2. Locate the `todoWallpaperSrv` service.
3. Right-click on the service and select "Start" to start the service.

##### Step 4: Verify the Service
1. Check if the service is running by looking at its status in the Services Manager or by checking the log file.
2. If the service is not running as expected, check the log file for error messages. The location of the log file depends on your `todoWallpaper.xml` configuration.

##### Step 5: Update or Uninstall the Service
- To update the service, uninstall it first using the command above, then reinstall it.
- To uninstall the service, run the following command:
```shell
C:\path\to\todoWallpaper.exe uninstall
```
For example:
```shell
C:\dev\todoWallpaper\todoWallpaper.exe uninstall
```
This will stop and remove `todoWallpaperSrv` from the Windows services list.
##### Notes
- Ensure that the paths specified for `executable`, `arguments`, and `workingdirectory` in the `todoWallpaper.xml` file match your system environment.
- If you make changes to the `todoWallpaper.py` script or related configuration files, you may need to restart the service for the changes to take effect.
By following the steps above, you should be able to successfully install and run `todoWallpaper` as a Windows service. If you encounter any issues, refer to the log file for more detailed information.

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
