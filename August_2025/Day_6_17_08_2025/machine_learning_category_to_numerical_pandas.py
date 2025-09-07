import numpy as np
import pandas as pd

df = pd.read_csv("../Day_7_23_08_2025/diamonds.csv")
print(df)

cut_detailing = df['cut'].unique()
print(cut_detailing)

#['Ideal' 'Premium' 'Good' 'Very Good' 'Fair']

# df['cut'] = df['cut'].map({"Good":1,"Premium":4,"Fair":3,"Ideal":2,"Very Good":8 })
# print(df)

df['cut'] = df['cut'].map({"Good":1,"Premium":4,"Fair":3,"Ideal":2,"Very Good":8 })
print(df)