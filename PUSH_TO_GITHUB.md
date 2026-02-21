# Push Fraud Detection Project to GitHub

## Quick Commands (Copy-Paste)

### Option 1: Using PowerShell Script (Recommended)
```powershell
# Run the automated script
.\push_to_github.ps1
```

### Option 2: Manual Commands
```powershell
# 1. Remove old git history (if exists)
Remove-Item -Recurse -Force .git -ErrorAction SilentlyContinue

# 2. Initialize new repository
git init

# 3. Add .gitignore FIRST (prevents venv from being tracked)
git add .gitignore
git commit -m "Add .gitignore"

# 4. Add all project files (venv will be ignored)
git add .

# 5. Commit with detailed message
git commit -m "Initial commit - Fraud Detection System"

# 6. Set branch to main
git branch -M main

# 7. Add remote repository
git remote add origin https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer.git

# 8. Push to GitHub
git push -u origin main
```

---

## ⚠️ IMPORTANT: Verify Before Pushing

### Check that venv is NOT being tracked:
```powershell
# This should return NOTHING
git ls-files | Select-String "venv"
```

### Check what files are being committed:
```powershell
git status
```

You should see:
- ✅ `src/` folder
- ✅ `data/` folder (with .gitkeep, not CSV files)
- ✅ `models/` folder (with final models only)
- ✅ `reports/` folder
- ✅ Documentation files (*.md)
- ✅ `requirements.txt`
- ✅ `.gitignore`

You should NOT see:
- ❌ `venv/` folder
- ❌ `__pycache__/` folders
- ❌ Large CSV files
- ❌ `.pyc` files

---

## If Push Fails

### Error: "Repository not found"
```powershell
# Make sure the repository exists on GitHub
# Go to: https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer
# If it doesn't exist, create it first
```

### Error: "Large files detected"
```powershell
# Check what large files are being tracked
git ls-files | ForEach-Object { 
    $size = (Get-Item $_).Length / 1MB
    if ($size -gt 10) { 
        Write-Host "$_ : $([math]::Round($size, 2)) MB" 
    }
}

# If you see venv files, your .gitignore isn't working
# Make sure .gitignore was committed FIRST
```

### Error: "Authentication failed"
```powershell
# Use GitHub Personal Access Token
# 1. Go to: https://github.com/settings/tokens
# 2. Generate new token (classic)
# 3. Use token as password when prompted
```

### Force Push (if repository already has content)
```powershell
git push -u origin main --force
```

---

## After Successful Push

### Verify on GitHub:
1. Go to: https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer
2. Check that:
   - ✅ All source code is there
   - ✅ Documentation is visible
   - ✅ No `venv/` folder
   - ✅ Repository size is reasonable (<50 MB)

### Create requirements.txt (if not exists):
```powershell
# Activate your virtual environment
.\venv\Scripts\activate

# Generate requirements
pip freeze > requirements.txt

# Commit and push
git add requirements.txt
git commit -m "Add requirements.txt"
git push
```

---

## Repository Structure on GitHub

Your repository should look like this:

```
resume_analyzer/
├── .gitignore
├── README.md
├── USAGE_GUIDE.md
├── requirements.txt
├── setup.py
├── app.py
├── quick_test.py
├── test_system.py
├── data/
│   ├── raw/.gitkeep
│   └── processed/.gitkeep
├── docs/
│   └── fraud_patterns.md
├── models/
│   ├── fraud_pipeline.joblib
│   └── threshold.json
├── reports/
│   ├── figures/
│   │   ├── confusion_matrix.png
│   │   ├── roc_curve.png
│   │   ├── pr_curve.png
│   │   └── shap_summary.png
│   └── metrics/
│       ├── metrics.json
│       └── threshold_search.json
└── src/
    ├── generate_data.py
    ├── advanced_features.py
    ├── temporal_features.py
    ├── data_prep.py
    ├── features.py
    ├── train_model.py
    ├── evaluate.py
    ├── explain.py
    └── score_new_transactions.py
```

---

## Troubleshooting

### "Everything up-to-date" but nothing on GitHub
```powershell
# Check remote URL
git remote -v

# Should show:
# origin  https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer.git (fetch)
# origin  https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer.git (push)

# If wrong, update it:
git remote set-url origin https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer.git
```

### "fatal: refusing to merge unrelated histories"
```powershell
# Force push (overwrites remote)
git push -u origin main --force
```

### Still getting venv errors
```powershell
# Nuclear option - completely fresh start
Remove-Item -Recurse -Force .git
git init
git add .gitignore
git commit -m "Add .gitignore"
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer.git
git push -u origin main --force
```

---

## Quick Checklist

Before pushing:
- [ ] `.gitignore` exists and is committed first
- [ ] `venv/` is NOT in git (check with `git ls-files | Select-String "venv"`)
- [ ] No files over 100 MB
- [ ] `requirements.txt` exists
- [ ] Documentation is complete
- [ ] Repository URL is correct

After pushing:
- [ ] Check GitHub repository
- [ ] Verify all files are there
- [ ] Verify no `venv/` folder
- [ ] Clone to test: `git clone https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer.git`

---

## Need Help?

If you're still having issues:

1. **Check repository exists**: https://github.com/ATHARVASHRIVASTAVA2003/resume_analyzer
2. **Use the PowerShell script**: `.\push_to_github.ps1`
3. **Try manual commands** from Option 2 above
4. **Force push** if needed: `git push -u origin main --force`

Good luck! 🚀
