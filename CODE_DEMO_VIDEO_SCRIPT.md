# Code Demo Video Script (4-5 Minutes)
## Fraud Detection System - Code Walkthrough & Live Demonstration

---

## Video Structure
- **Duration:** 4-5 minutes
- **Format:** Screen recording with voiceover
- **Focus:** Code explanation + Live demo
- **Tools:** OBS Studio, Loom, or Zoom screen recording

---

## SECTION 1: Introduction & Approach (0:00 - 0:45)

### Screen: Show project structure in VS Code/IDE

### Script:
> "Hello! I'm [Your Name], and today I'll walk you through my fraud detection system code and demonstrate it live.
>
> [Show file tree]
>
> The project follows a production-ready structure with separate modules for data generation, feature engineering, model training, evaluation, and deployment. Let me explain my approach and the key features in the code.
>
> My approach was to build a complete end-to-end system, not just a Jupyter notebook. I focused on three things: realistic fraud patterns in synthetic data, sophisticated feature engineering with 40+ features, and production-ready architecture with proper pipelines and explainability.
>
> I wrote all the code from scratch, using scikit-learn for the ML pipeline, SHAP for explainability, and Streamlit for the interactive dashboard. Let's dive into the key code components."

### What to Show:
- Project folder structure
- README.md briefly
- Highlight key directories: src/, data/, models/, reports/

---

## SECTION 2: Data Generation Code (0:45 - 1:30)

### Screen: Open `src/generate_data.py`

### Script:
> "First, let's look at the data generation code. This is where I implemented five explicit fraud patterns.
>
> [Scroll to fraud pattern functions]
>
> Here's the velocity attack pattern - it generates 5 to 10 rapid transactions within a 2-hour window. Notice I'm using realistic time intervals and random transaction types.
>
> [Scroll to amount spike pattern]
>
> The amount spike pattern creates transactions 10 to 50 times the user's average spending. This simulates compromised accounts making large purchases.
>
> [Scroll to location inconsistency]
>
> Location inconsistencies generate two transactions from different countries within 30 to 120 minutes - physically impossible travel.
>
> [Highlight key code section]
>
> A key feature here is that I'm not just randomly labeling transactions as fraud. Each fraud case follows a specific, detectable pattern based on real-world fraud intelligence. The patterns are weighted - 30% velocity, 25% amount spikes, 20% location, 15% device sharing, and 10% merchant rings.
>
> [Show data generation execution]
>
> The code generates 10,000 transactions with exactly 5% fraud rate, matching real-world distributions."

### What to Show:
- `inject_fraud_patterns()` function
- Individual pattern functions (velocity, amount, location)
- Pattern distribution logic
- Realistic parameter choices (time windows, multipliers)

### Key Code Features to Highlight:
```python
# Velocity attack pattern
for j in range(np.random.randint(5, 11)):  # 5-10 transactions
    transaction_time = base_time + timedelta(minutes=np.random.randint(0, 120))
    
# Amount spike pattern
spike_amount = normal_amount * np.random.uniform(10, 50)  # 10-50x normal

# Location inconsistency
countries = ['US', 'UK', 'DE', 'TR', 'AU']
country1, country2 = np.random.choice(countries, 2, replace=False)
```

---

## SECTION 3: Feature Engineering Code (1:30 - 2:15)

### Screen: Open `src/advanced_features.py`

### Script:
> "Now let's look at feature engineering - this is where the ML magic happens.
>
> [Scroll to create_user_behavioral_features]
>
> I created over 40 features across multiple dimensions. Here's the user behavioral features function. It calculates user spending patterns, transaction frequency, and amount deviations from personal baselines.
>
> [Highlight key code]
>
> Notice this line - I'm calculating how much each transaction deviates from the user's average. This catches unusual spending patterns.
>
> [Scroll to create_velocity_features]
>
> The velocity features use rolling windows to detect burst activity. This rolling mean over the last 3 transactions helps identify sudden spikes in activity.
>
> [Scroll to composite features]
>
> A key feature I'm proud of is these composite risk scores. The velocity risk score combines burst detection, high-frequency sequences, unusual timing, and IP risk into a single meaningful metric. This is more powerful than individual features.
>
> [Show feature list]
>
> In total, I engineered 40+ features including behavioral, temporal, velocity, device sharing, and merchant relationship features."

### What to Show:
- `engineer_all_features()` main function
- Individual feature creation functions
- Rolling window calculations
- Composite risk score formulas
- Feature list at the end

### Key Code Features to Highlight:
```python
# Amount deviation from user baseline
df['amount_deviation'] = abs(df['amount'] - df['user_avg_amount']) / (df['user_avg_amount'] + 1)

# Rolling window velocity
df['rolling_amount_mean'] = df.groupby('user_id')['amount'].transform(
    lambda x: x.rolling(window=3, min_periods=1).mean()
)

# Composite risk score
df['velocity_risk_score'] = (
    df['is_burst'] * 0.3 + 
    df['high_velocity_seq'] * 0.3 + 
    df['is_night_transaction'] * 0.2 +
    df['high_ip_risk'] * 0.2
)
```

---

## SECTION 4: Model Pipeline Code (2:15 - 2:50)

### Screen: Open `src/features.py` and `src/train_model.py`

### Script:
> "Let me show you the model pipeline code.
>
> [Show build_pipeline function]
>
> I built a complete scikit-learn pipeline with preprocessing and the classifier. This is crucial for preventing data leakage and ensuring reproducibility.
>
> [Highlight preprocessor]
>
> The preprocessor handles categorical features with OneHotEncoding and numeric features with StandardScaling. The 'handle_unknown=ignore' parameter ensures the model can handle new categories in production.
>
> [Show model configuration]
>
> For the classifier, I chose RandomForest with 300 trees, max depth of 8, and balanced class weights to handle the imbalance. The class_weight='balanced' automatically adjusts for the 95-5 split between normal and fraud.
>
> [Open train_model.py]
>
> The training code is clean and modular. It loads processed data, fits the pipeline, generates metrics, and saves everything with joblib for deployment.
>
> [Highlight key feature]
>
> A key feature here is that I'm saving both the model and the metrics as JSON. This creates an audit trail for model governance and monitoring."

### What to Show:
- `build_pipeline()` function
- `build_preprocessor()` with ColumnTransformer
- `build_model()` with RandomForest configuration
- `train_and_evaluate()` function
- Model serialization with joblib

### Key Code Features to Highlight:
```python
# Pipeline prevents data leakage
pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('clf', model)
])

# Balanced class weights for imbalance
RandomForestClassifier(
    n_estimators=300,
    max_depth=8,
    class_weight='balanced',  # Handles 95-5 split
    n_jobs=-1,
    random_state=42
)

# Serialization for deployment
joblib.dump(pipeline, model_path)
```

---

## SECTION 5: Threshold Optimization Code (2:50 - 3:20)

### Screen: Open `src/evaluate.py`

### Script:
> "Now let's look at threshold optimization - this is critical for fraud detection.
>
> [Show compute_threshold_metrics function]
>
> I evaluate 19 different thresholds from 0.05 to 0.95. For each threshold, I calculate precision, recall, F1, and most importantly, business cost.
>
> [Highlight cost calculation]
>
> The cost function is simple but powerful: 10 times the false negatives plus 1 times the false positives. This reflects the business reality that missing fraud is 10 times more expensive than a false alarm.
>
> [Show pick_best_threshold]
>
> The best threshold is the one that minimizes this cost, not the one that maximizes accuracy. This is cost-sensitive machine learning in action.
>
> [Show results]
>
> The optimal threshold turns out to be 0.35, not the default 0.5. This saves significant business cost while maintaining high precision."

### What to Show:
- `compute_threshold_metrics()` function
- Cost calculation logic
- `pick_best_threshold()` function
- Threshold search results
- Visualization generation code

### Key Code Features to Highlight:
```python
# Cost-sensitive evaluation
cost = COST_FALSE_NEGATIVE * fn + COST_FALSE_POSITIVE * fp

# Find optimal threshold
best = min(results, key=lambda r: r['cost'])

# Business-driven decision making
COST_FALSE_NEGATIVE = 10.0  # Missing fraud is expensive
COST_FALSE_POSITIVE = 1.0   # False alarm is cheaper
```

---

## SECTION 6: Explainability Code (3:20 - 3:50)

### Screen: Open `src/explain.py` and `app.py`

### Script:
> "Explainability is essential for production fraud systems. Let me show you the SHAP implementation.
>
> [Show compute_and_plot_global_shap]
>
> I'm using SHAP's TreeExplainer for the RandomForest model. The code extracts the preprocessor and classifier from the pipeline, transforms the data, and computes SHAP values.
>
> [Highlight key handling]
>
> A key feature here is handling sparse matrices from OneHotEncoding. I convert them to dense arrays for SHAP, and handle both binary and multi-class cases.
>
> [Open app.py - show explain_single_transaction]
>
> For the Streamlit dashboard, I implemented per-transaction explanations. This function computes SHAP values for a single transaction and creates a bar plot showing which features contributed to the fraud prediction.
>
> [Highlight]
>
> This transparency is critical for fraud analysts to understand and trust the model's decisions."

### What to Show:
- `compute_and_plot_global_shap()` function
- TreeExplainer initialization
- Sparse matrix handling
- `explain_single_transaction()` in app.py
- SHAP value plotting code

### Key Code Features to Highlight:
```python
# Extract components from pipeline
preprocessor = model.named_steps["preprocess"]
clf = model.named_steps["clf"]

# Handle sparse matrices
if sp.issparse(X_transformed):
    X_for_shap = X_transformed.toarray()

# TreeExplainer for RandomForest
explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(X_for_shap)

# Handle binary classification
if isinstance(shap_values, list):
    shap_values_to_plot = shap_values[1]  # Fraud class
```

---

## SECTION 7: Live Demonstration (3:50 - 4:50)

### Screen: Terminal/Command Prompt

### Script:
> "Now let me demonstrate the system in action. I'll run the quick test script to show the complete workflow.
>
> [Type and run: python quick_test.py]
>
> Watch as it generates synthetic data with fraud patterns...
>
> [Wait for data generation]
>
> Now it's preparing the data with stratified train-test split...
>
> [Wait for data prep]
>
> Training the RandomForest model with the complete pipeline...
>
> [Wait for training]
>
> And making predictions on new transactions.
>
> [Show results]
>
> Perfect! The system generated 10,000 transactions, trained the model, and made predictions. We can see it flagged 88 transactions as fraud with high confidence.
>
> [Open Streamlit dashboard]
>
> Now let me show you the interactive dashboard.
>
> [Type: streamlit run app.py]
>
> [Wait for dashboard to load]
>
> Here's the dashboard. We can see the risk distribution - most transactions have low fraud probability, but there's a clear separation for fraud cases.
>
> [Adjust threshold slider]
>
> I can adjust the threshold dynamically. Watch how the flagged count changes.
>
> [Select a high-risk transaction]
>
> Let me select this high-risk transaction. The SHAP explanation shows exactly why it was flagged: high velocity risk score, unusual amount deviation, and shared device. This transparency is critical for fraud analysts.
>
> [Show top risky transactions table]
>
> The dashboard also shows the top risky transactions ranked by fraud probability, making it easy for analysts to prioritize their review."

### What to Show:
1. **Terminal Demo:**
   - Run `python quick_test.py`
   - Show each step executing
   - Display final results

2. **Dashboard Demo:**
   - Launch `streamlit run app.py`
   - Show overview metrics
   - Demonstrate threshold adjustment
   - Select and explain a transaction
   - Show SHAP values
   - Display top risky transactions

### Key Features to Demonstrate:
- ✅ Complete workflow execution
- ✅ Data generation with patterns
- ✅ Model training and evaluation
- ✅ Batch prediction capability
- ✅ Interactive dashboard
- ✅ Threshold adjustment
- ✅ Per-transaction explanations
- ✅ SHAP visualizations

---

## SECTION 8: Closing & Key Takeaways (4:50 - 5:00)

### Screen: Back to project structure or results

### Script:
> "To summarize the key features in my code:
>
> One - Five explicit fraud patterns with realistic parameters, not random labels.
>
> Two - Over 40 engineered features including composite risk scores.
>
> Three - Production-ready scikit-learn pipeline preventing data leakage.
>
> Four - Cost-sensitive threshold optimization minimizing business impact.
>
> Five - Complete SHAP explainability for transparency and trust.
>
> And six - Interactive dashboard for human-in-the-loop workflows.
>
> The system is fully functional, well-documented, and ready for production deployment. Thank you for watching!"

### What to Show:
- Project structure overview
- Key metrics summary
- Documentation files

---

## RECORDING SETUP

### Tools Needed:
1. **Screen Recording:**
   - OBS Studio (free, powerful)
   - Loom (easy, cloud-based)
   - Zoom (record screen share)
   - QuickTime (Mac)

2. **Code Editor:**
   - VS Code (recommended)
   - PyCharm
   - Sublime Text
   - Any IDE with good syntax highlighting

3. **Terminal:**
   - Clean terminal with clear font
   - Consider using iTerm2 (Mac) or Windows Terminal
   - Increase font size for readability

### Recording Settings:
- **Resolution:** 1920×1080 (Full HD)
- **Frame Rate:** 30 fps
- **Audio:** Clear microphone, 44.1 kHz
- **Format:** MP4 (most compatible)

### Screen Setup:
1. Close unnecessary applications
2. Clear desktop clutter
3. Increase IDE font size (14-16pt)
4. Increase terminal font size (14-16pt)
5. Use light theme for better visibility
6. Hide sensitive information

---

## PRE-RECORDING CHECKLIST

### Code Preparation:
- [ ] All code is clean and commented
- [ ] No syntax errors or warnings
- [ ] Test scripts run successfully
- [ ] Dashboard launches without errors
- [ ] All dependencies installed

### Environment Setup:
- [ ] Virtual environment activated
- [ ] All packages installed (`pip install -r requirements.txt`)
- [ ] Data generated (`python -m src.generate_data`)
- [ ] Model trained (`python -m src.train_model`)
- [ ] Dashboard tested (`streamlit run app.py`)

### Recording Setup:
- [ ] Screen recording software tested
- [ ] Microphone tested (clear audio)
- [ ] Font sizes increased
- [ ] Terminal cleared
- [ ] Browser tabs closed
- [ ] Notifications disabled

### Practice:
- [ ] Dry run of complete demo (3-5 times)
- [ ] Timing checked (4-5 minutes)
- [ ] Code sections bookmarked
- [ ] Demo script memorized
- [ ] Backup plan if something fails

---

## TIMING BREAKDOWN

| Section | Time | Focus |
|---------|------|-------|
| Introduction & Approach | 0:00-0:45 | Project overview, approach |
| Data Generation Code | 0:45-1:30 | Fraud patterns, key code |
| Feature Engineering | 1:30-2:15 | 40+ features, composites |
| Model Pipeline | 2:15-2:50 | Pipeline, training code |
| Threshold Optimization | 2:50-3:20 | Cost-sensitive approach |
| Explainability | 3:20-3:50 | SHAP implementation |
| Live Demo | 3:50-4:50 | Quick test + Dashboard |
| Closing | 4:50-5:00 | Key takeaways |

---

## CODE SECTIONS TO HIGHLIGHT

### Must Show:
1. ✅ Fraud pattern generation functions
2. ✅ Feature engineering functions
3. ✅ Pipeline construction
4. ✅ Cost calculation in threshold optimization
5. ✅ SHAP implementation
6. ✅ Live execution (quick_test.py)
7. ✅ Dashboard demonstration

### Nice to Show (if time):
- Temporal feature engineering
- Confusion matrix generation
- Batch scoring script
- Test suite

### Don't Show:
- ❌ Configuration files
- ❌ Requirements.txt
- ❌ Setup.py
- ❌ Long data loading code
- ❌ Debugging code

---

## NARRATION TIPS

### Do:
- ✅ Explain WHY you made design choices
- ✅ Highlight key features and innovations
- ✅ Show enthusiasm for your work
- ✅ Speak clearly and at moderate pace
- ✅ Pause briefly when switching screens
- ✅ Point out specific code lines
- ✅ Explain business value, not just technical details

### Don't:
- ❌ Read code line by line
- ❌ Apologize for code quality
- ❌ Get lost in minor details
- ❌ Rush through important sections
- ❌ Use too much jargon
- ❌ Forget to show the demo
- ❌ Go over 5 minutes

---

## BACKUP PLANS

### If Code Doesn't Run:
1. Have pre-recorded terminal output ready
2. Show screenshots of successful runs
3. Explain what should happen
4. Move to dashboard demo

### If Dashboard Doesn't Load:
1. Have screenshots of dashboard ready
2. Show static SHAP plots from reports/figures/
3. Explain functionality verbally
4. Show code instead

### If Time Runs Short:
1. Skip temporal features section
2. Shorten feature engineering explanation
3. Speed up live demo
4. Keep introduction and closing

### If Time Runs Long:
1. Cut threshold optimization details
2. Shorten feature engineering
3. Speed up narration
4. Skip nice-to-have sections

---

## UPLOAD & SHARING

### YouTube Upload:
1. **Title:** "Fraud Detection System - Code Walkthrough & Demo | [Your Name]"
2. **Description:** Include project overview, GitHub link, key features
3. **Visibility:** Unlisted (shareable link)
4. **Thumbnail:** Screenshot of dashboard or code
5. **Tags:** fraud detection, machine learning, python, scikit-learn

### Google Drive:
1. Upload MP4 file
2. Set sharing to "Anyone with the link"
3. Test link in incognito mode
4. Ensure video plays without download

### Video Description Template:
```
Fraud Detection System - Technical Assessment Demo

This video demonstrates my end-to-end fraud detection system including:
- Synthetic data generation with 5 explicit fraud patterns
- 40+ engineered features for behavioral analysis
- Production-ready scikit-learn pipeline
- Cost-sensitive threshold optimization
- SHAP explainability implementation
- Interactive Streamlit dashboard

Key Features:
✅ Realistic fraud patterns (not random)
✅ Sophisticated feature engineering
✅ Cost-sensitive optimization
✅ Complete explainability
✅ Production-ready architecture

GitHub: [Your Repository Link]
Contact: [Your Email]

Timestamps:
0:00 - Introduction & Approach
0:45 - Data Generation Code
1:30 - Feature Engineering
2:15 - Model Pipeline
2:50 - Threshold Optimization
3:20 - Explainability
3:50 - Live Demonstration
4:50 - Closing
```

---

## FINAL QUALITY CHECK

### Before Uploading:
- [ ] Video is 4-5 minutes long
- [ ] Audio is clear and audible
- [ ] Code is readable (font size)
- [ ] Demo runs successfully
- [ ] All key features explained
- [ ] Professional presentation
- [ ] No sensitive information visible
- [ ] Video plays smoothly
- [ ] Link is accessible

### Test Your Video:
1. Watch the entire video
2. Check audio quality
3. Verify code readability
4. Ensure demo is clear
5. Confirm timing
6. Test sharing link

---

## SUCCESS CRITERIA

Your video should demonstrate:
1. ✅ **Code clarity** - Clean, well-structured code
2. ✅ **Technical depth** - Understanding of ML concepts
3. ✅ **Communication** - Clear explanation of approach
4. ✅ **Key features** - Highlighting innovations
5. ✅ **Live demo** - Working system demonstration
6. ✅ **Professional delivery** - Confident presentation

**You've got this! Show them what you've built!** 🚀
