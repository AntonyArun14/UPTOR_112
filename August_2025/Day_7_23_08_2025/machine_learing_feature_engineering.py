import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("diamonds.csv")
#print(df)

# l_e = LabelEncoder()
# df['cut'] = l_e.fit_transform(df['cut'])
# print(df)
#
# print(l_e.classes_) # find classs

o_e = OrdinalEncoder()
df['cut'] = o_e.fit_transform(df[['cut']])
print(df)

print(o_e.categories_)