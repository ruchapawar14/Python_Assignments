##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 1
##  Date        : 07/08/2026
##################################################################################

import pandas as pd 

Border = "-"*90

df = pd.read_csv("student_performance_ml.csv")

print("--------Student Performance Dataset--------")

# First 5 records
print(Border)
print("First 5 Records")
print(df.head())
print(Border)

# Last 5 records
print("Last 5 Records")
print(df.tail())
print(Border)

# Shape
print("Total number of rows and columns:")
print(df.shape)
print(Border)

# Column Names
print("List of column names:")
print(df.columns)
print(Border)

# Data Types
print("Data Types of each column:")
print(df.dtypes)
print(Border)