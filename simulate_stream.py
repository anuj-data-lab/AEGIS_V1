import numpy as np
import pandas as pd

print("Synthesizing Corporate AI Data Streams...")

# 1. Generate the Baseline (What the AI expects)
# Simulating 1000 credit scores with a mean of 700
np.random.seed(42) 
baseline_scores = np.random.normal(loc=700, scale=50, size=1000)

# 2. Generate the Production Stream (The hidden threat)
# Simulating a live environment where scores have suddenly dropped (mean of 650)
production_scores = np.random.normal(loc=650, scale=60, size=1000)

# Export the payloads
pd.DataFrame({'credit_score': baseline_scores}).to_csv('baseline_data.csv', index=False)
pd.DataFrame({'credit_score': production_scores}).to_csv('production_data.csv', index=False)

print("SUCCESS: Live and Baseline data streams generated. Awaiting audit.")