@echo off
cls
echo [ydl-gui] Installing "ffmpeg" via "Chocolatey"
echo.
choco feature enable -n allowGlobalConfirmation
choco install ffmpeg-full
cls

startMain