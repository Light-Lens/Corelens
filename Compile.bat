@ECHO OFF

title Compile Corelet
echo Compiling Corelet

pyinstaller.exe --icon=Logo.ico --onefile Hexa.py
cls

echo Done.
move dist\Corelet.exe Corelet.exe

del dist
del build
del __pycache__
del Corelet.spec

echo|set /p="Continue."
pause >nul
exit
