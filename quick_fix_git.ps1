# Quick Fix Script for Git Push Issue
# This removes venv from git tracking

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Git Repository Fix Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in a git repository
if (-not (Test-Path .git)) {
    Write-Host "ERROR: Not a git repository!" -ForegroundColor Red
    Write-Host "Please run this script from your project root." -ForegroundColor Yellow
    exit 1
}

Write-Host "Step 1: Removing venv from git tracking..." -ForegroundColor Yellow
git rm -r --cached venv/ 2>$null

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ venv removed from git tracking" -ForegroundColor Green
} else {
    Write-Host "⚠ venv might not be tracked (this is OK)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 2: Adding .gitignore..." -ForegroundColor Yellow
git add .gitignore

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ .gitignore added" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to add .gitignore" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Step 3: Committing changes..." -ForegroundColor Yellow
git commit -m "Remove venv from repository and update .gitignore"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Changes committed" -ForegroundColor Green
} else {
    Write-Host "⚠ Nothing to commit (this might be OK)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 4: Checking git status..." -ForegroundColor Yellow
git status

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "If the above looks good, run:" -ForegroundColor Green
Write-Host "  git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "If you still get errors, you need to clean git history." -ForegroundColor Yellow
Write-Host "See FIX_GIT_ISSUE.md for detailed instructions." -ForegroundColor Yellow
Write-Host ""
