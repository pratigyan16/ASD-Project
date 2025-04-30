import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Use your updated CSV file name
df = pd.read_csv("toddler_asd.csv")

# Show first 5 rows
print("🔍 Preview of Dataset:")
print(df.head())

# Dataset structure
print("\n🧾 Dataset Info:")
print(df.info())

# Check for missing values
print("\n📌 Missing Values:")
print(df.isnull().sum())

# Check unique values in ASD target column
print("\n⚖️ ASD Diagnosis Counts:")
print(df['Class/ASD Traits '].value_counts())

# Bar plot of ASD distribution
sns.set(style="whitegrid")
sns.countplot(x='Class/ASD Traits ', data=df)
plt.title("ASD Trait Distribution")
plt.xlabel("ASD Trait (Yes/No)")
plt.ylabel("Count")
plt.show()
