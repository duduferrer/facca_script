@echo off
call %~dp0.venv\Scripts\activate.bat
python extrato_nubank_facca.py %1
pause
