
import csv
import random



data = [['"Name"', '"Tamil"', '"Maths"', '"Science"', '"English"', '"History"', '"Geography"', '"Social-Science"', '"Percentage']]
names = ['"Ravi"', '"Priya"', '"Amit"', '"Sonia"', '"Kiran"', '"Vivek"', '"Anjali"', '"Ramesh"', '"Lakshmi"',
    '"Manoj"', '"Seema"', '"Rajesh"', '"Pooja"', '"Arjun"', '"Neha"', '"Suresh"', '"Geeta"', '"Rahul"',
    '"Swati"', '"Vinay"', '"Deepa"', '"Asha"', '"Nitin"', '"Rekha"', '"Sunil"']
 
for name in names:
    tamil = random.randint(40,100)
    maths = random.randint(40,100)
    science = random.randint(40,100)
    english = random.randint(40,100)
    history = random.randint(40,100)
    geography = random.randint(40,100)
    social_science = random.randint(40,100)
    percentage = round(random.uniform(40.0,100.0), 2)
    data.append([name, tamil, maths, science, english, history, geography, social_science, percentage])

with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print("✅students.csv with 25 students created!")

import pandas as pd

"""BELOW LINE HELPS YOU READ THE REQUESTED CSV FILE"""
df = pd.read_csv("students.csv")
#print(df.head())

pd.set_option("display.max_columns", None)

#df = pd.read_csv"students.csv"

#print(df)
#print("---------------------------------------")

"""BELOW LINE HELPS YOU READ THE COLUMN NAMES OF THE REQUESTED FILE"""
columns = df.columns
#print(columns)
#print("----------------------------------------")

"""BELOW LINES ARE TO READ THE DATA TYPES OF THE GIVEN DATASET"""
column_data_types = df.dtypes
print(column_data_types)

"""BELOW LINES ARE TO GET THE GENERAL INFORMATION ABOUT THE DATASET """
df_information = df.info()
print(df_information)