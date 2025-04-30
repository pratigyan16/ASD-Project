import pandas as pd

# Load dataset
df = pd.read_csv("../Data/toddler_asd.csv")

# Step 1: Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("/", "_").str.replace("(", "").str.replace(")", "")

# Step 2: Drop rows with missing values
df = df.dropna()
print(f"✅ After dropping missing values: {df.shape[0]} rows remain.")

# Step 3: Encode categorical columns using pandas
# We'll map 'Yes'/'No' to 1/0 manually where applicable
if 'Class_ASD_Traits_' in df.columns:
    df['Class_ASD_Traits_'] = df['Class_ASD_Traits_'].map({'Yes': 1, 'No': 0})

# Convert other object-type columns to numeric codes
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category').cat.codes

print("✅ All categorical columns encoded using pandas.")

# Step 4: Preview cleaned data
print("\n🔍 Cleaned Data Preview:")
print(df.head())

# Optional: Save cleaned data
df.to_csv("../Data/toddler_asd_cleaned.csv", index=False)
print("📁 Cleaned dataset saved as 'toddler_asd_cleaned.csv'")
