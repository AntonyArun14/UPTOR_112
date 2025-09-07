import pandas as pd
from sklearn.impute import SimpleImputer
'''pip install scikit-learn'''
df = pd.read_csv("../Day_7_23_08_2025/diamonds.csv")
print(df)

# simple_imputer_object = SimpleImputer()
# df['price'] = simple_imputer_object.fit_transform(df[['price']])
# print(df)

"""Simple imputer is only fot numerical data so below code will fail"""
# simple_imputer_object = SimpleImputer()
# df['cut'] = simple_imputer_object.fit_transform(df[['cut']])
# print(df)


# simple_imputer_object = SimpleImputer(strategy="most_frequent")
# df['price'] = simple_imputer_object.fit_transform(df[['price']])
# print(df)

simple_imputer_object = SimpleImputer(strategy="constant", fill_value=100)
df['price'] = simple_imputer_object.fit_transform(df[['price']])
print(df)


