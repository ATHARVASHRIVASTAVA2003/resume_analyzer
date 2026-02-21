"""
Quick Functional Test Script

Tests the core functionality in under 2 minutes.
"""

import pandas as pd
import sys
from pathlib import Path

# Add project root and src to path
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(src_path))

def quick_test():
    print("⚡ QUICK FUNCTIONAL TEST")
    print("=" * 40)
    
    # Test 1: Data Generation
    print("1. Testing data generation...")
    try:
        from generate_data import main as generate_main
        generate_main()
        df = pd.read_csv(project_root / "data" / "raw" / "synthetic_fraud_dataset.csv")
        print(f"   ✓ Generated {len(df)} transactions")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False
    
    # Test 2: Data Preparation
    print("2. Testing data preparation...")
    try:
        from data_prep import main as prep_main
        prep_main()
        train_df = pd.read_csv(project_root / "data" / "processed" / "transactions_train.csv")
        print(f"   ✓ Prepared {len(train_df)} training samples")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False
    
    # Test 3: Model Training
    print("3. Testing model training...")
    try:
        from train_model import main as train_main
        train_main()
        model_path = project_root / "models" / "fraud_pipeline.joblib"
        print(f"   ✓ Model saved ({model_path.stat().st_size//1024} KB)")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False
    
    # Test 4: Simple Prediction
    print("4. Testing prediction...")
    try:
        from score_new_transactions import score_file
        test_path = project_root / "data" / "processed" / "transactions_test.csv"
        output_path = project_root / "quick_test_output.csv"
        score_file(test_path, output_path)
        predictions = pd.read_csv(output_path)
        fraud_count = predictions['fraud_flag'].sum()
        print(f"   ✓ Made {len(predictions)} predictions ({fraud_count} fraud flags)")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False
    
    print("\n🎉 QUICK TEST PASSED!")
    print("System is functional and ready for use.")
    return True

if __name__ == "__main__":
    quick_test()