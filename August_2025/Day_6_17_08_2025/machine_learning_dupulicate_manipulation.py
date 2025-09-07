import pandas as pd
df = pd.read_csv("../Day_7_23_08_2025/diamonds.csv")
print(df)
# '''below code is basically to find any duplicates in the rows  '''
# finding_duplicates  = df[df.duplicated()]
# print(finding_duplicates)
#
# print("-------------------------------------------------------------")
# df.drop_duplicates(inplace=True)
# print(df)
# print("after the removel \n -------------------------------------------------------------")
#
# finding_duplicates  = df[df.duplicated()]
# print(finding_duplicates)
'''Below code has additional attribute keep = false will include original '''
finding_duplicates  = df[df.duplicated(keep=False)]
print(finding_duplicates)
'''Below code has additional attribute keep = last  will include as original '''
finding_duplicates  = df[df.duplicated(keep="last")]
print(finding_duplicates)

"""
1. Arun
2. Arun
3. Arun

Condition 1: df[df.duplicated()]
2. Arun
3. Arun
Condition 2: df[df.duplicated(keep=False)]
1. Arun
2. Arun
3. Arun
Condition 1: df[df.duplicated(keep-"last")]
1. Arun
2. Arun

"""

finding_duplicates  = df[df.duplicated()]
print(finding_duplicates)

print("-------------------------------------------------------------")
df.drop_duplicates(keep="False", inplace=True)
print(df)
print("after the removel \n -------------------------------------------------------------")

finding_duplicates  = df[df.duplicated()]
print(finding_duplicates)