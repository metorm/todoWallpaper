# 获取当前用户
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name

# 询问用户获取pythonw.exe的位置
Write-Host "你需要一个带有Pillow的Python环境。"
Write-Host "You need a python environment with Pillow installed."

Write-Host "请输入pythonw.exe的完整路径(例如：C:\ProgramData\miniconda3\pythonw.exe)"
$pythonwPath = Read-Host "Please enter the full path to pythonw.exe (e.g., C:\ProgramData\miniconda3\pythonw.exe)"

# 获取脚本所在的路径作为工作目录
$scriptPath = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

# 定义计划任务名称
$taskName = "todoWallpaper"

# 检测是否存在同名计划任务
$taskExists = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue

if ($taskExists) {
    # 如果存在，首先尝试停止计划任务
    try {
        Stop-ScheduledTask -TaskName $taskName
        Write-Host "计划任务已停止。"
        Write-Host "The scheduled task has been stopped."
    }
    catch {
        Write-Host "停止计划任务时发生错误：$_"
        Write-Host "An error occurred while stopping the scheduled task: $_"
    }

    # 尝试删除计划任务
    try {
        Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
        Write-Host "已存在的计划任务已删除。"
        Write-Host "The existing scheduled task has been deleted."
    }
    catch {
        Write-Host "删除计划任务时发生错误：$_"
        Write-Host "An error occurred while deleting the scheduled task: $_"
    }
}

# 创建一个新的计划任务触发器，设置为用户登录时触发
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $currentUser
$trigger.Delay = 'PT60S'

# 创建一个新的计划任务动作，执行pythonw.exe
$action = New-ScheduledTaskAction -Execute $pythonwPath -Argument "todoWallpaper.py" -WorkingDirectory $scriptPath

# 创建一个新的计划任务设置
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit 0 -Priority 7
$settings.RestartInterval = 'PT1M'
$settings.RestartCount = 30

# 创建一个新的计划任务主体
$principal = New-ScheduledTaskPrincipal -UserId $currentUser -LogonType Interactive -RunLevel Limited

# 注册计划任务
$taskDescription = "todoWallpaper worker"
try {
    $registerTask = Register-ScheduledTask -TaskName $taskName -Trigger $trigger -Action $action -Settings $settings -Principal $principal -Description $taskDescription
    # 检测是否添加成功
    $taskAdded = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
    if ($taskAdded) {
        # 添加成功后，立即开始执行这个计划任务
        Start-ScheduledTask -TaskName $taskName
        Write-Host "计划任务已创建并开始执行。"
        Write-Host "The scheduled task has been created and started."

        Write-Host "计划任务已创建。如果想要卸载软件，请手动进入计算机管理界面，删除 $taskName 这条计划任务。"
        Write-Host "The scheduled task has been created. If you want to uninstall the software, please manually enter the Computer Management interface and delete this scheduled task: $taskName"
    }
    else {
        # 返回错误信息
        Write-Host "计划任务创建失败。"
        Write-Host "Failed to create the scheduled task."
    }
}
catch {
    # 返回错误信息
    Write-Host "计划任务注册失败：$_"
    Write-Host "Failed to register the scheduled task: $_"
}

Write-Host "等待15秒后，脚本将自动退出。"
Write-Host "The script will exit automatically in 15 seconds."
Start-Sleep 15