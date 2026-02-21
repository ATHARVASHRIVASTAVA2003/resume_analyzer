# Demo Quick Reference Card
## 4-5 Minute Code Walkthrough Cheat Sheet

---

## 🎬 RECORDING COMMANDS

### Before Recording:
```bash
# Activate environment
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate  # Windows

# Verify everything works
python quick_test.py
streamlit run app.py
```

### During Demo:
```bash
# Show quick test
python quick_test.py

# Launch dashboard
streamlit run app.py
```

---

## ⏱️ TIME MARKERS (Strict)

| Time | Section | What to Show |
|------|---------|--------------|
| 0:00-0:45 | Intro | Project structure, approach |
| 0:45-1:30 | Data Gen | Fraud patterns code |
| 1:30-2:15 | Features | 40+ features, composites |
| 2:15-2:50 | Model | Pipeline, training |
| 2:50-3:20 | Threshold | Cost optimization |
| 3:20-3:50 | SHAP | Explainability code |
| 3:50-4:50 | Demo | Live execution |
| 4:50-5:00 | Close | Key takeaways |

---

## 📝 KEY TALKING POINTS

### Introduction (45 sec):
- "Complete end-to-end system, not just a notebook"
- "Three focus areas: realistic patterns, sophisticated features, production-ready"
- "All code written from scratch"

### Data Generation (45 sec):
- "Five explicit fraud patterns, not random"
- "Velocity: 5-10 transactions in 2 hours"
- "Amount: 10-50x user average"
- "Location: impossible travel"
- "Weighted distribution: 30-25-20-15-10"

### Feature Engineering (45 sec):
- "Over 40 features across multiple dimensions"
- "Behavioral: user patterns, deviations"
- "Velocity: rolling windows, burst detection"
- "Composite risk scores combine multiple signals"

### Model Pipeline (35 sec):
- "Complete scikit-learn pipeline prevents leakage"
- "OneHotEncoding + StandardScaling"
- "RandomForest: 300 trees, balanced weights"
- "Serialized with joblib for deployment"

### Threshold (30 sec):
- "19 thresholds evaluated"
- "Cost function: 10×FN + 1×FP"
- "Optimal: 0.35, not 0.5"
- "Business-driven, not accuracy-driven"

### SHAP (30 sec):
- "TreeExplainer for RandomForest"
- "Handles sparse matrices from encoding"
- "Per-transaction explanations in dashboard"
- "Critical for trust and compliance"

### Live Demo (60 sec):
- "Quick test shows complete workflow"
- "Dashboard demonstrates interactivity"
- "Threshold adjustment in real-time"
- "SHAP explains individual predictions"

### Closing (10 sec):
- "Six key features: patterns, features, pipeline, cost, SHAP, dashboard"
- "Production-ready and fully documented"

---

## 💻 CODE SNIPPETS TO HIGHLIGHT

### 1. Fraud Pattern (show in generate_data.py):
```python
# Velocity attack - 5-10 rapid transactions
for j in range(np.random.randint(5, 11)):
    transaction_time = base_time + timedelta(minutes=np.random.randint(0, 120))
```

### 2. Feature Engineering (show in advanced_features.py):
```python
# Amount deviation from baseline
df['amount_deviation'] = abs(df['amount'] - df['user_avg_amount']) / (df['user_avg_amount'] + 1)

# Composite risk score
df['velocity_risk_score'] = (
    df['is_burst'] * 0.3 + 
    df['high_velocity_seq'] * 0.3 + 
    df['is_night_transaction'] * 0.2 +
    df['high_ip_risk'] * 0.2
)
```

### 3. Pipeline (show in features.py):
```python
pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('clf', model)
])

RandomForestClassifier(
    n_estimators=300,
    class_weight='balanced',  # Handles imbalance
    random_state=42
)
```

### 4. Cost Optimization (show in evaluate.py):
```python
cost = COST_FALSE_NEGATIVE * fn + COST_FALSE_POSITIVE * fp
best = min(results, key=lambda r: r['cost'])
```

### 5. SHAP (show in explain.py):
```python
explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(X_for_shap)
if isinstance(shap_values, list):
    shap_values_to_plot = shap_values[1]  # Fraud class
```

---

## 🎯 KEY FEATURES TO EMPHASIZE

### Must Mention:
1. ✅ **5 explicit fraud patterns** (not random)
2. ✅ **40+ engineered features** (sophisticated)
3. ✅ **Production pipeline** (prevents leakage)
4. ✅ **Cost-sensitive** (business-driven)
5. ✅ **SHAP explainability** (transparency)
6. ✅ **Interactive dashboard** (human-in-loop)

### Power Phrases:
- "Not just random labels"
- "Production-ready architecture"
- "Cost-sensitive optimization"
- "Complete explainability"
- "Business-driven decisions"
- "Composite risk scores"

---

## 🖥️ SCREEN SETUP

### IDE Settings:
- Font size: 14-16pt
- Theme: Light (better for video)
- Line numbers: ON
- Minimap: OFF (less distraction)

### Terminal Settings:
- Font size: 14-16pt
- Clear history before recording
- Use simple prompt (no fancy themes)

### Files to Have Open:
1. `src/generate_data.py` (fraud patterns)
2. `src/advanced_features.py` (feature engineering)
3. `src/features.py` (pipeline)
4. `src/evaluate.py` (threshold)
5. `src/explain.py` (SHAP)
6. Terminal (for demo)

---

## 🎤 NARRATION REMINDERS

### Pace:
- Speak at **moderate pace** (not too fast)
- **Pause** when switching screens (2 seconds)
- **Slow down** for key points
- **Speed up** for transitions

### Tone:
- **Confident** but not arrogant
- **Enthusiastic** about your work
- **Clear** and articulate
- **Professional** but personable

### Avoid:
- ❌ "Um", "uh", "like"
- ❌ Reading code line by line
- ❌ Apologizing for code
- ❌ Getting lost in details
- ❌ Going over 5 minutes

---

## 🚨 COMMON MISTAKES

### Don't:
1. ❌ Spend too long on any one section
2. ❌ Forget to show the live demo
3. ❌ Read code without explaining WHY
4. ❌ Skip the key features
5. ❌ Go over 5 minutes
6. ❌ Have unreadable font size
7. ❌ Show errors or bugs
8. ❌ Forget to test before recording

### Do:
1. ✅ Stick to time markers
2. ✅ Show working demo
3. ✅ Explain design choices
4. ✅ Highlight innovations
5. ✅ Stay under 5 minutes
6. ✅ Use large, readable fonts
7. ✅ Test everything first
8. ✅ Practice 3-5 times

---

## 📊 DEMO FLOW

### Terminal Demo (60 seconds):
```
1. Show command: python quick_test.py
2. Wait for data generation (10s)
3. Wait for training (15s)
4. Show results (5s)
5. Highlight key metrics
```

### Dashboard Demo (30 seconds):
```
1. Launch: streamlit run app.py
2. Show overview (5s)
3. Adjust threshold (5s)
4. Select transaction (5s)
5. Show SHAP explanation (10s)
6. Show top risky list (5s)
```

---

## ✅ PRE-RECORDING CHECKLIST

### Environment:
- [ ] Virtual environment activated
- [ ] All packages installed
- [ ] Data generated
- [ ] Model trained
- [ ] Dashboard tested

### Screen:
- [ ] Font sizes increased (14-16pt)
- [ ] Light theme enabled
- [ ] Unnecessary apps closed
- [ ] Notifications disabled
- [ ] Desktop cleaned

### Recording:
- [ ] Screen recorder tested
- [ ] Microphone tested
- [ ] Audio levels checked
- [ ] Recording area selected
- [ ] Backup plan ready

### Practice:
- [ ] Dry run completed (3-5 times)
- [ ] Timing verified (4-5 min)
- [ ] Code sections bookmarked
- [ ] Demo tested
- [ ] Script memorized

---

## 🎬 RECORDING WORKFLOW

### 1. Setup (5 minutes):
- Open all necessary files
- Clear terminal
- Test microphone
- Start screen recorder

### 2. Record (5 minutes):
- Follow time markers strictly
- Speak clearly and confidently
- Show code and demo
- End with key takeaways

### 3. Review (10 minutes):
- Watch entire video
- Check audio quality
- Verify code readability
- Confirm timing
- Test demo sections

### 4. Re-record if needed:
- If over 5 minutes
- If audio is unclear
- If demo fails
- If major mistakes

---

## 📤 UPLOAD CHECKLIST

### Video File:
- [ ] Duration: 4-5 minutes
- [ ] Format: MP4
- [ ] Resolution: 1920×1080
- [ ] Audio: Clear and audible
- [ ] Size: Under 500MB

### YouTube:
- [ ] Title: "Fraud Detection - Code Demo | [Name]"
- [ ] Description: Project overview + timestamps
- [ ] Visibility: Unlisted
- [ ] Link tested

### Google Drive:
- [ ] File uploaded
- [ ] Sharing: Anyone with link
- [ ] Link tested in incognito
- [ ] Video plays without download

---

## 🎯 SUCCESS METRICS

Your video should show:
1. ✅ Clear code explanation
2. ✅ Key features highlighted
3. ✅ Design choices justified
4. ✅ Working live demo
5. ✅ Professional delivery
6. ✅ Under 5 minutes
7. ✅ Readable code
8. ✅ Confident narration

---

## 💡 LAST-MINUTE TIPS

### Before Recording:
1. Take a deep breath
2. Smile (it affects your voice)
3. Have water nearby
4. Close all distractions
5. Remember: You know this!

### During Recording:
1. Speak to the camera/screen
2. Use natural gestures
3. Pause between sections
4. Don't rush
5. Show enthusiasm

### If You Make a Mistake:
1. Pause briefly
2. Correct and continue
3. Don't apologize excessively
4. Keep going
5. Can edit later if needed

---

## 🚀 YOU'RE READY!

**Remember:**
- You built an excellent system
- You know the code inside out
- You've practiced multiple times
- The demo works perfectly
- You're ready to succeed

**Take a deep breath and show them what you've built!**

Good luck! 🎯

---

## 📞 EMERGENCY CONTACTS

If technical issues:
- Have screenshots ready
- Pre-recorded demo backup
- Static visualizations
- Explain what should happen

**Most important: Stay calm and confident!**
