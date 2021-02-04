@echo Off
title Cari Java
:awal
cls
echo adakah file java
echo.---------------------------------------------------
echo dimana kamu pengen cari
set/p input=Masukan direktori:
echo ---------------------------------------------------
echo.
echo Direktori yang dipanggil %input%
echo.
echo ---------------------------------------------------
%input%:
echo ada file java di
dir *.java /s /b
pause
echo ----------------------------------------------
:lanjutan
echo file java ditemukan, ganti nama?
echo Masukan Y atau T
set/p "ganti=Masukan Option:"
if %ganti%==y goto bancakan
if %ganti%==t goto yaudah
cls
:bancakan
echo ganti nama
set/p input2=Masukan nama:
%input%:
ren *.java "%input2%".java
pause
goto awal
cls
:yaudah
echo baiklah kalau begitu
pause
goto awal