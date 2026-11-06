import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("tips.csv")

print("DATA VISUALIZATION")
print(df.head())

# Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="day", y="total_bill")
plt.title("Average Bill by Day")
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
plt.title("Total Bill vs Tip")
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="total_bill", bins=20, kde=True)
plt.title("Total Bill Distribution")
plt.show()

# Box Plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="day", y="total_bill")
plt.title("Bill Variation by Day")
plt.show()

print("DATA VISUALIZATION COMPLETED SUCCESSFULLY!")