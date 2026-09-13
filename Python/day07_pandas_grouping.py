# Day 7: Pandas Grouping and Aggregation
# --------------------------------------
# Problem Statement:
# Given a pandas DataFrame containing sales data, write a function that returns 
# the top 3 selling products by total revenue.

import pandas as pd

def get_top_3_products(df):
    # Calculate revenue per row
    df['revenue'] = df['quantity'] * df['price']
    
    # Group by product, sum the revenue, sort descending, and get the top 3
    top_products = df.groupby('product_name')['revenue'].sum().reset_index()
    top_products = top_products.sort_values(by='revenue', ascending=False).head(3)
    
    return top_products

if __name__ == "__main__":
    # Test data
    data = {
        'order_id': [1, 2, 3, 4, 5, 6],
        'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor', 'Mouse'],
        'quantity': [1, 5, 2, 2, 1, 3],
        'price': [1000, 20, 50, 1000, 300, 20]
    }
    
    df = pd.DataFrame(data)
    print("Sales Data:")
    print(df)
    
    print("\nTop 3 Products by Revenue:")
    print(get_top_3_products(df).to_string(index=False))
