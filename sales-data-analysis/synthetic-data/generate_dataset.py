import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

data = {
    "OrderID": range(100001, 100001 + rows),
    "OrderDate": pd.date_range(start="2023-01-01", periods=rows, freq="D"),
    "CustomerID": np.random.randint(1000, 1200, rows),
    "CustomerSegment": np.random.choice(
        ["Consumer", "Corporate", "Home Office"], rows
    ),
    "ProductCategory": np.random.choice(
        ["Electronics", "Furniture", "Clothing"], rows
    ),
    "ProductName": np.random.choice(
        ["Laptop", "Chair", "T-Shirt", "Mobile", "Table", "Jeans"], rows
    ),
    "UnitPrice": np.round(np.random.uniform(200, 50000, rows), 2),
    "Quantity": np.random.randint(1, 10, rows),
    "Discount": np.round(np.random.uniform(0, 0.3, rows), 2),
    "Region": np.random.choice(
        ["North", "South", "East", "West"], rows
    ),
    "PaymentMode": np.random.choice(
        ["Card", "UPI", "Cash"], rows
    ),
}

df = pd.DataFrame(data)

df["Revenue"] = (
    df["UnitPrice"] * df["Quantity"] * (1 - df["Discount"])
).round(2)

df.to_csv("sales_data.csv", index=False)

print("Dataset generated: sales_data.csv")
