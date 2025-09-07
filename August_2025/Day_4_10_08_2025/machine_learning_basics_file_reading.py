import pandas as pd

#pd.set_option('display.max_column', None)
#pd.set_option("display.max_rows",None)
"""Below line is actually to read the csv file from current file """
"""df mean Variable """
"""pd is pandas"""
df = pd.read_csv("../Day_7_23_08_2025/diamonds.csv")
print(df)
"""Below line is actually to read only the column names """
#columns = df.columns
# print(columns)
"""Below line is to ready the data types of the given dataset"""
#column_data_types = df.dtypes
#print(column_data_types)
"""Below line is to get the general information about the dataset """
#df_information = df.info()
#print("df_information")
"""Below function will work only numerical columns"""
#df_description = df.describe()
#print(df_description)
"""reading a single column and its data """
# data = df["carat"]
# print(data)
"""reading more then one column data """
# data = df[["carat","cut"]]
# print(data)
"""reading first 5 number of rows"""
# data = df.head()
# print(data)
"""reading last 5 number of rows"""
# data = df.tail()
# print(data)
"""reading first specific  number of rows"""
# data = df.head(10)
# print(data)
"""below concept is called slicing that cuts the rows in the given numeric order """
# data = df[10:20] # its will return rows from 10 to 20
# print(data)
"""Locator function that returns all the specified number rows"""
# data = df.loc[10:20] # its will return rows from 10 to 20
# print(data)
"""Locator function that returns all the specified number rows with column"""
# data = df.loc[10:20, "carat"] # its will return rows from 10 to 20
# print(data)

# data = df.loc[10:20, ["carat","cut"]] # its will return rows from 10 to 20
# print(data)
""" i Locator function (only numeric row and column name )that returns all the specified number rows with column """
# data = df.iloc[10:20,0:3] # its will return rows from 10 to 20
# print(data)

# data = df.iloc[10:20,[1,5,7]] # its will return rows from 10 to 20
# print(data)

data_type = df['carat'].dtype # its will return rows from 10 to 20
print(data_type)