@echo off
chcp 65001 > nul
title رفع موقع أوناش إنقاذ أولاد حجازي إلى GitHub
cd /d "D:\winch-hegazy"

echo ========================================================
echo       جاري رفع موقع أوناش أولاد حجازي بالكامل إلى GitHub
echo   المستودع: https://github.com/mohameddevil77-ux/winch-hegazy
echo   الحساب المطلوب: mohameddevil77-ux
echo ========================================================
echo.
echo [1/3] فحص وإعداد المستودع والفرع الرئيسي...
git remote remove origin 2>nul
git remote add origin https://mohameddevil77-ux@github.com/mohameddevil77-ux/winch-hegazy.git
git branch -M main

echo.
echo [2/3] جاري رفع كافة الملفات والصور والفيديوهات والمقالات...
echo ملاحظة هامة: ستفتح لك نافذة متصفح أو نافذة تسجيل الدخول إلى GitHub:
echo           اضغط على "Sign in with your browser"
echo           لتأكيد الدخول بحساب: mohameddevil77-ux
echo.
git push -u origin main --force

if %errorlevel% neq 0 (
    echo.
    echo ========================================================
    echo تنبيه: إذا لم يكتمل الرفع بسبب المصادقة، يمكنك إدخال:
    echo Personal Access Token (PAT) من حسابك في جيت هب.
    echo أو تأكد من تسجيل دخولك بحساب mohameddevil77-ux في المتصفح.
    echo ========================================================
    pause
    exit /b
)

echo.
echo ========================================================
echo [3/3] تم الرفع بنجاح 100%!
echo كافة الصور الحقيقية والفيديوهات والـ 26 مقالاً مرفوعة الآن على مستودعك.
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
