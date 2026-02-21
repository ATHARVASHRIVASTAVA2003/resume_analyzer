"""
Temporal and User-Level Feature Engineering

This module focuses on time-series patterns and user behavioral analytics
that are crucial for detecting sophisticated fraud patterns.

Features include:
- Time-series velocity patterns
- User behavioral baselines
- Seasonal and cyclical patterns
- Cross-user correlation features
- Session-based analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

def create_temporal_sequences(df):
    """
    Create time-ordered sequences for temporal analysis.
    """
    print("Creating temporal sequences...")
    
    # Sort by user and time
    df_sorted = df.sort_values(['user_id', 'transaction_id']).copy()
    
    # Create time-based indices
    df_sorted['transaction_order'] = df_sorted.groupby('user_id').cumcount()
    df_sorted['days_since_first'] = df_sorted.groupby('user_id')['transaction_order'].transform(
        lambda x: x * (90 / len(x)) if len(x) > 0 else 0
    )
    
    return df_sorted

def create_user_baselines(df):
    """
    Establish user behavioral baselines for anomaly detection.
    """
    print("Creating user behavioral baselines...")
    
    # User spending patterns over sequence windows
    df = df.sort_values(['user_id', 'transaction_id'])
    
    # 7-transaction and 30-transaction spending averages (sequence-based)
    df['user_7trans_avg'] = df.groupby('user_id')['amount'].transform(
        lambda x: x.rolling(window=7, min_periods=1).mean()
    )
    df['user_30trans_avg'] = df.groupby('user_id')['amount'].transform(
        lambda x: x.rolling(window=30, min_periods=1).mean()
    )
    
    # Deviation from baselines
    df['deviation_from_7trans'] = abs(df['amount'] - df['user_7trans_avg']) / (df['user_7trans_avg'] + 1)
    df['deviation_from_30trans'] = abs(df['amount'] - df['user_30trans_avg']) / (df['user_30trans_avg'] + 1)
    
    # User activity patterns
    df['user_daily_avg_transactions'] = df.groupby('user_id')['transaction_id'].transform('count') / 90
    
    # Sequence-based user preferences (using transaction_id modulo as proxy)
    # Create a proxy for 'hour' using transaction_id modulo to simulate time periods
    df['hour_proxy'] = df['transaction_id'] % 24
    user_hourly_activity = df.groupby(['user_id', 'hour_proxy']).size().reset_index(name='hourly_count')
    user_total_activity = df.groupby('user_id').size().reset_index(name='total_count')
    
    user_hourly_activity = user_hourly_activity.merge(user_total_activity, on='user_id')
    user_hourly_activity['hourly_preference'] = (
        user_hourly_activity['hourly_count'] / user_hourly_activity['total_count']
    )
    
    df = df.merge(
        user_hourly_activity[['user_id', 'hour_proxy', 'hourly_preference']], 
        on=['user_id', 'hour_proxy'], 
        how='left'
    )
    
    # User stability score (how consistent their behavior is)
    user_stability = df.groupby('user_id').agg({
        'amount': 'std'
    }).reset_index()
    user_stability.columns = ['user_id', 'amount_variability']
    
    df = df.merge(user_stability, on='user_id', how='left')
    
    # Placeholder for hour_entropy since we don't have hour data
    df['hour_entropy'] = 0  # Placeholder for compatibility
    
    return df

def create_session_features(df):
    """
    Create session-based features (transactions within sequence windows).
    """
    print("Creating session features...")
    
    df = df.sort_values(['user_id', 'transaction_id'])
    
    # Session definition: transactions with sequence gaps (using transaction_id as proxy)
    df['seq_diff_prev'] = df.groupby('user_id')['transaction_id'].diff().fillna(0)
    df['new_session'] = (df['seq_diff_prev'] > 100) | (df['seq_diff_prev'] < 0)  # Adjusted threshold for transaction_id gaps
    df['session_id'] = df.groupby('user_id')['new_session'].cumsum()
    
    # Session statistics
    session_stats = df.groupby(['user_id', 'session_id']).agg({
        'amount': ['sum', 'mean', 'count'],
        'transaction_id': 'nunique',
        'merchant_id': 'nunique',
        'location': 'nunique'
    }).reset_index()
    
    session_stats.columns = [
        'user_id', 'session_id', 'session_total_amount', 
        'session_avg_amount', 'session_transaction_count',
        'session_unique_ids', 'session_unique_merchants', 'session_unique_locations'
    ]
    
    df = df.merge(session_stats, on=['user_id', 'session_id'], how='left')
    
    # Session anomaly features
    df['session_amount_spike'] = (
        df['session_total_amount'] > df.groupby('user_id')['session_total_amount'].transform('mean') * 3
    ).astype(int)
    
    df['session_high_risk'] = (
        (df['session_unique_locations'] > 2) | 
        (df['session_unique_merchants'] > 3)
    ).astype(int)
    
    # For compatibility with original code, map to original column names
    df['time_diff_prev'] = df['seq_diff_prev']  # For compatibility
    df['session_unique_hours'] = df['session_unique_ids']  # For compatibility
    df['session_unique_categories'] = df['session_unique_merchants']  # For compatibility
    df['session_unique_countries'] = df['session_unique_locations']  # For compatibility
    
    return df

def create_cross_user_features(df):
    """
    Create features based on cross-user patterns and correlations.
    """
    print("Creating cross-user features...")
    
    # Device sharing patterns - since we don't have device_risk_score, use device_id
    device_users = df.groupby('device_id')['user_id'].nunique().reset_index()
    device_users.columns = ['device_id', 'users_per_device']
    
    df = df.merge(device_users, on='device_id', how='left')
    df['shared_device_risk'] = (df['users_per_device'] > 1).astype(int)
    
    # Since we don't have ip_risk_score, create a placeholder
    df['users_per_ip'] = 0  # Placeholder for compatibility
    df['shared_ip_risk'] = 0  # Placeholder for compatibility
    
    # Merchant abuse patterns
    merchant_users = df.groupby('merchant_id')['user_id'].nunique().reset_index()
    merchant_users.columns = ['merchant_id', 'unique_users_per_merchant']
    
    df = df.merge(merchant_users, on='merchant_id', how='left')
    df['merchant_popularity'] = df['unique_users_per_merchant'] / df['unique_users_per_merchant'].max() if df['unique_users_per_merchant'].max() > 0 else 0
    
    # High-risk user clusters - since we don't have device_risk_score and ip_risk_score, use placeholders
    user_risk_scores = df.groupby('user_id').agg({
        'is_fraud': 'mean'
    }).reset_index()
    user_risk_scores.columns = ['user_id', 'user_fraud_rate']
    
    df = df.merge(user_risk_scores, on='user_id', how='left')
    
    # Create placeholders for missing risk scores
    df['avg_user_device_risk'] = 0  # Placeholder for compatibility
    df['avg_user_ip_risk'] = 0  # Placeholder for compatibility
    
    # Fill NaN values that might occur
    if 'avg_user_device_risk' in df.columns:
        df['avg_user_device_risk'] = df['avg_user_device_risk'].fillna(0)
    else:
        df['avg_user_device_risk'] = 0
    if 'avg_user_ip_risk' in df.columns:
        df['avg_user_ip_risk'] = df['avg_user_ip_risk'].fillna(0)
    else:
        df['avg_user_ip_risk'] = 0
    if 'user_fraud_rate' in df.columns:
        df['user_fraud_rate'] = df['user_fraud_rate'].fillna(0)
    else:
        df['user_fraud_rate'] = 0
    
    return df

def create_cyclical_features(df):
    """
    Create cyclical sequence features for better pattern modeling.
    """
    print("Creating cyclical temporal features...")
    
    # Since we don't have 'hour' column, use transaction_id modulo as a proxy for cyclical features
    df['hour_sin'] = np.sin(2 * np.pi * (df['transaction_id'] % 24) / 24)
    df['hour_cos'] = np.cos(2 * np.pi * (df['transaction_id'] % 24) / 24)
    
    # Create sequence-of-day categories (using transaction_id modulo as proxy)
    df['time_of_day'] = pd.cut(
        df['transaction_id'] % 24, 
        bins=[0, 6, 12, 18, 24], 
        labels=['night', 'morning', 'afternoon', 'evening'],
        include_lowest=True
    )
    
    # Weekend vs weekday (approximate) - using transaction_id modulo
    df['is_weekend_approx'] = ((df['transaction_id'] % 24 >= 0) & (df['transaction_id'] % 24 <= 8)) | (df['transaction_id'] % 24 >= 22)
    
    # Business hour indicators - using transaction_id modulo
    df['business_hours'] = ((df['transaction_id'] % 24 >= 9) & (df['transaction_id'] % 24 <= 17)).astype(int)
    df['after_hours'] = ((df['transaction_id'] % 24 < 9) | (df['transaction_id'] % 24 > 17)).astype(int)
    
    return df

def create_anomaly_detection_features(df):
    """
    Create statistical anomaly detection features.
    """
    print("Creating anomaly detection features...")
    
    # Z-score based anomalies
    df['amount_zscore'] = (
        df['amount'] - df.groupby('user_id')['amount'].transform('mean')
    ) / (df.groupby('user_id')['amount'].transform('std') + 1)
    
    df['amount_anomaly'] = (abs(df['amount_zscore']) > 2).astype(int)
    
    # Isolation forest style features
    df['amount_percentile'] = df.groupby('user_id')['amount'].rank(pct=True)
    df['extreme_amount'] = ((df['amount_percentile'] > 0.95) | (df['amount_percentile'] < 0.05)).astype(int)
    
    # Behavioral change detection - use the new column names
    df['behavioral_change_score'] = (
        df['deviation_from_7trans'].fillna(0) * 0.4 + 
        df['deviation_from_30trans'].fillna(0) * 0.3 + 
        df['amount_anomaly'] * 0.3
    )
    
    # Composite risk indicators - use placeholders since we don't have these scores
    df['high_risk_profile'] = (
        (df['user_fraud_rate'].fillna(0) > 0.1) | 
        (df['avg_user_device_risk'].fillna(0) > 0.5) | 
        (df['avg_user_ip_risk'].fillna(0) > 0.5)
    ).astype(int)
    
    return df

def engineer_temporal_user_features(df):
    """
    Apply all temporal and user-level feature engineering.
    """
    print("Starting temporal and user-level feature engineering...")
    print(f"Input shape: {df.shape}")
    
    # Apply all feature engineering steps
    df = create_temporal_sequences(df)
    df = create_user_baselines(df)
    df = create_session_features(df)
    df = create_cross_user_features(df)
    df = create_cyclical_features(df)
    df = create_anomaly_detection_features(df)
    
    print(f"Output shape: {df.shape}")
    print("Temporal and user-level feature engineering completed!")
    
    return df

def get_temporal_user_feature_columns():
    """
    Return list of temporal and user-level feature columns.
    """
    return [
        'transaction_order', 'days_since_first', 'user_7day_avg', 'user_30day_avg',
        'deviation_from_7day', 'deviation_from_30day', 'user_daily_avg_transactions',
        'hourly_preference', 'amount_variability', 'hour_entropy', 'time_diff_prev',
        'new_session', 'session_id', 'session_total_amount', 'session_avg_amount',
        'session_transaction_count', 'session_unique_hours', 'session_unique_categories',
        'session_unique_countries', 'session_amount_spike', 'session_high_risk',
        'users_per_device', 'shared_device_risk', 'users_per_ip', 'shared_ip_risk',
        'unique_users_per_merchant', 'merchant_popularity', 'avg_user_device_risk',
        'avg_user_ip_risk', 'user_fraud_rate', 'hour_sin', 'hour_cos', 'time_of_day',
        'is_weekend_approx', 'business_hours', 'after_hours', 'amount_zscore',
        'amount_anomaly', 'amount_percentile', 'extreme_amount', 'behavioral_change_score',
        'high_risk_profile'
    ]

if __name__ == "__main__":
    print("Temporal and User-Level Feature Engineering Module")
    print("================================================")
    print("This module creates sophisticated temporal and behavioral features.")
    print("Use engineer_temporal_user_features() to apply all transformations.")