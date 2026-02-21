from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

try:
    from .config import CATEGORICAL_FEATURES, NUMERIC_FEATURES, RANDOM_STATE
except ImportError:
    # Fallback for direct execution
    from pathlib import Path
    import sys
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(PROJECT_ROOT / "src"))
    # Import config values manually
    import config
    CATEGORICAL_FEATURES = config.CATEGORICAL_FEATURES
    NUMERIC_FEATURES = config.NUMERIC_FEATURES
    RANDOM_STATE = config.RANDOM_STATE


def build_preprocessor() -> ColumnTransformer:
    """Create a ColumnTransformer for numeric + categorical features."""
    preprocessor = ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
            ("numeric", StandardScaler(), NUMERIC_FEATURES),
        ],
        remainder="drop",
    )
    return preprocessor


def build_model() -> RandomForestClassifier:
    """
    Build a fraud classifier.

    RandomForest with class_weight='balanced' to handle imbalanced data.
    """
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=8,
        class_weight="balanced",
        n_jobs=-1,
        random_state=RANDOM_STATE,
    )
    return model


def build_pipeline() -> Pipeline:
    """Full sklearn pipeline: preprocessing -> classifier."""
    preprocessor = build_preprocessor()
    model = build_model()

    pipeline = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("clf", model),
        ]
    )
    return pipeline
