import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    "Year" : [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009],
    "Price": [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
}

df = pd.DataFrame(data)
print(df)
print(type(df))

x = df[["Year"]]
y = df['Price']

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8, random_state=42)   # or test_size = 0.2


model = LinearRegression()
model.fit(x_train, y_train)

prediction = model.predict(x_test)
print(x_test)
print(prediction)

from sklearn.metrics import r2_score
final_accuracy_testing = r2_score(y_test, prediction)
print(final_accuracy_testing)