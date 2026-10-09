@echo off

set "WORKSPACE=%C:\Development\"

start "" chrome "https://mail.google.com" "https://calendar.google.com" "https://outlook.cloud.microsoft/mail/"
start "" spotify:
start "" code
start "" explorer.exe "%WORKSPACE%"
REM start powershell.exe
exit