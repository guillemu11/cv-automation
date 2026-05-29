' Silent launcher for the Career Ops dashboard.
' Invoked by Windows at login via a shortcut in shell:startup.
' Uses pythonw.exe (no console window) and 0 = SW_HIDE.
'
' To disable auto-start: delete the shortcut from
'   %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
Set sh = CreateObject("WScript.Shell")
projectDir = "C:\Users\gmunoz02\Desktop\CV_Automation"
pythonw = "C:\Users\gmunoz02\AppData\Local\Programs\Python\Python312\pythonw.exe"
script = projectDir & "\scripts\run_webapp_background.py"
sh.CurrentDirectory = projectDir
sh.Run """" & pythonw & """ """ & script & """", 0, False
