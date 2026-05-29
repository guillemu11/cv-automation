@echo off
REM ====================================================================
REM Career Ops — start Chrome with remote debugging enabled
REM ====================================================================
REM What this does:
REM   - Closes any running Chrome (otherwise the new flag is ignored)
REM   - Relaunches Chrome with --remote-debugging-port=9222 pointing at
REM     YOUR real profile, so all your cookies / sessions / extensions
REM     are available to Career Ops's autofill bot
REM
REM Run this once at the start of a session (double-click the icon).
REM Career Ops will detect Chrome on port 9222 and attach to it.
REM ====================================================================

setlocal

REM --- Find chrome.exe ---
set "CHROME="
if exist "%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" set "CHROME=%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
if not defined CHROME if exist "%PROGRAMFILES%\Google\Chrome\Application\chrome.exe" set "CHROME=%PROGRAMFILES%\Google\Chrome\Application\chrome.exe"
if not defined CHROME if exist "%PROGRAMFILES(X86)%\Google\Chrome\Application\chrome.exe" set "CHROME=%PROGRAMFILES(X86)%\Google\Chrome\Application\chrome.exe"

if not defined CHROME (
    echo.
    echo [ERROR] Could not locate chrome.exe.
    echo   Looked in:
    echo     %LOCALAPPDATA%\Google\Chrome\Application\
    echo     %PROGRAMFILES%\Google\Chrome\Application\
    echo     %PROGRAMFILES(X86)%\Google\Chrome\Application\
    echo.
    pause
    exit /b 1
)

echo.
echo Career Ops — Chrome launcher
echo ============================
echo Chrome:  %CHROME%
echo Profile: %LOCALAPPDATA%\Google\Chrome\User Data
echo Port:    9222
echo.

REM --- Kill any existing Chrome so the debug flag actually applies ---
echo Closing existing Chrome windows (if any)...
taskkill /F /IM chrome.exe >nul 2>&1
REM Small wait so Chrome's user-data lock releases
timeout /t 2 /nobreak >nul

REM --- Launch with debugging enabled, using YOUR real profile ---
echo Launching Chrome with --remote-debugging-port=9222...
start "" "%CHROME%" --remote-debugging-port=9222 --user-data-dir="%LOCALAPPDATA%\Google\Chrome\User Data"

REM --- Verify it started ---
timeout /t 3 /nobreak >nul
echo.
echo Chrome should now be open with all your existing tabs and sessions.
echo Career Ops's autofill will use THIS Chrome (no separate window).
echo.
echo You can close this prompt — Chrome will keep running.
echo.
endlocal
