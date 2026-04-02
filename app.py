# =========================================
# 🚀 ATM INTELLIGENCE STREAMLIT APP
# =========================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

# =========================================
# 🔹 PAGE CONFIG
# =========================================
st.set_page_config(page_title="ATM Intelligence System", layout="wide")

# =========================================
# 🔹 TITLE
# =========================================
st.title("🏦 ATM Intelligence Demand Forecasting System")

st.markdown("""
Interactive system for:
- 📊 Exploratory Data Analysis (EDA)
- 🤖 Clustering ATMs
- 🚨 Detecting anomalies in withdrawals
""")

# =========================================
# 🔹 LOAD DATA (AUTO + UPLOAD OPTION)
# =========================================
@st.cache_data
def load_data():
    try:
        return pd.read_csv("atm_dataset.csv")
    except:
        return None

df = load_data()

uploaded_file = st.file_uploader("Or upload your dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

if df is None:
    st.error("⚠️ No dataset found. Please upload or add atm_dataset.csv")
    st.stop()

# =========================================
# 🔹 DATA PREVIEW
# =========================================
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# =========================================
# 🔹 SIDEBAR FILTERS
# =========================================
st.sidebar.header("🔍 Filters")

filtered_df = df.copy()

if "Day_of_Week" in df.columns:
    day = st.sidebar.selectbox("Day", ["All"] + list(df["Day_of_Week"].unique()))
    if day != "All":
        filtered_df = filtered_df[filtered_df["Day_of_Week"] == day]

if "Time_of_Day" in df.columns:
    time = st.sidebar.selectbox("Time", ["All"] + list(df["Time_of_Day"].unique()))
    if time != "All":
        filtered_df = filtered_df[filtered_df["Time_of_Day"] == time]

if "Location_Type" in df.columns:
    loc = st.sidebar.selectbox("Location", ["All"] + list(df["Location_Type"].unique()))
    if loc != "All":
        filtered_df = filtered_df[filtered_df["Location_Type"] == loc]

st.subheader("📊 Filtered Data")
st.write(f"Rows: {filtered_df.shape[0]}")

# =========================================
# 🔶 EDA SECTION
# =========================================
st.header("📊 Exploratory Data Analysis")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["Total_Withdrawals"], kde=True, ax=ax)
    ax.set_title("Withdrawals Distribution")
    st.pyplot(fig)
    st.info("Right-skewed → occasional spikes in demand.")

with col2:
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["Total_Deposits"], kde=True, ax=ax)
    ax.set_title("Deposits Distribution")
    st.pyplot(fig)
    st.info("Deposits are relatively stable.")

# Time trend
if "Date" in filtered_df.columns:
    st.subheader("⏳ Withdrawals Over Time")
    temp_df = filtered_df.copy()
    temp_df["Date"] = pd.to_datetime(temp_df["Date"])

    fig, ax = plt.subplots()
    temp_df.groupby("Date")["Total_Withdrawals"].sum().plot(ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# =========================================
# 🔶 CLUSTERING
# =========================================
st.header("🤖 Clustering Analysis")

numeric_df = filtered_df.select_dtypes(include=np.number)

scaler = StandardScaler()
scaled = scaler.fit_transform(numeric_df)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
filtered_df["Cluster"] = kmeans.fit_predict(scaled)

fig, ax = plt.subplots()
sns.scatterplot(
    x=filtered_df["Total_Withdrawals"],
    y=filtered_df["Total_Deposits"],
    hue=filtered_df["Cluster"],
    palette="Set1",
    ax=ax
)
ax.set_title("ATM Clusters")
st.pyplot(fig)

st.success("""
Cluster 0 → Low Demand  
Cluster 1 → Medium Demand  
Cluster 2 → High Demand  
""")

# =========================================
# 🔶 ANOMALY DETECTION
# =========================================
st.header("🚨 Anomaly Detection")

model = IsolationForest(contamination=0.05, random_state=42)
filtered_df["Anomaly"] = model.fit_predict(scaled)
filtered_df["Anomaly"] = filtered_df["Anomaly"].map({1: 0, -1: 1})

fig, ax = plt.subplots()
sns.scatterplot(
    x=filtered_df["Total_Withdrawals"],
    y=filtered_df["Total_Deposits"],
    hue=filtered_df["Anomaly"],
    palette={0: "blue", 1: "red"},
    ax=ax
)
ax.set_title("Anomalies in ATM Usage")
st.pyplot(fig)

st.warning("Red points indicate unusual spikes in withdrawals.")

# =========================================
# 🔶 HOLIDAY ANALYSIS
# =========================================
if "Holiday_Flag" in filtered_df.columns:
    st.subheader("🎉 Holiday Impact")

    fig, ax = plt.subplots()
    sns.barplot(x="Holiday_Flag", y="Total_Withdrawals", data=filtered_df, ax=ax)
    st.pyplot(fig)

# =========================================
# 🔥 FINAL INSIGHTS
# =========================================
st.header("📌 Key Insights")

st.markdown("""
- ATM withdrawals show demand spikes and variability  
- Weekends and evenings generally have higher usage  
- Clustering helps identify high-demand vs low-demand ATMs  
- Anomalies highlight unusual transaction spikes  
- Holidays and events significantly impact withdrawals  
""")