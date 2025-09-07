import pandas as pd
df = pd.read_csv("diamonds.csv")
#print(df)
encoded_df = pd.get_dummies((df['cut']))
print(encoded_df)

final_df  = pd.concat([df, encoded_df], axis=1)
final_df.drop('cut', axis=0, inplace=True)
print(final_df)


