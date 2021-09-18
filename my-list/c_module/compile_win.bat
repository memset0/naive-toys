@echo off

cd %~dp0
g++ arraymodule.cpp -fPIC -shared -o arraymodule.dll
pause