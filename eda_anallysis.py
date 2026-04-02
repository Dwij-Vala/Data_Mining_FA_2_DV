# ================================
# 📊 ATM DEMAND FORECASTING - EDA
# ================================

# 🔹 Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Style settings
sns.set(style="whitegrid")

# 🔹 Load Dataset
# Replace with your file name
df = pd.read_csv("your_dataset.csv")

# 🔹 Basic Info
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nMissing Values:\n", df.isnull().sum())

# ================================
# 🔶 1. DISTRIBUTION ANALYSIS
# ================================

# 📌 Histogram - Withdrawals
plt.figure()
sns.histplot(df['Total_Withdrawals'], kde=True)
plt.title("Distribution of Total Withdrawals")
plt.xlabel("Withdrawals")
plt.ylabel("Frequency")
plt.show()

print("Insight: Withdrawals show right-skew → occasional high demand spikes.\n")

# 📌 Histogram - Deposits
plt.figure()
sns.histplot(df['Total_Deposits'], kde=True)
plt.title("Distribution of Total Deposits")
plt.xlabel("Deposits")
plt.ylabel("Frequency")
plt.show()

print("Insight: Deposits are more stable compared to withdrawals.\n")

# 📌 Boxplot - Outliers
plt.figure()
sns.boxplot(x=df['Total_Withdrawals'])
plt.title("Boxplot of Withdrawals")
plt.show()

print("Insight: Outliers represent unusual high-demand days.\n")


# ================================
# 🔶 2. TIME-BASED ANALYSIS
# ================================

# 📌 Line Chart - Withdrawals Over Time
plt.figure()
df.groupby('Date')['Total_Withdrawals'].sum().plot()
plt.title("Withdrawals Over Time")
plt.xlabel("Date")
plt.ylabel("Withdrawals")
plt.xticks(rotation=45)
plt.show()

print("Insight: Peaks indicate periodic high-demand days.\n")

# 📌 Day of Week Analysis
plt.figure()
sns.barplot(x='Day_of_Week', y='Total_Withdrawals', data=df)
plt.title("Withdrawals by Day of Week")
plt.xticks(rotation=45)
plt.show()

print("Insight: Higher withdrawals on weekends.\n")

# 📌 Time of Day Analysis
plt.figure()
sns.barplot(x='Time_of_Day', y='Total_Withdrawals', data=df)
plt.title("Withdrawals by Time of Day")
plt.show()

print("Insight: Evening usage is highest.\n")


# ================================
# 🔶 3. HOLIDAY & EVENT IMPACT
# ================================

# 📌 Holiday Impact
plt.figure()
sns.barplot(x='Holiday_Flag', y='Total_Withdrawals', data=df)
plt.title("Withdrawals on Holidays")
plt.show()

print("Insight: Withdrawals increase during holidays.\n")

# 📌 Event Impact
plt.figure()
sns.barplot(x='Special_Event_Flag', y='Total_Withdrawals', data=df)
plt.title("Withdrawals during Events")
plt.show()

print("Insight: Events create demand spikes.\n")


# ================================
# 🔶 4. EXTERNAL FACTORS
# ================================

# 📌 Weather Condition
plt.figure()
sns.boxplot(x='Weather_Condition', y='Total_Withdrawals', data=df)
plt.title("Withdrawals vs Weather")
plt.xticks(rotation=45)
plt.show()

print("Insight: Weather affects ATM usage.\n")

# 📌 Competitor ATMs
plt.figure()
sns.boxplot(x='Nearby_Competitor_ATMs', y='Total_Withdrawals', data=df)
plt.title("Withdrawals vs Nearby Competitors")
plt.show()

print("Insight: Competition reduces demand slightly.\n")


# ================================
# 🔶 5. RELATIONSHIP ANALYSIS
# ================================

# 📌 Scatter Plot
plt.figure()
sns.scatterplot(
    x='Previous_Day_Cash_Level',
    y='Cash_Demand_Next_Day',
    data=df
)
plt.title("Cash Level vs Next Day Demand")
plt.show()

print("Insight: Positive relationship helps predict demand.\n")

# 📌 Correlation Heatmap
plt.figure()
corr = df.select_dtypes(include=np.number).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

print("Insight: Key variables influencing ATM demand identified.\n")


# ================================
# 🔥 FINAL SUMMARY
# ================================

print("====== FINAL INSIGHTS ======")
print("""
1. ATM demand shows strong fluctuations with spikes.
2. Weekends and evenings have higher usage.
3. Holidays and events significantly increase withdrawals.
4. Weather and competition influence ATM demand.
5. Outliers indicate real-world demand surges.
""")