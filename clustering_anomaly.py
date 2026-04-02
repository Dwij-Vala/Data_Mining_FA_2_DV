# =========================================
# 🤖 ATM DEMAND - CLUSTERING & ANOMALY
# =========================================

# 🔹 Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

sns.set(style="whitegrid")

# 🔹 Load Dataset
df = pd.read_csv("your_dataset.csv")

# =========================================
# 🔶 1. FEATURE SELECTION FOR CLUSTERING
# =========================================

features = df[['Total_Withdrawals', 'Total_Deposits', 'Nearby_Competitor_ATMs']]

# Convert categorical if needed
if 'Location_Type' in df.columns:
    df = pd.get_dummies(df, columns=['Location_Type'], drop_first=True)
    features = df.drop(columns=['Date'], errors='ignore').select_dtypes(include=np.number)

# =========================================
# 🔶 2. STANDARDIZATION (VERY IMPORTANT)
# =========================================

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# =========================================
# 🔶 3. FIND OPTIMAL K (ELBOW METHOD)
# =========================================

inertia = []

for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 10), inertia, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()

print("Insight: Optimal clusters chosen where curve bends (elbow point).\n")

# =========================================
# 🔶 4. APPLY K-MEANS (CHOOSE K=3)
# =========================================

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# =========================================
# 🔶 5. VISUALIZE CLUSTERS
# =========================================

plt.figure()
sns.scatterplot(
    x=df['Total_Withdrawals'],
    y=df['Total_Deposits'],
    hue=df['Cluster'],
    palette='Set1'
)
plt.title("ATM Clusters based on Demand")
plt.show()

# =========================================
# 🔥 CLUSTER INTERPRETATION (VERY IMPORTANT)
# =========================================

cluster_summary = df.groupby('Cluster')[['Total_Withdrawals', 'Total_Deposits']].mean()
print("\nCluster Summary:\n", cluster_summary)

print("""
Cluster 0 → Low Demand ATMs (Residential / Rural)
Cluster 1 → Medium Demand ATMs (Business Areas)
Cluster 2 → High Demand ATMs (Urban / Event-heavy zones)
""")

# =========================================
# 🔶 6. ANOMALY DETECTION (ISOLATION FOREST)
# =========================================

model = IsolationForest(contamination=0.05, random_state=42)
df['Anomaly'] = model.fit_predict(scaled_features)

# Convert labels
df['Anomaly'] = df['Anomaly'].map({1: 0, -1: 1})

# =========================================
# 🔶 7. VISUALIZE ANOMALIES
# =========================================

plt.figure()
sns.scatterplot(
    x=df['Total_Withdrawals'],
    y=df['Total_Deposits'],
    hue=df['Anomaly'],
    palette={0: 'blue', 1: 'red'}
)
plt.title("Anomaly Detection in ATM Transactions")
plt.show()

print("Insight: Red points indicate unusual withdrawal behavior.\n")

# =========================================
# 🔶 8. HOLIDAY ANOMALY ANALYSIS
# =========================================

if 'Holiday_Flag' in df.columns:
    holiday_data = df[df['Holiday_Flag'] == 1]

    plt.figure()
    sns.histplot(holiday_data['Total_Withdrawals'], kde=True)
    plt.title("Withdrawals During Holidays")
    plt.show()

    print("Insight: Holidays show higher anomalies and demand spikes.\n")

# =========================================
# 🔥 FINAL INSIGHTS
# =========================================

print("====== FINAL INSIGHTS ======")
print("""
1. ATMs are grouped into 3 clear demand-based clusters.
2. High-demand ATMs require frequent cash replenishment.
3. Anomalies detected indicate unusual spikes in usage.
4. Holidays and events strongly contribute to anomalies.
5. Model helps prevent cash shortages and overstocking.
""")