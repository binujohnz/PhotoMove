@echo off

:: Build me

pyinstaller --onefile --distpath ..\dist --workpath ..\build --specpath ..\build\ photoMain.py
