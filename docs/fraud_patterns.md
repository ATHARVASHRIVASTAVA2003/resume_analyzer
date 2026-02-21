# Fraud Pattern Documentation

## Overview
This document describes the explicit fraud patterns designed and injected into the synthetic dataset. Each pattern is based on real-world fraud behaviors observed in digital payment systems.

## Fraud Patterns Implemented

### 1. Velocity Attack Patterns (30% of fraud cases)
**Description**: Multiple rapid transactions from the same user within a short time window.

**Realism Justification**:
- **Real-world occurrence**: Common in account takeover scenarios where fraudsters quickly drain accounts
- **Detection rationale**: Legitimate users typically don't make 5-10 transactions within 2 hours
- **Business impact**: High financial loss potential, often targets high-value accounts
- **Prevention methods**: Velocity limits, transaction amount caps, real-time monitoring

**Implementation Details**:
- 5-10 transactions generated within 2-hour windows
- Random intervals between transactions (0-120 minutes)
- Mix of transaction types (Online, QR)
- Moderate transaction amounts ($50-$500)

### 2. Amount Spike Patterns (25% of fraud cases)
**Description**: Sudden, unusually large transactions that deviate significantly from user behavior.

**Realism Justification**:
- **Real-world occurrence**: Classic fraud pattern when accounts are compromised
- **Detection rationale**: Legitimate users rarely make purchases 10-50x their normal spending
- **Business impact**: High individual transaction losses
- **Prevention methods**: Amount-based rules, user spending profile analysis

**Implementation Details**:
- Transaction amounts 10-50x user's average spending
- Primarily Online transaction type (easier for large fraud)
- Random timing across 24-hour period
- High-risk merchant categories (Electronics, Travel)

### 3. Location Inconsistency Patterns (20% of fraud cases)
**Description**: Transactions from geographically distant locations within impossible time frames.

**Realism Justification**:
- **Real-world occurrence**: Physical impossibility indicates account compromise
- **Detection rationale**: Cannot be in US and UK within 2 hours realistically
- **Business impact**: Strong fraud indicator, high confidence alerts
- **Prevention methods**: Geolocation validation, travel pattern analysis

**Implementation Details**:
- Two transactions from different countries within 30-120 minutes
- Countries selected from high-risk regions (TR, DE, US, UK, AU)
- Same user ID for both transactions
- Online transaction type for remote execution

### 4. Shared Device Abuse Patterns (15% of fraud cases)
**Description**: Same high-risk device used by multiple different user accounts.

**Realism Justification**:
- **Real-world occurrence**: Botnets, malware, or shared compromised devices
- **Detection rationale**: Legitimate users typically use personal devices
- **Business impact**: Indicates systematic attack or malware distribution
- **Prevention methods**: Device fingerprinting, shared device monitoring

**Implementation Details**:
- 20 suspicious devices pre-generated with high risk scores
- Each device used by 2-3 different user accounts
- Transactions within 10-60 minute windows
- Online transaction type for remote access

### 5. Merchant Ring Patterns (10% of fraud cases)
**Description**: Coordinated fraudulent activity across multiple related merchants.

**Realism Justification**:
- **Real-world occurrence**: Organized fraud rings, colluding merchants
- **Detection rationale**: Unusual concentration at specific merchant types
- **Business impact**: Systemic risk, regulatory concerns
- **Prevention methods**: Merchant network analysis, relationship mapping

**Implementation Details**:
- Groups of 5 related suspicious merchants
- High-value transactions ($100-$2000)
- Concentrated in high-risk categories (Electronics, Travel, Clothing)
- Coordinated timing patterns

## Risk Scoring System

### Device Risk Scores
- **Normal devices**: Beta(1,15) distribution → ~0.06 average risk
- **Suspicious devices**: Beta(5,2) distribution → ~0.71 average risk
- **Threshold**: >0.5 considered high-risk

### IP Risk Scores
- **Normal IPs**: Beta(1,20) distribution → ~0.05 average risk
- **Suspicious IPs**: Beta(4,2) distribution → ~0.67 average risk
- **Threshold**: >0.5 considered high-risk

### Merchant Risk Factors
- **Electronics/Travel categories**: +0.1 base risk
- **High-risk countries (TR, DE)**: +0.08 base risk
- **Combined merchant risk**: Base + Beta(1,9) random component

## Pattern Distribution Rationale

The distribution (30%-25%-20%-15%-10%) reflects:
- **Velocity attacks**: Most common due to ease of execution
- **Amount spikes**: Very common in compromised accounts
- **Location inconsistencies**: Strong signal but less frequent
- **Shared devices**: Requires infrastructure, less common
- **Merchant rings**: Organized crime, least frequent but highest impact

## Detection Effectiveness

These patterns are designed to be:
1. **Detectable** by machine learning models using the engineered features
2. **Realistic** based on industry fraud intelligence
3. **Diverse** enough to test different detection approaches
4. **Measurable** with clear performance metrics

## Validation Approach

The effectiveness of these patterns can be validated through:
- Feature importance analysis showing relevant features are utilized
- SHAP values indicating correct reasoning paths
- Performance metrics demonstrating pattern detection capability
- Cross-validation showing consistent detection across time periods

## Future Enhancements

Potential additional patterns to consider:
- **Behavioral drift**: Gradual changes in user spending patterns
- **Session hijacking**: Multiple users from same session
- **Refund abuse**: Coordinated purchase-return cycles
- **Promotional fraud**: Exploitation of signup bonuses
- **Affiliate fraud**: Fake referrals and signups