import pandas as pd

df = pd.read_csv("../Day_7_23_08_2025/diamonds.csv")
#print(df)

finding_null_data = df.isna().sum() # Find Null Value
#print(finding_null_data)

# df.ffill(inplace=True) # Forward Fill
# print(df)
# df.bfill(inplace=True) # Backward fill
# print(df)

df["price"] = df['price'].fillna(df['price'].mean())
#print(df)
df["x"] = df['x'].fillna(df['price'].mean())
#print(df)

find_null_data = df.isna().sum()
print(find_null_data)
