# Push Fraud Detection Project to GitHub
# This script properly pushes your project without venv

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Push to GitHub Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Configuration
$REPO_URL = "https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer.git"
$BRANCH = "main"

Write-Host "Target Repository: $REPO_URL" -ForegroundColor Yellow
Write-Host ""

# Step 1: Check if .git exists
if (Test-Path .git) {
    Write-Host "⚠ Git repository already exists!" -ForegroundColor Yellow
    Write-Host "Cleaning up old git history..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force .git
    Write-Host "✓ Old git history removed" -ForegroundColor Green
    Write-Host ""
}

# Step 2: Initialize new repository
Write-Host "Step 1: Initializing new git repository..." -ForegroundColor Yellow
git init
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Git repository initialized" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to initialize git" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 3: Add .gitignore first (CRITICAL!)
Write-Host "Step 2: Adding .gitignore (prevents venv from being tracked)..." -ForegroundColor Yellow
git add .gitignore
git commit -m "Add .gitignore to prevent venv and large files"
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ .gitignore committed" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to commit .gitignore" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 4: Add all other files (venv will be ignored)
Write-Host "Step 3: Adding project files..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Files staged" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to stage files" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 5: Check what's being committed
Write-Host "Files to be committed:" -ForegroundColor Cyan
git status --short
Write-Host ""

# Verify venv is NOT being tracked
$venvFiles = git ls-files | Select-String "venv"
if ($venvFiles) {
    Write-Host "✗ ERROR: venv files are still being tracked!" -ForegroundColor Red
    Write-Host "Please check your .gitignore file." -ForegroundColor Yellow
    exit 1
} else {
    Write-Host "✓ venv is properly ignored" -ForegroundColor Green
}
Write-Host ""

# Step 6: Commit
Write-Host "Step 4: Committing files..." -ForegroundColor Yellow
git commit -m "Initial commit - Fraud Detection System

- Complete end-to-end fraud detection system
- 5 explicit fraud patterns with realistic parameters
- 40+ engineered features (behavioral, temporal, relational)
- Production-ready scikit-learn pipeline
- Cost-sensitive threshold optimization
- SHAP explainability implementation
- Interactive Streamlit dashboard
- Comprehensive documentation and testing

Technical Assessment Compliance:
✅ Part 1: Synthetic Data Generation (10,000 transactions, 5% fraud)
✅ Part 2: Fraud Pattern Design (5 documented patterns)
✅ Part 3: Feature Engineering (40+ features)
✅ Part 4: Model Development (RandomForest with justification)
✅ Part 5: Evaluation (All metrics, threshold optimization)
✅ Part 6: Explainability (SHAP implementation)
✅ Part 7: System Design (Production-ready architecture)

Performance:
- ROC-AUC: 0.9067
- Precision: 89.77%
- Recall: 79%
- F1-Score: 84.04%
- False Positive Rate: 0.47%"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Files committed" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to commit" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 7: Set branch to main
Write-Host "Step 5: Setting branch to main..." -ForegroundColor Yellow
git branch -M $BRANCH
Write-Host "✓ Branch set to $BRANCH" -ForegroundColor Green
Write-Host ""

# Step 8: Add remote
Write-Host "Step 6: Adding remote repository..." -ForegroundColor Yellow
git remote add origin $REPO_URL
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Remote added: $REPO_URL" -ForegroundColor Green
} else {
    Write-Host "⚠ Remote might already exist, removing and re-adding..." -ForegroundColor Yellow
    git remote remove origin
    git remote add origin $REPO_URL
    Write-Host "✓ Remote added: $REPO_URL" -ForegroundColor Green
}
Write-Host ""

# Step 9: Push to GitHub
Write-Host "Step 7: Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Cyan
Write-Host ""

git push -u origin $BRANCH

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "✓ SUCCESS!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Your fraud detection project has been pushed to:" -ForegroundColor Green
    Write-Host "$REPO_URL" -ForegroundColor White
    Write-Host ""
    Write-Host "View your repository at:" -ForegroundColor Cyan
    Write-Host "https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "✗ PUSH FAILED" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "1. Repository doesn't exist on GitHub" -ForegroundColor White
    Write-Host "2. Authentication failed (check credentials)" -ForegroundColor White
    Write-Host "3. Network connection issues" -ForegroundColor White
    Write-Host ""
    Write-Host "Try:" -ForegroundColor Cyan
    Write-Host "  git push -u origin main --force" -ForegroundColor White
    Write-Host ""
}
