import pandas as pd
from scipy.stats import ks_2samp

print("Initiating AEGIS_V1 Liability Scan...")

# 1. Ingest the Data
baseline_df = pd.read_csv('baseline_data.csv')
production_df = pd.read_csv('production_data.csv')

# 2. The K-S Statistical Audit
print("Executing Kolmogorov-Smirnov Drift Detection...")
stat, p_value = ks_2samp(baseline_df['credit_score'], production_df['credit_score'])

print(f"\n--- AUDIT RESULTS ---")
print(f"Drift Statistic: {stat:.4f}")
print(f"P-Value: {p_value:.4e}")
print(f"---------------------")

# 3. Enterprise Alert Logic
# If p-value < 0.05, the distributions are significantly different.
if p_value < 0.05:
    print("\n🚨 CRITICAL ALERT: DATA DRIFT DETECTED! 🚨")
    print("The production data has mathematically deviated from the training baseline.")
    print("LIABILITY RISK: High. The AI model is operating in an unknown environment.")
    print("ACTION: Suspending automated decision-making pending human review.")
else:
    print("\n✅ System Stable: Production data aligns with baseline training.")