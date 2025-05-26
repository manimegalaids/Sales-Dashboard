# eda_sales.py
import pandas as pd
import os

# Ensure data/ folder exists
DATA_PATH = 'data/sales_data_sample.csv'
if not os.path.exists(DATA_PATH):
    print("❌ Error: Dataset not found.")
    exit()

df = pd.read_csv(DATA_PATH)
print("✅ Data loaded successfully. Shape:", df.shape)

# Preview
print(df.head())

# Optional: Clean or preprocess
df.dropna(inplace=True)
print("✅ Cleaned shape:", df.shape)

# Save cleaned version
df.to_csv('data/cleaned_sales.csv', index=False)
print("✅ Cleaned data saved.")
