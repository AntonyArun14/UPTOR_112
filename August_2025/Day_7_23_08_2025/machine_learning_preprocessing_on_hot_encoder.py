import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("diamonds.csv")
#print(df)

one_hot_encoder_object  = OneHotEncoder(sparse_output=False)
encoder_result = one_hot_encoder_object.fit_transform(df[['cut']])
#print(encoder_result)

new_df = pd.DataFrame(encoder_result, columns=one_hot_encoder_object.get_feature_names_out())
#print(new_df)

final_df = pd.concat([df, new_df], axis=1)
final_df.drop("cut",axis=1, inplace=True)
print(final_df)
