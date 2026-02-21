# Slide-by-Slide Visual Guide for 5-Minute Video

## Slide Design Principles
- **Clean and professional** - White/light background with dark text
- **Consistent branding** - Use same color scheme throughout
- **Visual hierarchy** - Important numbers/text larger
- **Minimal text** - Bullet points, not paragraphs
- **High-quality graphics** - Professional diagrams and charts

---

## SLIDE 1: Title Slide

### Layout:
```
┌─────────────────────────────────────────┐
│                                         │
│    End-to-End Fraud Detection System   │
│                                         │
│    Technical Assessment Presentation    │
│                                         │
│              [Your Name]                │
│                                         │
│    [Date] | [Institution/Company]      │
│                                         │
└─────────────────────────────────────────┘
```

### Design Elements:
- Large, bold title font
- Subtitle in lighter weight
- Professional background (gradient or subtle pattern)
- Optional: Small fraud detection icon/graphic
- Your name prominently displayed

### Color Scheme Suggestion:
- Primary: Navy blue (#1e3a8a)
- Secondary: Teal (#0d9488)
- Accent: Orange (#f97316) for highlights
- Background: White or light gray (#f8fafc)

---

## SLIDE 2: Problem Statement & Approach

### Layout:
```
┌──────────────────┬──────────────────────┐
│   THE PROBLEM    │   OUR SOLUTION       │
│                  │                      │
│ • Fraud <5%      │  [Pipeline Diagram]  │
│ • Imbalanced     │                      │
│ • High cost      │  Data → Features →   │
│ • Adversarial    │  Model → Threshold   │
│                  │                      │
│ Business Impact: │  Cost-Sensitive      │
│ FN cost = 10×FP  │  Explainable AI      │
└──────────────────┴──────────────────────┘
```

### Key Visuals:
- Left: Problem statistics with icons
- Right: Simple pipeline flowchart
- Use arrows to show flow
- Highlight "Cost-Sensitive" in accent color

### Text Content:
**Left Side:**
- Fraud rate: <5% (highly imbalanced)
- Cost: Missing fraud = 10-100× false alarm
- Challenge: Adversarial, evolving patterns
- Impact: $billions lost annually

**Right Side:**
- Synthetic Data Generation
- Feature Engineering (40+ features)
- Model Training (RandomForest)
- Threshold Optimization
- Explainability (SHAP)

---

## SLIDE 3: Synthetic Data Generation

### Layout:
```
┌─────────────────────────────────────────┐
│  5 EXPLICIT FRAUD PATTERNS              │
│                                         │
│  [Icon] Velocity Attacks        30%    │
│  [Icon] Amount Spikes           25%    │
│  [Icon] Location Inconsistency  20%    │
│  [Icon] Shared Device Abuse     15%    │
│  [Icon] Merchant Rings          10%    │
│                                         │
│  📊 Dataset: 10,000 transactions        │
│     • 1,000 users • 500 merchants       │
│     • 5% fraud rate • 90-day period     │
└─────────────────────────────────────────┘
```

### Key Visuals:
- 5 icons representing each pattern (use emojis or simple graphics)
- Percentage bars showing distribution
- Data statistics box at bottom
- Use different colors for each pattern

### Icon Suggestions:
- ⚡ Velocity Attacks (lightning bolt)
- 💰 Amount Spikes (money bag)
- 🌍 Location Inconsistency (globe)
- 📱 Shared Device (phone)
- 🔗 Merchant Rings (chain links)

---

## SLIDE 4: Feature Engineering

### Layout:
```
┌──────────────────────────────────────────┐
│     40+ ENGINEERED FEATURES              │
│                                          │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │BEHAVIORAL│ │ TEMPORAL │ │RELATIONAL│ │
│ │          │ │          │ │          │ │
│ │• Velocity│ │• Sessions│ │• Device  │ │
│ │• Amount  │ │• Bursts  │ │  sharing │ │
│ │  patterns│ │• Time of │ │• Merchant│ │
│ │• User    │ │  day     │ │  networks│ │
│ │  baseline│ │• Cyclical│ │• Cross-  │ │
│ │          │ │  features│ │  entity  │ │
│ └──────────┘ └──────────┘ └──────────┘ │
│                                          │
│  Example: velocity_risk_score =          │
│    burst_detection + high_frequency +    │
│    unusual_timing + high_ip_risk         │
└──────────────────────────────────────────┘
```

### Key Visuals:
- Three columns with distinct colors
- Icons for each category
- Example formula at bottom
- Use boxes/cards for visual separation

### Design Tips:
- Make "40+" large and prominent
- Use icons: 👤 (behavioral), ⏰ (temporal), 🔗 (relational)
- Highlight the composite feature example

---

## SLIDE 5: Model Architecture & Performance

### Layout:
```
┌──────────────────┬──────────────────────┐
│  ARCHITECTURE    │   PERFORMANCE        │
│                  │                      │
│  [Pipeline]      │  ROC-AUC:   0.9067  │
│  OneHot →        │  Precision: 89.77%  │
│  Scaler →        │  Recall:    79.00%  │
│  RandomForest    │  F1-Score:  84.04%  │
│  (300 trees)     │                      │
│                  │  [Confusion Matrix]  │
│  Balanced        │     Pred             │
│  Class Weights   │   F    N             │
│                  │ F 79   21            │
│                  │ N  9  1891           │
└──────────────────┴──────────────────────┘
```

### Key Visuals:
- Left: Simple pipeline diagram with arrows
- Right: Large metrics with color coding
  - Green for good metrics (>80%)
  - Orange for moderate (70-80%)
- Confusion matrix as heatmap
- Use large, bold numbers

### Color Coding:
- True Positives: Dark green
- True Negatives: Light green
- False Positives: Light orange
- False Negatives: Dark orange

---

## SLIDE 6: Threshold Optimization

### Layout:
```
┌─────────────────────────────────────────┐
│   COST-SENSITIVE THRESHOLD OPTIMIZATION │
│                                         │
│   [Graph: Cost vs Threshold]            │
│   │                                     │
│   │     ╱╲                              │
│   │    ╱  ╲                             │
│   │   ╱    ╲___                         │
│   │  ╱         ╲___                     │
│   │ ╱              ╲___                 │
│   └─────────────────────────            │
│     0.0  0.35  0.5  0.75  1.0           │
│          ↑                              │
│       Optimal                           │
│                                         │
│   Cost Function: 10×FN + 1×FP           │
│   Optimal Threshold: 0.35               │
│   Minimum Cost: 219                     │
└─────────────────────────────────────────┘
```

### Key Visuals:
- Line graph showing cost curve
- Vertical line at optimal point (0.35)
- Annotate the optimal point
- Show cost function prominently
- Use accent color for optimal threshold

### Alternative: Table Format
```
Threshold | Precision | Recall | Cost
   0.25   |   66.9%   |  79%   | 249
   0.35   |   89.8%   |  79%   | 219 ← Optimal
   0.50   |   89.8%   |  79%   | 219
   0.95   |   93.9%   |  31%   | 692
```

---

## SLIDE 7: Explainability & Dashboard

### Layout:
```
┌──────────────────┬──────────────────────┐
│  SHAP VALUES     │  INTERACTIVE         │
│                  │  DASHBOARD           │
│  [SHAP Plot]     │                      │
│  Feature         │  [Dashboard          │
│  Importance:     │   Screenshot]        │
│                  │                      │
│  • velocity_risk │  • Upload data       │
│  • amount_dev    │  • Adjust threshold  │
│  • device_shared │  • View explanations │
│  • unusual_merch │  • Export results    │
│                  │                      │
│  Transparency    │  Human-in-the-Loop   │
│  for Compliance  │  Workflow Support    │
└──────────────────┴──────────────────────┘
```

### Key Visuals:
- Left: SHAP summary plot (screenshot from reports/figures/)
- Right: Streamlit dashboard screenshot
- Arrows pointing to key features
- Highlight "Explainability" and "Transparency"

### Design Tips:
- Use actual screenshots from your project
- Add annotations/callouts to highlight features
- Show a real transaction explanation

---

## SLIDE 8: System Architecture

### Layout:
```
┌─────────────────────────────────────────┐
│   PRODUCTION-READY ARCHITECTURE         │
│                                         │
│   ┌─────────────┐                       │
│   │ Raw Data    │                       │
│   └──────┬──────┘                       │
│          ↓                              │
│   ┌─────────────┐    ┌──────────────┐  │
│   │ Batch       │    │ Real-Time    │  │
│   │ Processing  │    │ API          │  │
│   └──────┬──────┘    └──────┬───────┘  │
│          ↓                   ↓          │
│   ┌─────────────────────────────────┐  │
│   │   Fraud Detection Pipeline      │  │
│   │   (Preprocessing → Model)       │  │
│   └──────┬──────────────────────────┘  │
│          ↓                              │
│   ┌─────────────┐    ┌──────────────┐  │
│   │ Threshold   │    │ Explainability│ │
│   │ Application │    │ (SHAP)       │  │
│   └──────┬──────┘    └──────┬───────┘  │
│          ↓                   ↓          │
│   ┌─────────────────────────────────┐  │
│   │   Analyst Dashboard             │  │
│   │   (Human Review)                │  │
│   └─────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### Key Visuals:
- Flowchart with boxes and arrows
- Two paths: Batch and Real-time
- Highlight human-in-the-loop
- Use different colors for different components

### Components to Show:
- Data ingestion
- Preprocessing pipeline
- Model inference
- Threshold application
- Explainability layer
- Human review interface
- Monitoring & logging

---

## SLIDE 9: Key Achievements

### Layout:
```
┌─────────────────────────────────────────┐
│   ✅ KEY ACHIEVEMENTS                    │
│                                         │
│   ✅ All 7 Assessment Requirements      │
│   ✅ 5 Explicit Fraud Patterns          │
│   ✅ 40+ Engineered Features            │
│   ✅ Cost-Sensitive Optimization        │
│   ✅ SHAP Explainability                │
│   ✅ Interactive Dashboard              │
│   ✅ Production-Ready Pipeline          │
│   ✅ Comprehensive Testing (8/8)        │
│                                         │
│   📊 RESULTS:                            │
│   • ROC-AUC: 0.9067                     │
│   • 79% Recall, 90% Precision           │
│   • 0.47% False Positive Rate           │
└─────────────────────────────────────────┘
```

### Key Visuals:
- Large checkmarks (✅) in green
- Two sections: Achievements and Results
- Use bold text for numbers
- Keep it clean and scannable

### Design Tips:
- Use green checkmarks consistently
- Make numbers large and prominent
- Group related items
- Leave white space for readability

---

## SLIDE 10: Results & Future Work

### Layout:
```
┌──────────────────┬──────────────────────┐
│  RESULTS         │  FUTURE ENHANCEMENTS │
│                  │                      │
│  ✅ Production-  │  🚀 Graph-based      │
│     grade        │     fraud detection  │
│     performance  │                      │
│                  │  🚀 LSTM for         │
│  ✅ Realistic    │     sequences        │
│     complexity   │                      │
│                  │  🚀 Real-time        │
│  ✅ Fully        │     streaming        │
│     documented   │                      │
│                  │  🚀 Auto-retraining  │
│  ✅ Ready for    │     pipeline         │
│     deployment   │                      │
│                  │                      │
│  THANK YOU!      │  Questions?          │
└──────────────────┴──────────────────────┘
```

### Key Visuals:
- Left: Summary with checkmarks
- Right: Future roadmap with rocket emojis
- Large "THANK YOU" at bottom
- Contact information

### Contact Info to Include:
- Email
- GitHub repository link
- LinkedIn (optional)
- Portfolio website (optional)

---

## BONUS: Demo Slide (Optional)

### Layout:
```
┌─────────────────────────────────────────┐
│   LIVE DEMO                             │
│                                         │
│   [Screen recording or live demo]       │
│                                         │
│   Showing:                              │
│   • Quick test execution                │
│   • Dashboard interaction               │
│   • Transaction explanation             │
│                                         │
│   Time: 30 seconds                      │
└─────────────────────────────────────────┘
```

---

## VISUAL ASSETS NEEDED

### From Your Project:
1. ✅ SHAP summary plot: `reports/figures/shap_summary.png`
2. ✅ ROC curve: `reports/figures/roc_curve.png`
3. ✅ PR curve: `reports/figures/pr_curve.png`
4. ✅ Confusion matrix: `reports/figures/confusion_matrix.png`
5. ✅ Dashboard screenshot: Take from running `streamlit run app.py`

### To Create:
1. Pipeline diagram (use draw.io, Lucidchart, or PowerPoint)
2. Fraud pattern icons (use emojis or icon libraries)
3. Architecture diagram (flowchart)
4. Cost vs threshold graph (from threshold_search.json data)
5. Feature engineering visualization

---

## DESIGN TOOLS RECOMMENDATIONS

### Presentation Software:
- **PowerPoint** - Most common, easy to use
- **Google Slides** - Cloud-based, easy sharing
- **Keynote** - Mac users, beautiful animations
- **Canva** - Modern templates, easy design

### Diagram Tools:
- **draw.io** - Free, powerful
- **Lucidchart** - Professional diagrams
- **Miro** - Collaborative whiteboard
- **PowerPoint SmartArt** - Built-in diagrams

### Icon Resources:
- **Font Awesome** - Free icons
- **Flaticon** - Large icon library
- **Emojis** - Quick and universal
- **Material Icons** - Google's icon set

---

## ANIMATION SUGGESTIONS

### Slide Transitions:
- Use **Fade** or **Push** (professional, not distracting)
- Avoid flashy transitions (wipes, spins, etc.)
- Keep consistent throughout

### Element Animations:
- **Appear** for bullet points (one at a time)
- **Fade in** for images
- **Grow** for important numbers
- Timing: 0.3-0.5 seconds per animation

### When to Animate:
- ✅ Bullet points appearing sequentially
- ✅ Highlighting key metrics
- ✅ Showing pipeline flow
- ❌ Don't animate every element
- ❌ Don't use sound effects

---

## RECORDING TIPS

### Screen Recording:
- **OBS Studio** (free, powerful)
- **Loom** (easy, cloud-based)
- **Zoom** (record yourself presenting)
- **PowerPoint** (built-in recording)

### Video Settings:
- Resolution: 1920×1080 (Full HD)
- Frame rate: 30 fps
- Format: MP4 (most compatible)
- Audio: 44.1 kHz, clear microphone

### Recording Setup:
1. Close unnecessary applications
2. Clear desktop/browser tabs
3. Test audio levels
4. Do a practice recording
5. Have water nearby
6. Record in quiet environment

---

## FINAL CHECKLIST

### Before Creating Slides:
- [ ] Gather all visual assets
- [ ] Take dashboard screenshots
- [ ] Create diagrams
- [ ] Choose color scheme
- [ ] Select fonts (max 2 fonts)

### While Creating Slides:
- [ ] Consistent design across all slides
- [ ] Large, readable text (min 24pt)
- [ ] High contrast (dark text on light background)
- [ ] Minimal text per slide
- [ ] Professional graphics

### Before Recording:
- [ ] Practice presentation 3-5 times
- [ ] Time yourself (4:30-5:00 target)
- [ ] Test recording setup
- [ ] Prepare demo (if including)
- [ ] Have notes ready (but don't read)

### After Recording:
- [ ] Watch full video
- [ ] Check audio quality
- [ ] Verify timing (under 5 minutes)
- [ ] Add captions (optional but helpful)
- [ ] Export in correct format

---

## SUCCESS METRICS

Your slides should:
1. ✅ Be readable from 6 feet away
2. ✅ Have consistent branding
3. ✅ Support your narrative (not replace it)
4. ✅ Include actual project visuals
5. ✅ Look professional and polished

**Remember:** Slides support your presentation, they don't replace it. Keep them clean, visual, and focused on key points. Your verbal explanation provides the depth!

Good luck! 🎯
