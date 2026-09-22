# Day 16: Handling Missing Values with Pandas
# -------------------------------------------
# Problem Statement:
# Given a pandas DataFrame with missing values, write a function to clean it by:
# 1. Dropping rows where the 'target' column is missing.
# 2. Filling missing numerical values with the column mean.
# 3. Filling missing categorical values with the mode.

import pandas as pd
import numpy as np

def clean_data(df):
    # 1. Drop rows with missing 'target'
    df = df.dropna(subset=['target']).copy()
    
    # 2. Fill missing numerical values with column mean
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # 3. Fill missing categorical values with the mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
        
    return df

if __name__ == "__main__":
    data = {
        'age': [25, np.nan, 30, 22, np.nan],
        'city': ['NY', 'LA', np.nan, 'NY', 'SF'],
        'target': [1, 0, 1, np.nan, 0]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)
    print("\nCleaned DataFrame:\n", clean_data(df))
