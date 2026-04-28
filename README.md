# 🛡️ AEGIS_V1: Automated Model Risk Auditor
**Statistical Drift Detection & Liability Shield for Production AI**

Machine learning models degrade when real-world data shifts away from training data. AEGIS_V1 is an automated auditing engine designed to detect this "Data Drift" before it compromises model integrity or creates enterprise liability.

### ⚙️ Core Architecture
* **The Simulator (`simulate_stream.py`):** Synthesizes both a stable baseline dataset and a corrupted production data stream.
* **The Auditor (`aegis_auditor.py`):** Ingests the data streams and applies a rigorous **Kolmogorov-Smirnov (K-S) statistical test**.
* **The Alert Pipeline:** If the K-S test yields a p-value < 0.05, the engine mathematically proves the data distributions have diverged and triggers an automated system halt to prevent biased or hallucinated AI decision-making.

**Technical Stack:** Python, Pandas, NumPy, SciPy (Statistical Analysis).
**Domain Focus:** Model Risk Management (MRM), AI Auditing, Liability Protection.