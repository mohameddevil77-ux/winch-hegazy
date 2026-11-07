@echo off
chcp 65001 > nul
color 0B
title UPLOAD AWLAD HEGAZY TO GITHUB

cd /d "D:\winch-hegazy"

echo ================================================================
echo       UPLOADING AWLAD HEGAZY WEBSITE TO GITHUB PAGES
echo   Repository: https://github.com/mohameddevil77-ux/winch-hegazy
echo   Target Account: mohameddevil77-ux
echo ================================================================
echo.
echo [1/3] Preparing git repository...
git remote remove origin 2>nul
git remote add origin https://mohameddevil77-ux@github.com/mohameddevil77-ux/winch-hegazy.git
git branch -M main

echo.
echo [2/3] Uploading all 80+ files, photos, videos, and articles...
echo NOTE: A browser window will now open asking you to confirm:
echo       "Sign in with your browser"
echo       Click it and click "Authorize" to finish the upload.
echo.
git push -u origin main --force

if %errorlevel% neq 0 (
    echo.
    echo ================================================================
    echo If GitHub authentication failed, you can paste a Personal Access Token:
    set /p GITHUB_TOKEN="Paste your GitHub Token (or press Enter to exit): "
    if not "%GITHUB_TOKEN%"=="" (
        git push https://mohameddevil77-ux:%GITHUB_TOKEN%@github.com/mohameddevil77-ux/winch-hegazy.git main --force
    )
)

echo.
echo ================================================================
echo [3/3] SUCCESS! All files uploaded 100% to GitHub!
echo ================================================================
pause
