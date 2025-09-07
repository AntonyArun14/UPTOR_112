import pandas as pd

#pd.set_option('display.max_column', None)
#pd.set_option("display.max_rows",None)
"""Below line is actually to read the csv file from current file """
"""df mean Variable """
"""pd is pandas"""
df = pd.read_csv("../Day_7_23_08_2025/diamonds.csv")
columns_name = df.columns

numeric_columns = []
categorical_columns = []

for col in columns_name:
    if df[col].dtype =="O": #its Capital O for Represent Object
        categorical_columns.append(col)
    else:
        numeric_columns.append(col)

print("Categorical:", categorical_columns)
print("Numeric:", numeric_columns)