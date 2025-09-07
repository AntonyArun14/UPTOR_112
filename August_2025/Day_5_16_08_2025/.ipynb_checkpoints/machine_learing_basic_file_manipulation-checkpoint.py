import  pandas as pd

df = pd.read_csv("diamonds.csv")
print(df)

df.drop(["Unnamed: 0"],axis=1, inplace=True)
print("After Dropping\n", df)

"""axis = 1 is basically to remove on column basis"""
"""inplace = True is basically to update the change in all df """
