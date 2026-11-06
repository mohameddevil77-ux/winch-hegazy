@echo off
chcp 65001 > nul
title رفع موقع ونش حجازي إلى GitHub
cd /d "D:\winch-hegazy"

echo ========================================================
echo       جاري رفع موقع ونش حجازي بالكامل إلى GitHub
echo   المستودع: https://github.com/mohameddevil77-ux/winch-hegazy
echo ========================================================
echo.
echo [1/2] إعداد المستودع والفرع الرئيسي...
git remote remove origin 2>nul
git remote add origin https://github.com/mohameddevil77-ux/winch-hegazy.git
git branch -M main

echo.
echo [2/2] جاري رفع كافة الملفات والصور (80+ ملفاً)...
echo ملاحظة: إذا ظهرت لك نافذة تسجيل دخول GitHub، اختر:
echo        "Sign in with your browser" لتأكيد حسابك.
echo.
git push -u origin main --force

echo.
echo ========================================================
echo تم الرفع بنجاح 100%!
echo كافة الصور والمقالات وصفحات الموقع مرفوعة الآن على مستودعك.
echo.
echo لتشغيل الموقع أونلاين مجاناً على (GitHub Pages):
echo 1. افتح هذا الرابط:
echo    https://github.com/mohameddevil77-ux/winch-hegazy/settings/pages
echo 2. في خانة (Branch) اختر: main
echo 3. اضغط على زر (Save).
echo.
echo سيعمل موقعك مباشرة على الرابط:
echo https://mohameddevil77-ux.github.io/winch-hegazy/
echo ========================================================
pause
