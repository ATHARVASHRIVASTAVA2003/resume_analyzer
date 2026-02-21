"""
Advanced Feature Engineering for Fraud Detection

This module creates sophisticated behavioral and temporal features that help
distinguish fraudulent transactions from legitimate ones.

Features include:
- User behavioral patterns (spending velocity, amount patterns)
- Temporal features (time-based anomalies)
- Device and IP consistency patterns
- Merchant relationship features
- Velocity-based features (transactions per time window)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

def create_user_behavioral_features(df):
    """
    Create user-level behavioral features.
    
    Features include:
    - Average transaction amount for user
    - Transaction frequency (transactions per day)
    - Amount variance for user
    - Recent transaction velocity
    - Unusual amount deviation
    """
    print("Creating user behavioral features...")
    
    # User spending patterns
    user_stats = df.groupby('user_id').agg({
        'amount': ['mean', 'std', 'count']
    }).reset_index()
    
    user_stats.columns = [
        'user_id', 'user_avg_amount', 'user_amount_std', 
        'user_transaction_count'
    ]
    
    # Merge back to original dataframe
    df = df.merge(user_stats, on='user_id', how='left')
    
    # Calculate user transaction frequency (per day)
    df['user_frequency'] = df['user_transaction_count'] / 90  # 90-day period
    
    # Calculate amount deviation from user average
    df['amount_deviation'] = abs(df['amount'] - df['user_avg_amount']) / (df['user_avg_amount'] + 1)
    
    # Recent activity indicators
    df = df.sort_values(['user_id', 'transaction_id'])
    df['prev_amount'] = df.groupby('user_id')['amount'].shift(1)
    df['amount_change_ratio'] = abs(df['amount'] - df['prev_amount']) / (df['prev_amount'] + 1)
    df['amount_change_ratio'] = df['amount_change_ratio'].fillna(0)
    
    # For new data structure without 'hour', we'll skip the time-related features
    # Instead, we'll use other available features
    df['user_hour_std'] = 0  # Placeholder for compatibility
    df['hour_diff'] = 0     # Placeholder for compatibility
    
    return df

def create_velocity_features(df):
    """
    Create velocity-based features for fraud detection.
    
    Features include:
    - Transactions per time unit for user
    - Recent burst activity
    - Sequential transaction patterns
    """
    print("Creating velocity features...")
    
    # Sort by user and transaction_id
    df = df.sort_values(['user_id', 'transaction_id'])
    
    # Rolling window features (last 3 transactions)
    df['rolling_amount_mean'] = df.groupby('user_id')['amount'].transform(
        lambda x: x.rolling(window=3, min_periods=1).mean()
    )
    df['rolling_amount_std'] = df.groupby('user_id')['amount'].transform(
        lambda x: x.rolling(window=3, min_periods=1).std()
    ).fillna(0)
    
    # Velocity features (transactions in sequence windows)
    # Since we don't have 'hour', we'll use transaction sequence instead
    df['user_seq_velocity'] = df.groupby('user_id')['transaction_id'].transform('count')
    
    # Since we don't have hour data, we'll create a simple burst detection
    # based on transaction sequence within user
    df['user_transaction_rank'] = df.groupby('user_id')['transaction_id'].rank(method='dense')
    df['user_recent_velocity'] = df.groupby('user_id')['user_transaction_rank'].transform(
        lambda x: x.rolling(window=10, min_periods=1).count()
    )
    
    # Burst detection features
    df['is_burst'] = (df['user_recent_velocity'] > 5).astype(int)
    df['high_velocity_seq'] = (df['user_seq_velocity'] > 3).astype(int)
    
    return df

def create_temporal_features(df):
    """
    Create time-based anomaly detection features.
    
    Features include:
    - Transaction sequence patterns
    - Sequential timing anomalies
    - Transaction order features
    """
    print("Creating temporal features...")
    
    # Since we don't have 'hour' column, we'll create sequence-based features
    # Night hours (22-6) are higher risk - placeholder since no hour data
    df['is_night_transaction'] = 0  # Placeholder for compatibility
    
    # Weekend flag - placeholder since no day data
    df['potential_weekend'] = 0  # Placeholder for compatibility
    
    # Unusual timing patterns - based on transaction sequence instead
    # Users typically have preferred patterns
    user_seq_preference = df.groupby(['user_id', 'transaction_id']).size().reset_index(name='seq_count')
    user_seq_preference['seq_preference'] = user_seq_preference.groupby('user_id')['seq_count'].transform(
        lambda x: x / x.sum()
    )
    
    # Merge preference back
    df = df.merge(
        user_seq_preference[['user_id', 'transaction_id', 'seq_preference']], 
        on=['user_id', 'transaction_id'], 
        how='left'
    )
    df['unusual_hour'] = (df['seq_preference'].fillna(0) < 0.05).astype(int)  # Less than 5% preference
    
    # Time sequence features (using transaction_id as sequence)
    df['is_first_transaction'] = df.groupby('user_id').cumcount() == 0
    df['transaction_sequence'] = df.groupby('user_id').cumcount() + 1
    
    return df

def create_device_ip_features(df):
    """
    Create device and IP consistency features.
    
    Features include:
    - Device usage consistency per user
    - Risk score aggregation
    - Shared device detection
    """
    print("Creating device/IP features...")
    
    # Device consistency per user
    # Since we don't have device_risk_score in the new data, we'll use device_id instead
    # Count how many times each user uses each device
    device_user_counts = df.groupby(['user_id', 'device_id']).size().reset_index(name='device_usage_count')
    user_device_stats = device_user_counts.groupby('user_id').agg({
        'device_usage_count': ['mean', 'max']
    }).reset_index()
    
    user_device_stats.columns = [
        'user_id', 'avg_device_usage', 'max_device_usage'
    ]
    
    df = df.merge(user_device_stats, on='user_id', how='left')
    
    # Multiple devices per user (potential fraud indicator)
    df['multiple_devices'] = (df['avg_device_usage'] > 1.5).astype(int)
    
    # Since we don't have ip_risk_score in new data, we'll create a placeholder
    df['high_ip_risk'] = 0  # Placeholder for compatibility
    df['high_device_risk'] = 0  # Placeholder for compatibility
    df['avg_user_device_risk'] = 0  # Placeholder for compatibility
    
    # Combined risk score - placeholder
    df['combined_risk_score'] = 0  # Placeholder for compatibility
    df['high_combined_risk'] = 0  # Placeholder for compatibility
    
    return df

def create_merchant_features(df):
    """
    Create merchant relationship features.
    
    Features include:
    - Merchant risk history
    - Unusual merchant for user
    - Category risk scores
    - Cross-merchant patterns
    """
    print("Creating merchant features...")
    
    # Merchant risk scores based on historical fraud rates
    merchant_stats = df.groupby('merchant_id').agg({
        'is_fraud': 'mean',
        'amount': 'mean'
    }).reset_index()
    merchant_stats.columns = ['merchant_id', 'merchant_fraud_rate', 'avg_merchant_amount']
    
    df = df.merge(merchant_stats, on='merchant_id', how='left')
    
    # Location risk features (using 'location' instead of 'country')
    location_stats = df.groupby('location').agg({
        'is_fraud': 'mean'
    }).reset_index()
    location_stats.columns = ['location', 'country_fraud_rate']
    
    df = df.merge(location_stats, on='location', how='left')
    
    # Since we don't have device_risk_score, we'll use a placeholder
    df['country_avg_device_risk'] = 0  # Placeholder for compatibility
    
    # Unusual merchant for user (based on user history)
    user_merchant_patterns = df.groupby(['user_id', 'merchant_id']).size().reset_index(name='user_merchant_count')
    total_user_transactions = df.groupby('user_id').size().reset_index(name='total_user_transactions')
    
    user_merchant_patterns = user_merchant_patterns.merge(total_user_transactions, on='user_id')
    user_merchant_patterns['merchant_preference'] = (
        user_merchant_patterns['user_merchant_count'] / user_merchant_patterns['total_user_transactions']
    )
    
    # Merge back user-merchant preferences
    df = df.merge(
        user_merchant_patterns[['user_id', 'merchant_id', 'merchant_preference']], 
        on=['user_id', 'merchant_id'], 
        how='left'
    )
    
    df['unusual_merchant'] = (df['merchant_preference'].fillna(0) < 0.1).astype(int)
    # Since we don't have category information in merchant_id, we'll create a simple high risk indicator
    df['high_risk_category'] = (df['merchant_fraud_rate'].fillna(0) > 0.3).astype(int)
    
    return df

def create_derived_features(df):
    """
    Create mathematical transformations and interaction features.
    """
    print("Creating derived features...")
    
    # Amount-based features
    df['amount_log'] = np.log1p(df['amount'])  # Log transform for normalization
    df['amount_squared'] = df['amount'] ** 2
    df['amount_bin'] = pd.cut(df['amount'], bins=10, labels=False)
    
    # Time-based cyclical features - since we don't have hour, we'll create placeholders
    df['hour_sin'] = 0  # Placeholder for compatibility
    df['hour_cos'] = 0  # Placeholder for compatibility
    
    # Composite risk scores - adjust for new column names
    df['velocity_risk_score'] = (
        df['is_burst'] * 0.3 + 
        df['high_velocity_seq'] * 0.3 + 
        df['is_night_transaction'] * 0.2 +
        df['high_ip_risk'] * 0.2
    )
    
    # Behavioral anomaly scores
    df['behavioral_anomaly_score'] = (
        df['amount_deviation'] * 0.4 + 
        df['unusual_hour'] * 0.3 + 
        df['multiple_devices'] * 0.2 +
        df['unusual_merchant'] * 0.1
    )
    
    # Normalize some key features
    df['user_behavior_norm'] = (
        df['amount_deviation'] + 
        df['user_amount_std'] / (df['user_avg_amount'] + 1) + 
        df['user_hour_std'].fillna(0) / 24  # Using fillna for compatibility
    ) / 3
    
    return df

def engineer_all_features(df):
    """
    Apply all feature engineering steps in sequence.
    """
    print("Starting comprehensive feature engineering...")
    print(f"Input shape: {df.shape}")
    
    # Apply feature engineering steps
    df = create_user_behavioral_features(df)
    df = create_velocity_features(df)
    df = create_temporal_features(df)
    df = create_device_ip_features(df)
    df = create_merchant_features(df)
    df = create_derived_features(df)
    
    print(f"Output shape: {df.shape}")
    print("Feature engineering completed!")
    
    return df

def get_advanced_feature_columns():
    """
    Return list of advanced feature columns created by this module.
    """
    return [
        'user_avg_amount', 'user_amount_std', 'user_transaction_count',
        'user_frequency', 'amount_deviation', 'prev_amount', 'amount_change_ratio',
        'user_hour_std', 'hour_diff', 'rolling_amount_mean', 'rolling_amount_std',
        'user_seq_velocity', 'user_recent_velocity', 'is_burst',
        'high_velocity_seq', 'is_night_transaction', 'potential_weekend',
        'seq_preference', 'unusual_hour', 'is_first_transaction',
        'transaction_sequence', 'avg_device_usage', 'max_device_usage',
        'avg_user_device_risk', 'multiple_devices', 'high_ip_risk',
        'high_device_risk', 'combined_risk_score', 'high_combined_risk',
        'merchant_fraud_rate', 'avg_merchant_amount', 'country_fraud_rate',
        'country_avg_device_risk', 'merchant_preference', 'unusual_merchant',
        'high_risk_category', 'amount_log', 'amount_squared', 'amount_bin',
        'hour_sin', 'hour_cos', 'velocity_risk_score', 'behavioral_anomaly_score',
        'user_behavior_norm'
    ]

def build_advanced_pipeline():
    """
    Build a complete pipeline with advanced feature engineering.
    """
    # Get feature columns based on new data structure
    categorical_features = ['payment_method', 'merchant_id', 'location']
    numeric_features = [
        'amount', 'transaction_id', 'user_id',
        'user_avg_amount', 'user_amount_std', 'user_frequency',
        'amount_deviation', 'amount_change_ratio', 'user_hour_std', 'hour_diff',
        'rolling_amount_mean', 'rolling_amount_std', 'user_seq_velocity',
        'user_recent_velocity', 'is_burst', 'high_velocity_seq',
        'is_night_transaction', 'unusual_hour', 'transaction_sequence',
        'avg_device_usage', 'max_device_usage', 'avg_user_device_risk',
        'multiple_devices', 'high_ip_risk', 'high_device_risk',
        'combined_risk_score', 'merchant_fraud_rate', 'avg_merchant_amount',
        'country_fraud_rate', 'merchant_preference', 'unusual_merchant',
        'high_risk_category', 'amount_log', 'amount_squared', 'amount_bin',
        'hour_sin', 'hour_cos', 'velocity_risk_score', 'behavioral_anomaly_score',
        'user_behavior_norm'
    ]
    
    # Create preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('categorical', OneHotEncoder(handle_unknown='ignore'), categorical_features),
            ('numeric', StandardScaler(), numeric_features),
        ],
        remainder='drop'
    )
    
    # Create model
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        min_samples_split=10,
        min_samples_leaf=5,
        class_weight='balanced',
        n_jobs=-1,
        random_state=42
    )
    
    # Create pipeline
    pipeline = Pipeline([
        ('preprocess', preprocessor),
        ('clf', model)
    ])
    
    return pipeline

if __name__ == "__main__":
    # Example usage
    print("Advanced Feature Engineering Module")
    print("==================================")
    print("This module provides comprehensive feature engineering for fraud detection.")
    print("Use engineer_all_features() to apply all transformations to your dataset.")
    print("Use build_advanced_pipeline() to create a complete ML pipeline.")