' ====================================================================
' Career Ops — One-click dashboard launcher (Chrome-app style)
' ====================================================================
' Double-click this (or the desktop shortcut that points to it) and it:
'   1. Finds the project + Python interpreter (no hard-coded user paths)
'   2. Starts the dashboard server in the background if it isn't running
'   3. Waits until the server actually answers
'   4. Opens the dashboard in a clean Chrome "app" window (no tabs / no
'      address bar) so it looks and feels like a native desktop app
'
' Everything is self-locating: this script lives in <project>\scripts\,
' so the project root is just its parent folder. Move the whole folder
' anywhere and it still works.
' ====================================================================
Option Explicit

Dim fso, sh, scriptDir, projectDir, pythonw, chrome, port, portFile, url, i
Set fso = CreateObject("Scripting.FileSystemObject")
Set sh  = CreateObject("WScript.Shell")

' --- Locate project root (parent of the \scripts folder) ---
scriptDir  = fso.GetParentFolderName(WScript.ScriptFullName)
projectDir = fso.GetParentFolderName(scriptDir)

' --- Pick the Python interpreter (prefer the project venv) ---
pythonw = projectDir & "\.venv\Scripts\pythonw.exe"
If Not fso.FileExists(pythonw) Then
    pythonw = sh.ExpandEnvironmentStrings("%LOCALAPPDATA%\Programs\Python\Python312\pythonw.exe")
End If

portFile = projectDir & "\data\webapp_port.txt"

' --- Is the server already running? ---
port = ReadPort(portFile, "8062")
If Not ServerUp(port) Then
    ' Launch the background server (no console window: pythonw + window style 0)
    sh.CurrentDirectory = projectDir
    sh.Run """" & pythonw & """ """ & projectDir & "\scripts\run_webapp_background.py""", 0, False

    ' Wait up to ~30s for it to bind a port and answer
    For i = 1 To 60
        WScript.Sleep 500
        port = ReadPort(portFile, "8062")
        If ServerUp(port) Then Exit For
    Next
End If

url = "http://localhost:" & port

' --- Open in a Chrome app window, or fall back to the default browser ---
chrome = FindChrome(fso, sh)
If chrome = "" Then
    sh.Run url, 1, False
Else
    Dim profileDir
    profileDir = projectDir & "\data\chrome_app_profile"
    sh.Run """" & chrome & """ --app=" & url & _
           " --user-data-dir=""" & profileDir & """" & _
           " --no-first-run --no-default-browser-check", 1, False
End If

WScript.Quit 0

' ====================================================================
' Helpers
' ====================================================================
Function ReadPort(pf, fallback)
    ReadPort = fallback
    If fso.FileExists(pf) Then
        Dim f, txt
        Set f = fso.OpenTextFile(pf, 1)
        If Not f.AtEndOfStream Then
            txt = Trim(f.ReadAll)
            If Len(txt) > 0 Then ReadPort = txt
        End If
        f.Close
    End If
End Function

Function ServerUp(p)
    On Error Resume Next
    Dim http
    Set http = CreateObject("MSXML2.ServerXMLHTTP.6.0")
    http.setTimeouts 1500, 1500, 1500, 1500
    http.open "GET", "http://localhost:" & p & "/", False
    http.send
    ' Any HTTP status (even 404) means something is listening = server up.
    ServerUp = (Err.Number = 0 And http.Status > 0)
    On Error GoTo 0
End Function

Function FindChrome(fsoRef, shRef)
    Dim candidates, c
    candidates = Array( _
        shRef.ExpandEnvironmentStrings("%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"), _
        shRef.ExpandEnvironmentStrings("%PROGRAMFILES%\Google\Chrome\Application\chrome.exe"), _
        shRef.ExpandEnvironmentStrings("%PROGRAMFILES(X86)%\Google\Chrome\Application\chrome.exe"), _
        shRef.ExpandEnvironmentStrings("%PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe"), _
        shRef.ExpandEnvironmentStrings("%PROGRAMFILES(X86)%\Microsoft\Edge\Application\msedge.exe") )
    FindChrome = ""
    For Each c In candidates
        If fsoRef.FileExists(c) Then
            FindChrome = c
            Exit For
        End If
    Next
End Function
