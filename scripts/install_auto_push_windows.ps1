# Registers the Windows equivalent of the macOS launchd auto-push: a Task
# Scheduler task that runs scripts/auto_push.sh every day at 23:00. If the PC is
# off or asleep at 23:00, it runs as soon as it is available again. Runs hidden
# (conhost --headless) in the user's session so Git Credential Manager works.
# Idempotent: re-running replaces the existing task. Dev-only one-shot.

$TaskName = 'CV_Automation AutoPush'
$Repo = Split-Path -Parent $PSScriptRoot
$Script = Join-Path $Repo 'scripts\auto_push.sh'

$GitExe = (Get-Command git -ErrorAction Stop).Source
$GitRoot = Split-Path -Parent (Split-Path -Parent $GitExe)
$Bash = Join-Path $GitRoot 'bin\bash.exe'
if (-not (Test-Path $Bash)) { throw "Git Bash not found at $Bash" }

$Action = New-ScheduledTaskAction -Execute 'conhost.exe' `
    -Argument "--headless `"$Bash`" `"$($Script -replace '\\', '/')`"" `
    -WorkingDirectory $Repo
$Trigger = New-ScheduledTaskTrigger -Daily -At '23:00'
$Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries -WakeToRun -ExecutionTimeLimit (New-TimeSpan -Minutes 30) `
    -MultipleInstances IgnoreNew
$Principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings `
    -Principal $Principal -Description 'Nightly git commit + push of CV_Automation to GitHub if anything changed (log: logs/auto_push.log)' `
    -Force | Out-Null

Get-ScheduledTask -TaskName $TaskName | Get-ScheduledTaskInfo | Select-Object TaskName, NextRunTime
