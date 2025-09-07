import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Year" : [2000, 2001, 2002, 2003, 2004, 2005, 2006,2007, 2008, 2009],
    "bedroom" : [2,3,2,3,2,3,2,3,2,3],
    "Price" : [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
}

df = pd.DataFrame(data)
print(df)
print(type(df))

x = df[["Year","bedroom"]]
y = df['Price']

model = LinearRegression()
model.fit(x, y)

year_for_prediction = {"Year" : [2010, 2011],"bedroom" :[2, 3]}
predictive_df = pd.DataFrame(year_for_prediction)

predictive_df["Price"] = model.predict(predictive_df)
print(predictive_df["Price"])

final_df = pd.concat([df, predictive_df], ignore_index= True)
print(final_df)