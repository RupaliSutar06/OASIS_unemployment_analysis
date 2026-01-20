# 1️⃣ Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2️⃣ Load Dataset
df = pd.read_csv("Unemployment in India.csv")

print("First 5 Rows of Dataset:")
print(df.head())

# 3️⃣ Dataset Information
print("\nDataset Info:")
print(df.info())

# 4️⃣ Rename Columns (easy names)
df.columns = [
    "Region",
    "Date",
    "Frequency",
    "Unemployment_Rate",
    "Employed",
    "Labour_Participation_Rate",
    "Area"
]

# 5️⃣ Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# 6️⃣ Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# ================================
# 📊 DATA VISUALIZATION
# ================================

# 7️⃣ Unemployment Rate Over Time (India)
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Unemployment_Rate"])
plt.title("Unemployment Rate in India Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

# 8️⃣ Covid-19 Impact (Year 2020)
covid_data = df[df["Date"].dt.year == 2020]

plt.figure(figsize=(10,5))
sns.lineplot(
    x="Date",
    y="Unemployment_Rate",
    data=covid_data
)
plt.title("Unemployment Rate During Covid-19 (2020)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# 9️⃣ Region-wise Average Unemployment Rate
region_avg = df.groupby("Region")["Unemployment_Rate"].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
region_avg.plot(kind="bar")
plt.title("Average Unemployment Rate by Region")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Region")
plt.show()

# 🔟 Area-wise Comparison (Urban vs Rural)
plt.figure(figsize=(6,4))
sns.barplot(
    x="Area",
    y="Unemployment_Rate",
    data=df
)
plt.title("Urban vs Rural Unemployment Rate")
plt.show()

# 1️⃣1️⃣ Boxplot (Distribution)
plt.figure(figsize=(6,4))
sns.boxplot(
    y="Unemployment_Rate",
    data=df
)
plt.title("Distribution of Unemployment Rate")
plt.show()

# ================================
# 📝 CONCLUSION PRINT
# ================================

print("\nConclusion:")
print("- Unemployment rate increased sharply during Covid-19 (2020).")
print("- Significant variation is observed across different regions.")
print("- Urban and Rural areas show different unemployment patterns.")
print("- Covid-19 had a strong negative impact on employment in India.")
