# Screen Recording Script - Exact Actions & Words
## Frame-by-Frame Guide for 4-5 Minute Demo

---

## 🎬 FRAME 1: Introduction (0:00-0:45)

### Screen Action:
1. Start with VS Code showing project root
2. Show file explorer with all folders visible
3. Briefly scroll through README.md

### Exact Words:
> "Hello! I'm [Your Name], and today I'll walk you through my fraud detection system code and demonstrate it live.
>
> [Gesture to file tree]
>
> The project follows a production-ready structure. You can see separate modules for data generation, feature engineering, model training, evaluation, and deployment.
>
> My approach was to build a complete end-to-end system. I focused on three things: realistic fraud patterns in synthetic data, sophisticated feature engineering with over 40 features, and production-ready architecture with proper pipelines and explainability.
>
> I wrote all the code from scratch using scikit-learn, SHAP, and Streamlit. Let's dive into the key components."

### Mouse Actions:
- Hover over `src/` folder
- Expand to show files
- Hover over `data/`, `models/`, `reports/`

---

## 🎬 FRAME 2: Data Generation (0:45-1:30)

### Screen Action:
1. Open `src/generate_data.py`
2. Scroll to `inject_fraud_patterns()` function (line ~150)
3. Show velocity attack pattern (line ~170)
4. Scroll to amount spike pattern (line ~200)
5. Show location inconsistency (line ~230)

### Exact Words:
> "First, let's look at data generation. This is where I implemented five explicit fraud patterns.
>
> [Scroll to velocity function]
>
> Here's the velocity attack pattern. It generates 5 to 10 rapid transactions within a 2-hour window. Notice I'm using realistic time intervals.
>
> [Highlight this code]
>
> ```python
> for j in range(np.random.randint(5, 11)):
>     transaction_time = base_time + timedelta(minutes=np.random.randint(0, 120))
> ```
>
> [Scroll to amount spike]
>
> The amount spike pattern creates transactions 10 to 50 times the user's average spending.
>
> [Highlight]
>
> ```python
> spike_amount = normal_amount * np.random.uniform(10, 50)
> ```
>
> [Scroll to location]
>
> Location inconsistencies generate two transactions from different countries within 30 to 120 minutes - physically impossible travel.
>
> A key feature here is that I'm not randomly labeling transactions. Each fraud case follows a specific, detectable pattern based on real-world fraud intelligence. The patterns are weighted: 30% velocity, 25% amount spikes, 20% location, 15% device sharing, and 10% merchant rings."

### Mouse Actions:
- Highlight line numbers
- Underline key code sections
- Hover over pattern percentages

---

## 🎬 FRAME 3: Feature Engineering (1:30-2:15)

### Screen Action:
1. Open `src/advanced_features.py`
2. Scroll to `create_user_behavioral_features()` (line ~30)
3. Show amount deviation calculation (line ~50)
4. Scroll to `create_velocity_features()` (line ~80)
5. Show rolling window code (line ~95)
6. Scroll to composite risk scores (line ~250)

### Exact Words:
> "Now let's look at feature engineering - this is where the ML magic happens.
>
> [Show function]
>
> I created over 40 features across multiple dimensions. Here's the user behavioral features function. It calculates user spending patterns, transaction frequency, and amount deviations.
>
> [Highlight this line]
>
> ```python
> df['amount_deviation'] = abs(df['amount'] - df['user_avg_amount']) / (df['user_avg_amount'] + 1)
> ```
>
> This calculates how much each transaction deviates from the user's average. This catches unusual spending patterns.
>
> [Scroll to velocity]
>
> The velocity features use rolling windows to detect burst activity.
>
> [Highlight]
>
> ```python
> df['rolling_amount_mean'] = df.groupby('user_id')['amount'].transform(
>     lambda x: x.rolling(window=3, min_periods=1).mean()
> )
> ```
>
> This rolling mean over the last 3 transactions helps identify sudden spikes.
>
> [Scroll to composite]
>
> A key feature I'm proud of is these composite risk scores.
>
> [Highlight]
>
> ```python
> df['velocity_risk_score'] = (
>     df['is_burst'] * 0.3 + 
>     df['high_velocity_seq'] * 0.3 + 
>     df['is_night_transaction'] * 0.2 +
>     df['high_ip_risk'] * 0.2
> )
> ```
>
> This combines burst detection, high-frequency sequences, unusual timing, and IP risk into a single meaningful metric. This is more powerful than individual features."

### Mouse Actions:
- Highlight each code block
- Hover over variable names
- Underline key calculations

---

## 🎬 FRAME 4: Model Pipeline (2:15-2:50)

### Screen Action:
1. Open `src/features.py`
2. Show `build_pipeline()` function (line ~30)
3. Show `build_preprocessor()` (line ~15)
4. Show `build_model()` (line ~25)
5. Open `src/train_model.py`
6. Show training function (line ~30)

### Exact Words:
> "Let me show you the model pipeline code.
>
> [Show build_pipeline]
>
> I built a complete scikit-learn pipeline with preprocessing and the classifier. This is crucial for preventing data leakage.
>
> [Highlight preprocessor]
>
> ```python
> preprocessor = ColumnTransformer([
>     ('categorical', OneHotEncoder(handle_unknown='ignore'), CATEGORICAL_FEATURES),
>     ('numeric', StandardScaler(), NUMERIC_FEATURES)
> ])
> ```
>
> The preprocessor handles categorical features with OneHotEncoding and numeric features with StandardScaling. The 'handle_unknown=ignore' ensures the model can handle new categories in production.
>
> [Show model]
>
> ```python
> RandomForestClassifier(
>     n_estimators=300,
>     max_depth=8,
>     class_weight='balanced',
>     random_state=42
> )
> ```
>
> For the classifier, I chose RandomForest with 300 trees and balanced class weights to handle the 95-5 imbalance.
>
> [Switch to train_model.py]
>
> The training code is clean and modular. It loads data, fits the pipeline, generates metrics, and saves everything with joblib.
>
> A key feature is saving both the model and metrics as JSON for audit trails and governance."

### Mouse Actions:
- Highlight pipeline construction
- Hover over class_weight parameter
- Show joblib.dump line

---

## 🎬 FRAME 5: Threshold Optimization (2:50-3:20)

### Screen Action:
1. Open `src/evaluate.py`
2. Scroll to `compute_threshold_metrics()` (line ~30)
3. Show cost calculation (line ~45)
4. Show `pick_best_threshold()` (line ~60)

### Exact Words:
> "Now threshold optimization - this is critical for fraud detection.
>
> [Show function]
>
> I evaluate 19 different thresholds from 0.05 to 0.95. For each threshold, I calculate precision, recall, F1, and business cost.
>
> [Highlight cost calculation]
>
> ```python
> cost = COST_FALSE_NEGATIVE * fn + COST_FALSE_POSITIVE * fp
> ```
>
> The cost function is simple but powerful: 10 times the false negatives plus 1 times the false positives. This reflects the business reality that missing fraud is 10 times more expensive than a false alarm.
>
> [Show pick_best]
>
> ```python
> best = min(results, key=lambda r: r['cost'])
> ```
>
> The best threshold minimizes this cost, not accuracy. This is cost-sensitive machine learning in action.
>
> The optimal threshold turns out to be 0.35, not the default 0.5. This saves significant business cost."

### Mouse Actions:
- Highlight cost formula
- Hover over COST constants
- Underline min() function

---

## 🎬 FRAME 6: Explainability (3:20-3:50)

### Screen Action:
1. Open `src/explain.py`
2. Show `compute_and_plot_global_shap()` (line ~20)
3. Show TreeExplainer initialization (line ~35)
4. Show sparse matrix handling (line ~40)
5. Open `app.py`
6. Show `explain_single_transaction()` (line ~150)

### Exact Words:
> "Explainability is essential for production fraud systems. Let me show you the SHAP implementation.
>
> [Show function]
>
> I'm using SHAP's TreeExplainer for the RandomForest model. The code extracts the preprocessor and classifier from the pipeline, transforms the data, and computes SHAP values.
>
> [Highlight]
>
> ```python
> if sp.issparse(X_transformed):
>     X_for_shap = X_transformed.toarray()
> ```
>
> A key feature is handling sparse matrices from OneHotEncoding. I convert them to dense arrays for SHAP.
>
> [Switch to app.py]
>
> ```python
> explainer = shap.TreeExplainer(clf)
> shap_values = explainer.shap_values(X_for_shap)
> if isinstance(shap_values, list):
>     shap_values_to_plot = shap_values[1]  # Fraud class
> ```
>
> For the dashboard, I implemented per-transaction explanations. This creates a bar plot showing which features contributed to the fraud prediction.
>
> This transparency is critical for fraud analysts to understand and trust the model."

### Mouse Actions:
- Highlight TreeExplainer line
- Hover over sparse matrix check
- Show SHAP plotting code

---

## 🎬 FRAME 7: Live Demo - Terminal (3:50-4:20)

### Screen Action:
1. Switch to terminal
2. Clear screen
3. Type: `python quick_test.py`
4. Press Enter
5. Watch output scroll
6. Highlight final results

### Exact Words:
> "Now let me demonstrate the system in action. I'll run the quick test script.
>
> [Type command]
>
> ```bash
> python quick_test.py
> ```
>
> [Press Enter]
>
> Watch as it generates synthetic data with fraud patterns...
>
> [Wait 5 seconds]
>
> Now preparing the data with stratified train-test split...
>
> [Wait 5 seconds]
>
> Training the RandomForest model...
>
> [Wait 5 seconds]
>
> And making predictions.
>
> [Show results]
>
> Perfect! The system generated 10,000 transactions, trained the model, and made predictions. We can see it flagged 88 transactions as fraud with high confidence."

### Mouse Actions:
- Hover over key output lines
- Highlight metrics
- Show fraud count

---

## 🎬 FRAME 8: Live Demo - Dashboard (4:20-4:50)

### Screen Action:
1. Type: `streamlit run app.py`
2. Wait for browser to open
3. Show overview section
4. Adjust threshold slider
5. Scroll to top risky transactions
6. Click on a high-risk transaction
7. Show SHAP explanation

### Exact Words:
> "Now let me show the interactive dashboard.
>
> [Type command]
>
> ```bash
> streamlit run app.py
> ```
>
> [Wait for dashboard]
>
> Here's the dashboard. We can see the risk distribution - most transactions have low fraud probability, but there's clear separation for fraud cases.
>
> [Move slider]
>
> I can adjust the threshold dynamically. Watch how the flagged count changes.
>
> [Scroll down]
>
> The dashboard shows top risky transactions ranked by fraud probability.
>
> [Click transaction]
>
> Let me select this high-risk transaction. The SHAP explanation shows exactly why it was flagged: high velocity risk score, unusual amount deviation, and shared device.
>
> This transparency is critical for fraud analysts to make informed decisions and prioritize their review."

### Mouse Actions:
- Hover over metrics
- Drag threshold slider
- Click on transaction row
- Point to SHAP bars

---

## 🎬 FRAME 9: Closing (4:50-5:00)

### Screen Action:
1. Switch back to VS Code
2. Show project structure
3. Show README.md

### Exact Words:
> "To summarize the key features in my code:
>
> One - Five explicit fraud patterns with realistic parameters.
>
> Two - Over 40 engineered features including composite risk scores.
>
> Three - Production-ready scikit-learn pipeline preventing data leakage.
>
> Four - Cost-sensitive threshold optimization minimizing business impact.
>
> Five - Complete SHAP explainability for transparency.
>
> And six - Interactive dashboard for human-in-the-loop workflows.
>
> The system is fully functional, well-documented, and ready for production deployment.
>
> Thank you for watching!"

### Mouse Actions:
- Hover over key folders
- Show documentation
- End with project root view

---

## 🎥 RECORDING SETTINGS

### OBS Studio Settings:
```
Video:
- Base Resolution: 1920x1080
- Output Resolution: 1920x1080
- FPS: 30
- Encoder: x264
- Rate Control: CBR
- Bitrate: 2500 Kbps

Audio:
- Sample Rate: 44.1 kHz
- Channels: Stereo
- Bitrate: 160 Kbps

Output:
- Format: MP4
- Encoder: H.264
```

### Screen Capture Area:
- Full screen or
- IDE window + terminal (side by side)

---

## 🎬 RECORDING WORKFLOW

### 1. Pre-Recording (5 min):
```bash
# Open all files in tabs
code src/generate_data.py
code src/advanced_features.py
code src/features.py
code src/evaluate.py
code src/explain.py
code app.py

# Clear terminal
clear

# Test commands
python quick_test.py
streamlit run app.py
```

### 2. Recording (5 min):
- Start screen recorder
- Follow script exactly
- Speak clearly
- Show code and demo
- End recording

### 3. Post-Recording (10 min):
- Watch full video
- Check audio/video quality
- Verify timing
- Re-record if needed

---

## ✅ FINAL CHECKLIST

### Before Recording:
- [ ] All files open in tabs
- [ ] Terminal cleared
- [ ] Font size 14-16pt
- [ ] Light theme enabled
- [ ] Notifications off
- [ ] Microphone tested
- [ ] Screen recorder ready

### During Recording:
- [ ] Follow time markers
- [ ] Speak clearly
- [ ] Show key code
- [ ] Run demo successfully
- [ ] Stay under 5 minutes

### After Recording:
- [ ] Video is 4-5 minutes
- [ ] Audio is clear
- [ ] Code is readable
- [ ] Demo works
- [ ] No errors shown

---

## 🚀 YOU'RE READY TO RECORD!

**Remember:**
- Stick to the script
- Show enthusiasm
- Highlight key features
- Demonstrate working system
- Stay confident

**Take a deep breath and hit record!** 🎬
