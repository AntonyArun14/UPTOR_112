import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("diamonds.csv")
#print(df)

std_scaler_obj = StandardScaler()
#df["price"] = std_scaler_obj.fit_transform(df[['price']])
df["converted_price"] = std_scaler_obj.fit_transform(df[['price']])
print(df[['price','converted_price']])