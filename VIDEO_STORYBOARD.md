# Video Storyboard - Visual Guide
## 4-5 Minute Code Demo Visualization

---

## 🎬 SCENE 1: Introduction (0:00-0:45)

```
┌─────────────────────────────────────────┐
│  VS Code - Project Root                 │
│  ┌───────────────────────────────────┐  │
│  │ 📁 Financial-Fraud-Risk-Engine    │  │
│  │   📁 data/                        │  │
│  │   📁 docs/                        │  │
│  │   📁 models/                      │  │
│  │   📁 reports/                     │  │
│  │   📁 src/                         │  │
│  │     📄 generate_data.py           │  │
│  │     📄 advanced_features.py       │  │
│  │     📄 train_model.py             │  │
│  │   📄 app.py                       │  │
│  │   📄 README.md                    │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"Hello! I'm [Name], and today I'll walk you 
through my fraud detection system code..."

MOUSE: Hover over folders, expand src/
```

---

## 🎬 SCENE 2: Data Generation (0:45-1:30)

```
┌─────────────────────────────────────────┐
│  src/generate_data.py                   │
│  ┌───────────────────────────────────┐  │
│  │ def inject_fraud_patterns():      │  │
│  │                                   │  │
│  │   # Velocity attacks (30%)        │  │
│  │   for i in range(int(n * 0.3)):  │  │
│  │     for j in range(5, 11):       │  │
│  │       time = base + timedelta(   │  │
│  │         minutes=randint(0, 120)  │  │ ← HIGHLIGHT
│  │       )                           │  │
│  │                                   │  │
│  │   # Amount spikes (25%)           │  │
│  │   spike = normal * uniform(      │  │
│  │     10, 50                        │  │ ← HIGHLIGHT
│  │   )                               │  │
│  │                                   │  │
│  │   # Location inconsistency (20%) │  │
│  │   countries = ['US', 'UK', ...]  │  │
│  │   country1, country2 = choice()  │  │ ← HIGHLIGHT
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"Five explicit fraud patterns, not random..."
"Velocity: 5-10 transactions in 2 hours..."
"Amount: 10-50x user average..."

MOUSE: Highlight key lines, scroll through patterns
```

---

## 🎬 SCENE 3: Feature Engineering (1:30-2:15)

```
┌─────────────────────────────────────────┐
│  src/advanced_features.py               │
│  ┌───────────────────────────────────┐  │
│  │ def create_user_behavioral():     │  │
│  │                                   │  │
│  │   # Amount deviation              │  │
│  │   df['amount_deviation'] = abs(  │  │
│  │     df['amount'] -                │  │
│  │     df['user_avg_amount']         │  │
│  │   ) / (df['user_avg_amount'] + 1)│  │ ← HIGHLIGHT
│  │                                   │  │
│  │ def create_velocity_features():   │  │
│  │                                   │  │
│  │   # Rolling window                │  │
│  │   df['rolling_mean'] =            │  │
│  │     df.groupby('user_id')         │  │
│  │       ['amount'].transform(       │  │
│  │         lambda x: x.rolling(      │  │
│  │           window=3                │  │ ← HIGHLIGHT
│  │         ).mean()                  │  │
│  │       )                           │  │
│  │                                   │  │
│  │ # Composite risk score            │  │
│  │ df['velocity_risk'] = (           │  │
│  │   df['is_burst'] * 0.3 +          │  │
│  │   df['high_velocity'] * 0.3 +     │  │ ← HIGHLIGHT
│  │   df['unusual_time'] * 0.2 +      │  │
│  │   df['high_ip_risk'] * 0.2        │  │
│  │ )                                 │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"Over 40 features across multiple dimensions..."
"Amount deviation catches unusual spending..."
"Rolling windows detect burst activity..."
"Composite scores combine multiple signals..."

MOUSE: Highlight calculations, hover over formulas
```

---

## 🎬 SCENE 4: Model Pipeline (2:15-2:50)

```
┌─────────────────────────────────────────┐
│  src/features.py                        │
│  ┌───────────────────────────────────┐  │
│  │ def build_pipeline():             │  │
│  │                                   │  │
│  │   preprocessor = ColumnTransform( │  │
│  │     transformers=[                │  │
│  │       ('categorical',             │  │
│  │        OneHotEncoder(             │  │
│  │          handle_unknown='ignore'  │  │ ← HIGHLIGHT
│  │        ),                         │  │
│  │        CATEGORICAL_FEATURES),     │  │
│  │       ('numeric',                 │  │
│  │        StandardScaler(),          │  │
│  │        NUMERIC_FEATURES)          │  │
│  │     ]                             │  │
│  │   )                               │  │
│  │                                   │  │
│  │   model = RandomForestClassifier( │  │
│  │     n_estimators=300,             │  │
│  │     max_depth=8,                  │  │
│  │     class_weight='balanced',      │  │ ← HIGHLIGHT
│  │     random_state=42               │  │
│  │   )                               │  │
│  │                                   │  │
│  │   return Pipeline([               │  │
│  │     ('preprocess', preprocessor), │  │
│  │     ('clf', model)                │  │
│  │   ])                              │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"Complete pipeline prevents data leakage..."
"handle_unknown ensures production readiness..."
"Balanced weights handle 95-5 imbalance..."

MOUSE: Highlight pipeline construction, parameters
```

---

## 🎬 SCENE 5: Threshold Optimization (2:50-3:20)

```
┌─────────────────────────────────────────┐
│  src/evaluate.py                        │
│  ┌───────────────────────────────────┐  │
│  │ def compute_threshold_metrics():  │  │
│  │                                   │  │
│  │   for thr in thresholds:          │  │
│  │     y_pred = (y_proba >= thr)     │  │
│  │     tn, fp, fn, tp = confusion()  │  │
│  │                                   │  │
│  │     # Business cost               │  │
│  │     cost = (                      │  │
│  │       COST_FALSE_NEGATIVE * fn +  │  │ ← HIGHLIGHT
│  │       COST_FALSE_POSITIVE * fp    │  │
│  │     )                             │  │
│  │                                   │  │
│  │ def pick_best_threshold():        │  │
│  │   best = min(                     │  │
│  │     results,                      │  │
│  │     key=lambda r: r['cost']       │  │ ← HIGHLIGHT
│  │   )                               │  │
│  │   return best                     │  │
│  │                                   │  │
│  │ # Constants                       │  │
│  │ COST_FALSE_NEGATIVE = 10.0        │  │ ← HIGHLIGHT
│  │ COST_FALSE_POSITIVE = 1.0         │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"19 thresholds evaluated..."
"Cost function: 10×FN + 1×FP..."
"Optimal: 0.35, not 0.5..."
"Business-driven, not accuracy-driven..."

MOUSE: Highlight cost calculation, constants
```

---

## 🎬 SCENE 6: Explainability (3:20-3:50)

```
┌─────────────────────────────────────────┐
│  src/explain.py                         │
│  ┌───────────────────────────────────┐  │
│  │ def compute_global_shap():        │  │
│  │                                   │  │
│  │   # Extract from pipeline         │  │
│  │   preprocessor = model['preproc'] │  │
│  │   clf = model['clf']              │  │
│  │                                   │  │
│  │   # Handle sparse matrices        │  │
│  │   if sp.issparse(X_transformed):  │  │
│  │     X_for_shap =                  │  │
│  │       X_transformed.toarray()     │  │ ← HIGHLIGHT
│  │                                   │  │
│  │   # TreeExplainer                 │  │
│  │   explainer = shap.TreeExplainer( │  │
│  │     clf                           │  │ ← HIGHLIGHT
│  │   )                               │  │
│  │   shap_values = explainer(        │  │
│  │     X_for_shap                    │  │
│  │   )                               │  │
│  │                                   │  │
│  │   # Handle binary classification  │  │
│  │   if isinstance(shap_values, list):│ │
│  │     shap_values = shap_values[1]  │  │ ← HIGHLIGHT
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"SHAP TreeExplainer for RandomForest..."
"Handles sparse matrices from encoding..."
"Per-transaction explanations in dashboard..."
"Critical for trust and compliance..."

MOUSE: Highlight TreeExplainer, sparse handling
```

---

## 🎬 SCENE 7: Live Demo - Terminal (3:50-4:20)

```
┌─────────────────────────────────────────┐
│  Terminal                               │
│  ┌───────────────────────────────────┐  │
│  │ $ python quick_test.py            │  │
│  │                                   │  │
│  │ ⚡ QUICK FUNCTIONAL TEST           │  │
│  │ ================================  │  │
│  │                                   │  │
│  │ 1. Testing data generation...     │  │
│  │    ✓ Generated 10000 transactions │  │ ← SHOW
│  │                                   │  │
│  │ 2. Testing data preparation...    │  │
│  │    ✓ Prepared 8000 training       │  │ ← SHOW
│  │                                   │  │
│  │ 3. Testing model training...      │  │
│  │    ✓ Model saved (2.3 MB)         │  │ ← SHOW
│  │                                   │  │
│  │ 4. Testing prediction...          │  │
│  │    ✓ Made 2000 predictions        │  │
│  │    ✓ 88 fraud flags               │  │ ← SHOW
│  │                                   │  │
│  │ 🎉 QUICK TEST PASSED!             │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"Running quick test to show complete workflow..."
"Generating data with fraud patterns..."
"Training the model..."
"Making predictions..."
"88 transactions flagged as fraud!"

MOUSE: Hover over key output lines
```

---

## 🎬 SCENE 8: Live Demo - Dashboard (4:20-4:50)

```
┌─────────────────────────────────────────┐
│  Streamlit Dashboard                    │
│  ┌───────────────────────────────────┐  │
│  │ Financial Fraud Risk Engine       │  │
│  │                                   │  │
│  │ Overview                          │  │
│  │ ┌─────────┬─────────┬─────────┐  │  │
│  │ │ Total   │ True    │ Flagged │  │  │
│  │ │ 2,000   │ 5.00%   │ 4.40%   │  │  │ ← SHOW
│  │ └─────────┴─────────┴─────────┘  │  │
│  │                                   │  │
│  │ Threshold: [====●====] 0.35       │  │ ← ADJUST
│  │                                   │  │
│  │ Risk Distribution                 │  │
│  │ [Histogram showing separation]    │  │ ← SHOW
│  │                                   │  │
│  │ Top High-Risk Transactions        │  │
│  │ ┌─────┬──────┬──────┬──────┐    │  │
│  │ │ ID  │ Prob │ Flag │ Amt  │    │  │
│  │ │ 9822│ 0.97 │  1   │ 256  │    │  │ ← CLICK
│  │ │ 9608│ 0.97 │  1   │ 323  │    │  │
│  │ └─────┴──────┴──────┴──────┘    │  │
│  │                                   │  │
│  │ SHAP Explanation                  │  │
│  │ velocity_risk    ████████ 0.45    │  │ ← SHOW
│  │ amount_deviation ██████   0.32    │  │
│  │ device_shared    ████     0.18    │  │
│  │ unusual_merchant ██       0.05    │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"Interactive dashboard for analysts..."
"Adjust threshold dynamically..."
"Top risky transactions ranked..."
"SHAP shows why it was flagged..."
"Velocity, amount, device sharing..."

MOUSE: Move slider, click transaction, point to SHAP
```

---

## 🎬 SCENE 9: Closing (4:50-5:00)

```
┌─────────────────────────────────────────┐
│  VS Code - Project Root                 │
│  ┌───────────────────────────────────┐  │
│  │ KEY FEATURES:                     │  │
│  │                                   │  │
│  │ ✅ 5 Explicit Fraud Patterns      │  │
│  │ ✅ 40+ Engineered Features        │  │
│  │ ✅ Production Pipeline            │  │
│  │ ✅ Cost-Sensitive Optimization    │  │
│  │ ✅ SHAP Explainability            │  │
│  │ ✅ Interactive Dashboard          │  │
│  │                                   │  │
│  │ READY FOR PRODUCTION DEPLOYMENT   │  │
│  │                                   │  │
│  │ Thank you for watching!           │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

NARRATION:
"Six key features in my code..."
"Realistic patterns, sophisticated features..."
"Production pipeline, cost optimization..."
"Complete explainability, interactive dashboard..."
"Fully functional and ready for deployment..."
"Thank you!"

MOUSE: Hover over project structure
```

---

## 🎨 Visual Design Guidelines

### Color Coding:
- **Green highlights** - Key code sections
- **Yellow highlights** - Important parameters
- **Blue highlights** - Function names
- **Red highlights** - Critical values

### Mouse Movements:
- **Hover** - Draw attention
- **Underline** - Emphasize text
- **Circle** - Highlight numbers
- **Arrow** - Point to specific lines

### Screen Transitions:
- **Fade** - Between major sections
- **Slide** - Between code files
- **Zoom** - To highlight specific code
- **Pan** - To show full context

---

## 📐 Layout Recommendations

### Split Screen (Recommended):
```
┌──────────────┬──────────────┐
│              │              │
│   IDE/Code   │   Terminal   │
│              │              │
│   (60%)      │   (40%)      │
│              │              │
└──────────────┴──────────────┘
```

### Full Screen:
```
┌─────────────────────────────┐
│                             │
│      IDE/Code/Dashboard     │
│                             │
│         (100%)              │
│                             │
└─────────────────────────────┘
```

### Picture-in-Picture:
```
┌─────────────────────────────┐
│                             │
│      Main Content           │
│                             │
│              ┌──────────┐   │
│              │ Terminal │   │
│              └──────────┘   │
└─────────────────────────────┘
```

---

## 🎬 Camera Angles (If Including Webcam)

### Option 1: Code Only (Recommended)
- No webcam
- Full screen for code
- Maximum readability

### Option 2: Picture-in-Picture
- Small webcam in corner
- Shows presenter
- More personal

### Option 3: Side-by-Side
- Split screen
- Code + presenter
- Professional look

---

## 🎵 Audio Guidelines

### Background Music:
- ❌ **Don't use** - Can be distracting
- ✅ **Silent** - Focus on narration

### Sound Effects:
- ❌ **Don't use** - Unprofessional
- ✅ **Natural** - Keyboard clicks OK

### Voice:
- ✅ **Clear** - Speak directly to mic
- ✅ **Confident** - Show enthusiasm
- ✅ **Paced** - Not too fast
- ✅ **Professional** - Avoid filler words

---

## 📊 Visual Hierarchy

### Most Important (Largest):
1. Code being explained
2. Terminal output
3. Dashboard metrics

### Important (Medium):
1. File names
2. Function names
3. Comments

### Context (Smaller):
1. Line numbers
2. Folder structure
3. Status bar

---

## ✅ Visual Quality Checklist

### Before Recording:
- [ ] Font size 14-16pt (readable)
- [ ] Light theme (better contrast)
- [ ] Line numbers visible
- [ ] Syntax highlighting enabled
- [ ] Minimap hidden (less clutter)
- [ ] Terminal clear
- [ ] No sensitive info visible

### During Recording:
- [ ] Smooth mouse movements
- [ ] Clear highlights
- [ ] Proper pacing
- [ ] Good transitions
- [ ] No distractions

### After Recording:
- [ ] Code is readable
- [ ] Highlights are visible
- [ ] Transitions are smooth
- [ ] Audio is clear
- [ ] Timing is correct

---

## 🎯 Final Visual Tips

### Do:
- ✅ Use large, readable fonts
- ✅ Highlight key code sections
- ✅ Show working demo
- ✅ Use smooth transitions
- ✅ Keep it clean and professional

### Don't:
- ❌ Use tiny fonts
- ❌ Show cluttered screens
- ❌ Have distracting backgrounds
- ❌ Use flashy effects
- ❌ Show errors or bugs

---

**Your storyboard is complete! Time to bring it to life!** 🎬✨
