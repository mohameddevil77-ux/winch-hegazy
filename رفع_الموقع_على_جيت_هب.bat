@echo off
chcp 65001 > nul
title رفع موقع ونش حجازي على GitHub
cd /d "D:\winch-hegazy"

echo ======================================================
echo       رفع موقع ونش حجازي كاملاً بكافة الصور على GitHub
echo ======================================================
echo.
echo تم تهيئة المستودع وإضافة كافة الصور (23 صورة) والصفحات (26 صفحة).
echo.
set /p REPO_URL="أدخل رابط مستودع GitHub الخاص بك (مثال: https://github.com/username/winch-hegazy.git): "

if "%REPO_URL%"=="" (
    echo خطأ: لم يتم إدخال الرابط!
    pause
    exit /b
)

git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main
echo.
echo جاري رفع كافة الملفات والصور إلى GitHub...
git push -u origin main --force

echo.
echo ======================================================
echo تم الرفع بنجاح! جميع الصور والمجلدات مرفوعة الآن على GitHub.
echo.
echo لتشغيل الموقع أونلاين مجاناً عبر (GitHub Pages):
echo 1. ادخل على رابط المستودع في المتصفح.
echo 2. اضغط على Settings ثم Pages من القائمة الجانبية.
echo 3. في خانة Branch اختر main واضغط Save.
echo ======================================================
pause
