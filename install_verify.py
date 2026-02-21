"""
Installation and Verification Script

This script installs dependencies and verifies the environment for the fraud detection system.
"""

import subprocess
import sys
import importlib
from pathlib import Path

def install_requirements():
    """Install packages from requirements.txt."""
    print("📦 Installing packages from requirements.txt...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def verify_package_installation():
    """Verify that all required packages can be imported."""
    print("\n🔍 Verifying package installations...")
    
    packages_to_check = [
        ("pandas", "pd"),
        ("numpy", "np"),
        ("sklearn", "sk"),
        ("matplotlib.pyplot", "plt"),
        ("seaborn", "sns"),
        ("joblib", "joblib"),
        ("shap", "shap"),
        ("streamlit", "st")
    ]
    
    all_installed = True
    for full_module, alias in packages_to_check:
        try:
            importlib.import_module(full_module)
            print(f"✓ {full_module} is available")
        except ImportError as e:
            print(f"❌ {full_module} is NOT available: {e}")
            all_installed = False
    
    return all_installed

def create_test_script():
    """Create a simple test script to verify functionality."""
    test_code = '''
import sys
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))

def test_basic_functionality():
    """Test basic functionality without complex imports."""
    print("Testing basic imports...")
    
    # Test pandas and numpy
    import pandas as pd
    import numpy as np
    print("✓ Pandas and NumPy working")
    
    # Test scikit-learn
    from sklearn.ensemble import RandomForestClassifier
    print("✓ Scikit-learn working")
    
    # Test matplotlib
    import matplotlib.pyplot as plt
    print("✓ Matplotlib working")
    
    # Test joblib
    import joblib
    print("✓ Joblib working")
    
    print("\\n🎉 Basic functionality verified!")
    return True

if __name__ == "__main__":
    test_basic_functionality()
'''
    
    with open("verify_installation.py", "w") as f:
        f.write(test_code)
    
    print("✓ Created verification script: verify_installation.py")

def run_verification():
    """Run the verification script."""
    print("\n🧪 Running verification test...")
    
    try:
        import pandas as pd
        import numpy as np
        import sklearn
        import matplotlib.pyplot as plt
        import joblib
        import shap
        import streamlit as st
        
        print("✓ All major packages can be imported")
        
        # Test basic functionality
        df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        arr = np.array([1, 2, 3])
        rf = sklearn.ensemble.RandomForestClassifier(n_estimators=2)  # Small for test
        
        print("✓ Basic functionality working")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        return False

def main():
    """Main installation and verification function."""
    print("🚀 FRAUD DETECTION SYSTEM - INSTALLATION VERIFICATION")
    print("=" * 60)
    
    # Install requirements
    if not install_requirements():
        print("\n❌ Requirements installation failed!")
        print("Try installing manually: pip install -r requirements.txt")
        return False
    
    # Verify packages
    print("\n" + "=" * 60)
    if not verify_package_installation():
        print("\n❌ Package verification failed!")
        return False
    
    # Run verification
    print("\n" + "=" * 60)
    if not run_verification():
        print("\n❌ Verification test failed!")
        return False
    
    # Create test script
    create_test_script()
    
    print("\n" + "=" * 60)
    print("🎉 INSTALLATION AND VERIFICATION SUCCESSFUL!")
    print("\nNext steps:")
    print("1. Run: python verify_installation.py (to confirm basic functionality)")
    print("2. Run: python quick_test.py (for quick functionality test)")
    print("3. Run: python test_system.py (for complete system test)")
    
    return True

if __name__ == "__main__":
    main()