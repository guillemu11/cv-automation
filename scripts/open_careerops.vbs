' Open the Career Ops dashboard in the default browser.
' Reads the live port from data/webapp_port.txt (written by the background
' server at startup). If the file is missing, falls back to 8062.
Set sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
projectDir = "C:\Users\gmunoz02\Desktop\CV_Automation"
portFile = projectDir & "\data\webapp_port.txt"
port = "8062"
If fso.FileExists(portFile) Then
    Set f = fso.OpenTextFile(portFile, 1)
    port = Trim(f.ReadAll)
    f.Close
End If
sh.Run "http://localhost:" & port, 1, False
