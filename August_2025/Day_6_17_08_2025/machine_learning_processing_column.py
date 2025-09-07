import pandas as pd

df = pd.read_csv("house_price_bd.csv")
#print(df)

df.drop(['Title','Location'], axis=1, inplace=True)
#print(df)

print(df['Price_in_taka'])

# df['Price_in_taka'] = df['Price_in_taka'].replace({"৳":"",",":""},regex=True).astype(float)
"""Below Code without Numerical remove all others """
df['Price_in_taka'] = df['Price_in_taka'].replace({r"[^\d.]": "",",":""},regex=True).astype(float)
print(df['Price_in_taka'])