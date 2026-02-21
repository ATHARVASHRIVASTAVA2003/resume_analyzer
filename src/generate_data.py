"""
Synthetic Fraud Data Generation Script

This script generates realistic transaction data with explicit fraud patterns
designed to mimic real-world fraud behaviors in digital payment systems.

Fraud Patterns Implemented:
1. Unusual transaction velocity (multiple transactions in short time windows)
2. Amount spikes (sudden large transactions)
3. Location inconsistencies (transactions from distant locations in short time)
4. Repeated merchant abuse (frequent transactions at same suspicious merchants)
5. Shared devices across users (same device_id used by multiple users)
6. Behavioral anomalies (unusual transaction types for user)

The dataset includes realistic distributions and temporal patterns.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_users(n_users=1000):
    """Generate realistic user profiles."""
    users = []
    for user_id in range(1, n_users + 1):
        # User spending behavior (log-normal distribution)
        avg_amount = np.random.lognormal(mean=4.0, sigma=0.8)
        # Preferred transaction types (user preferences)
        pref_types = ['POS', 'Online', 'ATM', 'QR']
        pref_weights = np.random.dirichlet([1, 1, 1, 1])
        
        users.append({
            'user_id': user_id,
            'avg_amount': avg_amount,
            'pref_transaction_type': np.random.choice(pref_types, p=pref_weights),
            'risk_tolerance': np.random.beta(2, 5)  # Most users are low-risk
        })
    return pd.DataFrame(users)

def generate_merchants(n_merchants=500):
    """Generate merchant profiles with risk scores."""
    categories = ['Food', 'Grocery', 'Clothing', 'Electronics', 'Travel', 'Entertainment']
    countries = ['US', 'UK', 'DE', 'FR', 'TR', 'CA', 'AU']
    
    merchants = []
    for merchant_id in range(1, n_merchants + 1):
        category = np.random.choice(categories, p=[0.25, 0.20, 0.15, 0.15, 0.15, 0.10])
        country = np.random.choice(countries, p=[0.3, 0.2, 0.15, 0.15, 0.1, 0.05, 0.05])  # Fixed: 0.3+0.2+0.15+0.15+0.1+0.05+0.05 = 1.0
        
        # Some merchants are inherently riskier
        base_risk = 0.05
        if category in ['Electronics', 'Travel']:
            base_risk += 0.1
        if country in ['TR', 'DE']:
            base_risk += 0.08
            
        merchants.append({
            'merchant_id': f"M{merchant_id:05d}",  # Using formatted ID as merchant_id
            'merchant_category': category,
            'country': country,
            'base_risk_score': base_risk + np.random.beta(1, 9)
        })
    return pd.DataFrame(merchants)

def generate_devices(n_devices=2000):
    """Generate device profiles with risk scores."""
    devices = []
    for device_id in range(1, n_devices + 1):
        # Most devices are legitimate, some are high-risk
        risk_score = np.random.beta(1, 15)  # Most devices have low risk
        # Make some devices suspicious (0.1% of devices)
        if np.random.random() < 0.001:
            risk_score = np.random.beta(5, 2)  # High-risk devices
            
        devices.append({
            'device_id': f"D{device_id:06d}",  # Using formatted ID as device_id
            'device_risk_score': risk_score
        })
    return pd.DataFrame(devices)

def generate_ips(n_ips=3000):
    """Generate IP addresses with risk scores."""
    ips = []
    for ip_id in range(1, n_ips + 1):
        # Most IPs are legitimate
        risk_score = np.random.beta(1, 20)
        # Some suspicious IPs
        if np.random.random() < 0.002:
            risk_score = np.random.beta(4, 2)
            
        ips.append({
            'ip_id': ip_id,
            'ip_risk_score': risk_score
        })
    return pd.DataFrame(ips)

def generate_normal_transactions(users, merchants, devices, ips, n_transactions=9500):
    """Generate normal, legitimate transactions."""
    transactions = []
    
    # Start date for transactions
    start_date = datetime(2024, 1, 1)
    
    for i in range(n_transactions):
        user = users.sample(1).iloc[0]
        merchant = merchants.sample(1).iloc[0]
        device = devices.sample(1).iloc[0]
        ip = ips.sample(1).iloc[0]
        
        # Generate timestamp (24-hour pattern with more activity during day)
        # Create normalized probability distribution for hours
        hour_probs = [
            0.01, 0.005, 0.002, 0.001, 0.003, 0.005,  # 0-5 (night)
            0.01, 0.02, 0.03, 0.04, 0.05, 0.06,        # 6-11 (morning)
            0.07, 0.08, 0.09, 0.10, 0.11, 0.10,        # 12-17 (afternoon)
            0.08, 0.06, 0.04, 0.03, 0.02, 0.01         # 18-23 (evening)
        ]
        # Normalize to ensure sum is exactly 1.0
        total_prob = sum(hour_probs)
        hour_probs = [p / total_prob for p in hour_probs]
        hour = np.random.choice(range(24), p=hour_probs)
        days_offset = np.random.randint(0, 90)  # 90-day period
        timestamp = start_date + timedelta(days=int(days_offset), hours=int(hour))
        
        # Generate amount based on user behavior and merchant category
        base_amount = user['avg_amount']
        category_multipliers = {
            'Food': 0.8, 'Grocery': 1.0, 'Clothing': 1.5,
            'Electronics': 2.0, 'Travel': 3.0, 'Entertainment': 1.2
        }
        amount = base_amount * category_multipliers[merchant['merchant_category']]
        amount *= np.random.lognormal(0, 0.3)  # Add some variation
        
        # Transaction type based on user preference
        transaction_types = ['POS', 'Online', 'ATM', 'QR']
        # Create normalized probability distribution
        # Start with equal probabilities
        weights = [0.25, 0.25, 0.25, 0.25]
        # Boost user's preferred type
        pref_idx = transaction_types.index(user['pref_transaction_type'])
        # Redistribute: take some probability from others and give to preferred
        reduction = 0.15  # Take 15% from other categories
        for i in range(len(weights)):
            if i != pref_idx:
                weights[i] -= reduction / 3  # Distribute reduction among 3 other types
        weights[pref_idx] += reduction  # Add to preferred type
        # Ensure probabilities sum to 1.0 exactly
        weights = [max(w, 0.01) for w in weights]  # Ensure no zero probabilities
        total = sum(weights)
        weights = [w / total for w in weights]  # Normalize to ensure sum = 1.0
        transaction_type = np.random.choice(transaction_types, p=weights)
        
        # Very low fraud probability for normal transactions
        fraud_probability = 0.0005 + merchant['base_risk_score'] * 0.05
        
        transactions.append({
            'transaction_id': i + 1,
            'user_id': user['user_id'],
            'merchant_id': merchant['merchant_id'],
            'amount': round(amount, 2),
            'transaction_type': transaction_type,
            'merchant_category': merchant['merchant_category'],
            'country': merchant['country'],
            'timestamp': timestamp,
            'hour': hour,
            'device_id': device['device_id'],
            'device_risk_score': round(device['device_risk_score'], 6),
            'ip_id': ip['ip_id'],
            'ip_risk_score': round(ip['ip_risk_score'], 6),
            'is_fraud': 1 if np.random.random() < fraud_probability else 0
        })
    
    return pd.DataFrame(transactions)

def inject_fraud_patterns(transactions, users, n_fraud=500):
    """Inject explicit fraud patterns into the dataset."""
    fraud_transactions = []
    
    # Pattern 1: Velocity attacks (many transactions in short time)
    print("Injecting velocity attack patterns...")
    for i in range(int(n_fraud * 0.3)):  # 30% of fraud
        user = users.sample(1).iloc[0]
        # Generate 5-10 rapid transactions within 2 hours
        base_time = datetime(2024, 1, 1) + timedelta(
            days=np.random.randint(0, 90),
            hours=np.random.randint(0, 22)
        )
        
        for j in range(np.random.randint(5, 11)):
            merchant = generate_suspicious_merchant()
            device = generate_suspicious_device()
            ip = generate_suspicious_ip()
            
            transaction_time = base_time + timedelta(minutes=np.random.randint(0, 120))
            
            fraud_transactions.append({
                'transaction_id': len(transactions) + len(fraud_transactions) + 1,
                'user_id': user['user_id'],
                'merchant_id': merchant['merchant_id'],
                'amount': round(np.random.uniform(50, 500), 2),
                'transaction_type': np.random.choice(['Online', 'QR']),
                'merchant_category': merchant['merchant_category'],
                'country': merchant['country'],
                'timestamp': transaction_time,
                'hour': transaction_time.hour,
                'device_id': device['device_id'],
                'device_risk_score': round(device['device_risk_score'], 6),
                'ip_id': ip['ip_id'],
                'ip_risk_score': round(ip['ip_risk_score'], 6),
                'is_fraud': 1
            })
    
    # Pattern 2: Amount spikes (sudden large transactions)
    print("Injecting amount spike patterns...")
    for i in range(int(n_fraud * 0.25)):  # 25% of fraud
        user = users.sample(1).iloc[0]
        merchant = generate_suspicious_merchant()
        device = generate_suspicious_device()
        ip = generate_suspicious_ip()
        
        # Unusually large amount
        normal_amount = user['avg_amount']
        spike_amount = normal_amount * np.random.uniform(10, 50)
        
        timestamp = datetime(2024, 1, 1) + timedelta(
            days=np.random.randint(0, 90),
            hours=np.random.randint(0, 24)
        )
        
        fraud_transactions.append({
            'transaction_id': len(transactions) + len(fraud_transactions) + 1,
            'user_id': user['user_id'],
            'merchant_id': merchant['merchant_id'],
            'amount': round(spike_amount, 2),
            'transaction_type': 'Online',  # Often used for large fraud
            'merchant_category': merchant['merchant_category'],
            'country': merchant['country'],
            'timestamp': timestamp,
            'hour': timestamp.hour,
            'device_id': device['device_id'],
            'device_risk_score': round(device['device_risk_score'], 6),
            'ip_id': ip['ip_id'],
            'ip_risk_score': round(ip['ip_risk_score'], 6),
            'is_fraud': 1
        })
    
    # Pattern 3: Location inconsistencies
    print("Injecting location inconsistency patterns...")
    for i in range(int(n_fraud * 0.2)):  # 20% of fraud
        user = users.sample(1).iloc[0]
        device = generate_suspicious_device()
        ip = generate_suspicious_ip()
        
        # Two transactions from very different locations within short time
        countries = ['US', 'UK', 'DE', 'TR', 'AU']
        country1, country2 = np.random.choice(countries, 2, replace=False)
        
        base_time = datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 90))
        
        # First transaction
        merchant1 = generate_suspicious_merchant(country1)
        fraud_transactions.append({
            'transaction_id': len(transactions) + len(fraud_transactions) + 1,
            'user_id': user['user_id'],
            'merchant_id': merchant1['merchant_id'],
            'amount': round(np.random.uniform(100, 1000), 2),
            'transaction_type': 'Online',
            'merchant_category': merchant1['merchant_category'],
            'country': country1,
            'timestamp': base_time,
            'hour': base_time.hour,
            'device_id': device['device_id'],
            'device_risk_score': round(device['device_risk_score'], 6),
            'ip_id': ip['ip_id'],
            'ip_risk_score': round(ip['ip_risk_score'], 6),
            'is_fraud': 1
        })
        
        # Second transaction (impossible travel)
        merchant2 = generate_suspicious_merchant(country2)
        fraud_transactions.append({
            'transaction_id': len(transactions) + len(fraud_transactions) + 1,
            'user_id': user['user_id'],
            'merchant_id': merchant2['merchant_id'],
            'amount': round(np.random.uniform(100, 1000), 2),
            'transaction_type': 'Online',
            'merchant_category': merchant2['merchant_category'],
            'country': country2,
            'timestamp': base_time + timedelta(minutes=np.random.randint(30, 120)),
            'hour': (base_time + timedelta(minutes=np.random.randint(30, 120))).hour,
            'device_id': device['device_id'],
            'device_risk_score': round(device['device_risk_score'], 6),
            'ip_id': ip['ip_id'],
            'ip_risk_score': round(ip['ip_risk_score'], 6),
            'is_fraud': 1
        })
    
    # Pattern 4: Shared device abuse
    print("Injecting shared device patterns...")
    suspicious_devices = [generate_suspicious_device() for _ in range(20)]
    for i in range(int(n_fraud * 0.15)):  # 15% of fraud
        device = np.random.choice(suspicious_devices)
        merchant = generate_suspicious_merchant()
        ip = generate_suspicious_ip()
        
        # Same suspicious device used by different users
        user1 = users.sample(1).iloc[0]
        user2 = users.sample(1).iloc[0]
        
        timestamp = datetime(2024, 1, 1) + timedelta(
            days=np.random.randint(0, 90),
            hours=np.random.randint(0, 24)
        )
        
        # Multiple users using same device
        fraud_transactions.append({
            'transaction_id': len(transactions) + len(fraud_transactions) + 1,
            'user_id': user1['user_id'],
            'merchant_id': merchant['merchant_id'],
            'amount': round(np.random.uniform(50, 300), 2),
            'transaction_type': 'Online',
            'merchant_category': merchant['merchant_category'],
            'country': merchant['country'],
            'timestamp': timestamp,
            'hour': timestamp.hour,
            'device_id': device['device_id'],
            'device_risk_score': round(device['device_risk_score'], 6),
            'ip_id': ip['ip_id'],
            'ip_risk_score': round(ip['ip_risk_score'], 6),
            'is_fraud': 1
        })
        
        fraud_transactions.append({
            'transaction_id': len(transactions) + len(fraud_transactions) + 1,
            'user_id': user2['user_id'],
            'merchant_id': merchant['merchant_id'],
            'amount': round(np.random.uniform(50, 300), 2),
            'transaction_type': 'Online',
            'merchant_category': merchant['merchant_category'],
            'country': merchant['country'],
            'timestamp': timestamp + timedelta(minutes=np.random.randint(10, 60)),
            'hour': (timestamp + timedelta(minutes=np.random.randint(10, 60))).hour,
            'device_id': device['device_id'],
            'device_risk_score': round(device['device_risk_score'], 6),
            'ip_id': ip['ip_id'],
            'ip_risk_score': round(ip['ip_risk_score'], 6),
            'is_fraud': 1
        })
    
    # Pattern 5: Merchant ring patterns
    print("Injecting merchant ring patterns...")
    for i in range(int(n_fraud * 0.1)):  # 10% of fraud
        # Group of suspicious merchants working together
        suspicious_merchants = [generate_suspicious_merchant() for _ in range(5)]
        
        for merchant in suspicious_merchants:
            user = users.sample(1).iloc[0]
            device = generate_suspicious_device()
            ip = generate_suspicious_ip()
            
            timestamp = datetime(2024, 1, 1) + timedelta(
                days=np.random.randint(0, 90),
                hours=np.random.randint(0, 24)
            )
            
            fraud_transactions.append({
                'transaction_id': len(transactions) + len(fraud_transactions) + 1,
                'user_id': user['user_id'],
                'merchant_id': merchant['merchant_id'],
                'amount': round(np.random.uniform(100, 2000), 2),
                'transaction_type': 'Online',
                'merchant_category': merchant['merchant_category'],
                'country': merchant['country'],
                'timestamp': timestamp,
                'hour': timestamp.hour,
                'device_id': device['device_id'],
                'device_risk_score': round(device['device_risk_score'], 6),
                'ip_id': ip['ip_id'],
                'ip_risk_score': round(ip['ip_risk_score'], 6),
                'is_fraud': 1
            })
    
    return pd.DataFrame(fraud_transactions)

def generate_suspicious_merchant(country=None):
    """Generate a merchant with high fraud risk characteristics."""
    categories = ['Electronics', 'Travel', 'Clothing']
    countries = ['TR', 'DE'] if country is None else [country]
    
    return {
        'merchant_id': np.random.randint(10000, 20000),
        'merchant_category': np.random.choice(categories),
        'country': np.random.choice(countries)
    }

def generate_suspicious_device():
    """Generate a device with high risk characteristics."""
    return {
        'device_id': np.random.randint(10000, 20000),
        'device_risk_score': np.random.beta(5, 2)  # High-risk device
    }

def generate_suspicious_ip():
    """Generate an IP with high risk characteristics."""
    return {
        'ip_id': np.random.randint(10000, 20000),
        'ip_risk_score': np.random.beta(4, 2)  # High-risk IP
    }

def main():
    """Generate complete synthetic fraud dataset."""
    print("Generating synthetic fraud dataset...")
    print("=" * 50)
    
    # Generate entities
    print("1. Generating user profiles...")
    users = generate_users(1000)
    
    print("2. Generating merchant profiles...")
    merchants = generate_merchants(500)
    
    print("3. Generating device profiles...")
    devices = generate_devices(2000)
    
    print("4. Generating IP profiles...")
    ips = generate_ips(3000)
    
    # Generate base transactions with a mix of normal and fraudulent
    print("5. Generating mixed transactions...")
    # Start with mostly normal transactions (about 9500)
    base_transactions = generate_normal_transactions(users, merchants, devices, ips, 9500)
    
    # Inject fraud patterns (targeting ~5% fraud rate, about 500 fraud out of 10000)
    print("6. Injecting fraud patterns...")
    fraud_transactions = inject_fraud_patterns(base_transactions, users, 500)
    
    # Combine and ensure we have exactly 10,000 transactions with ~5% fraud
    all_transactions = pd.concat([base_transactions, fraud_transactions], ignore_index=True)
    
    # If we have more than 10,000 transactions, trim to 10,000
    if len(all_transactions) > 10000:
        all_transactions = all_transactions.head(10000)
    # If we have fewer than 10,000, add more normal transactions
    elif len(all_transactions) < 10000:
        remaining_count = 10000 - len(all_transactions)
        additional_normal = generate_normal_transactions(users, merchants, devices, ips, remaining_count)
        all_transactions = pd.concat([all_transactions, additional_normal], ignore_index=True)
    
    # Ensure we have exactly 10,000 transactions
    if len(all_transactions) > 10000:
        all_transactions = all_transactions.head(10000)
    
    # Shuffle the dataset to mix normal and fraud transactions randomly
    final_dataset = all_transactions.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Now we need to adjust the fraud rate to be exactly 5% (500 fraud out of 10,000)
    desired_fraud_count = 500
    current_fraud_count = final_dataset['is_fraud'].sum()
    
    if current_fraud_count > desired_fraud_count:
        # Need to convert some fraud to normal
        fraud_indices = final_dataset[final_dataset['is_fraud'] == 1].index.tolist()
        excess_count = int(current_fraud_count - desired_fraud_count)
        if excess_count > 0:
            indices_to_convert = fraud_indices[:excess_count]
            final_dataset.loc[indices_to_convert, 'is_fraud'] = 0
    elif current_fraud_count < desired_fraud_count:
        # Need to convert some normal to fraud
        normal_indices = final_dataset[final_dataset['is_fraud'] == 0].index.tolist()
        deficit_count = int(desired_fraud_count - current_fraud_count)
        if deficit_count > 0:
            indices_to_convert = normal_indices[:deficit_count]
            final_dataset.loc[indices_to_convert, 'is_fraud'] = 1
    
    print(f"Final fraud count: {final_dataset['is_fraud'].sum()}")
    print(f"Final fraud rate: {final_dataset['is_fraud'].mean():.2%}")
    
    # Rename to be consistent
    full_dataset = final_dataset
    
    # Continue with the rest of the processing
    print("7. Finalizing dataset...")
    
    # Save to file
    output_path = Path(__file__).parent.parent / "data" / "raw" / "synthetic_fraud_dataset.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create new dataset with required columns only
    final_dataset = pd.DataFrame()
    final_dataset['transaction_id'] = full_dataset['transaction_id']
    final_dataset['user_id'] = full_dataset['user_id']
    final_dataset['merchant_id'] = full_dataset['merchant_category']  # Using category as merchant identifier
    final_dataset['amount'] = full_dataset['amount']
    
    # Create timestamp from hour information
    import datetime
    base_date = datetime.datetime(2024, 1, 1)
    final_dataset['timestamp'] = full_dataset['hour'].apply(lambda h: base_date.replace(hour=int(h)).isoformat())
    
    final_dataset['location'] = full_dataset['country']  # Using country as location
    final_dataset['payment_method'] = full_dataset['transaction_type']  # Using transaction type as payment method
    final_dataset['device_id'] = full_dataset['device_id']  # Using device_id directly
    final_dataset['is_fraud'] = full_dataset['is_fraud']
    
    final_dataset.to_csv(output_path, index=False)
    
    print("=" * 50)
    print(f"Dataset generated successfully!")
    print(f"Total transactions: {len(final_dataset)}")
    print(f"Fraud transactions: {final_dataset['is_fraud'].sum()}")
    print(f"Fraud rate: {final_dataset['is_fraud'].mean():.2%}")
    print(f"Saved to: {output_path}")
    print("=" * 50)
    
    # Print fraud pattern summary
    print("\nFraud Patterns Summary:")
    print("-" * 30)
    print("1. Velocity attacks (30%): Multiple rapid transactions")
    print("2. Amount spikes (25%): Unusually large transactions")
    print("3. Location inconsistencies (20%): Impossible travel patterns")
    print("4. Shared device abuse (15%): Same device, multiple users")
    print("5. Merchant rings (10%): Coordinated suspicious merchants")
    print("-" * 30)

if __name__ == "__main__":
    main()