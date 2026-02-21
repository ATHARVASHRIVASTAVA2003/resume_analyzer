"""
Setup and Installation Script

This script helps install dependencies and set up the environment for the fraud detection system.
"""

import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install required Python packages."""
    print("📦 Installing required dependencies...")
    
    required_packages = [
        "pandas",
        "numpy", 
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "joblib",
        "shap",
        "streamlit"
    ]
    
    for package in required_packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False
    
    return True

def check_environment():
    """Check if all required packages are available."""
    print("\n🔍 Checking environment...")
    
    required_packages = [
        ("pandas", "pd"),
        ("numpy", "np"),
        ("sklearn", "sk"),
        ("matplotlib", "plt"),
        ("seaborn", "sns"),
        ("joblib", "joblib"),
        ("shap", "shap"),
        ("streamlit", "st")
    ]
    
    all_good = True
    for package, import_name in required_packages:
        try:
            # Try importing using the actual import mechanism
            if package == "sklearn":
                import sklearn
            elif package == "matplotlib":
                import matplotlib.pyplot as plt
            elif package == "seaborn":
                import seaborn as sns
            else:
                __import__(import_name)
            print(f"✓ {package} is available")
        except ImportError:
            print(f"❌ {package} is not available")
            all_good = False
    
    return all_good

def setup_directories():
    """Create necessary directories."""
    print("\n📁 Setting up directories...")
    
    project_root = Path(__file__).parent
    directories = [
        project_root / "data" / "raw",
        project_root / "data" / "processed",
        project_root / "models",
        project_root / "reports" / "metrics",
        project_root / "reports" / "figures",
        project_root / "docs"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created {directory}")

def run_quick_test():
    """Run a quick test to verify everything works."""
    print("\n🧪 Running quick functionality test...")
    
    try:
        # Test data generation
        from src.generate_data import main as generate_main
        print("✓ Data generation module loaded")
        
        # Test feature engineering
        from src.advanced_features import engineer_all_features
        print("✓ Feature engineering module loaded")
        
        # Test temporal features
        from src.temporal_features import engineer_temporal_user_features
        print("✓ Temporal features module loaded")
        
        print("🎉 All modules loaded successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    """Main setup function."""
    print("🚀 FRAUD DETECTION SYSTEM SETUP")
    print("=" * 50)
    
    # Setup directories
    setup_directories()
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Dependency installation failed!")
        return False
    
    # Check environment
    if not check_environment():
        print("\n❌ Environment check failed!")
        return False
    
    # Run quick test
    if not run_quick_test():
        print("\n❌ Quick test failed!")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 SETUP COMPLETE!")
    print("\nYou can now run:")
    print("  python quick_test.py     # Quick functionality test")
    print("  python test_system.py    # Complete system test")
    print("  streamlit run app.py     # Launch dashboard")
    
    return True

if __name__ == "__main__":
    main()