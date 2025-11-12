import numpy as np
import pandas as pd

# Step 1: Generate random data with a few outliers
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100)  # Normal data
outliers = np.array([150, 160, 170])  # Add some obvious outliers
full_data = np.concatenate([data, outliers])

# Step 2: Create DataFrame and save to 'original_data.csv'
df = pd.DataFrame({'value': full_data})
df.to_csv('original_data.csv', index=False)

# Step 3: Remove outliers using Z-score method
mean = df['value'].mean()
std = df['value'].std()
z_scores = (df['value'] - mean) / std
# Consider data with |z| < 3 as non-outlier
clean_df = df[np.abs(z_scores) < 3]

# Step 4: Save cleaned data to a new CSV file
clean_df.to_csv('cleaned_data.csv', index=False)
