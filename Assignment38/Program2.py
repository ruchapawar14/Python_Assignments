##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 2
##  Date        : 07/08/2026
##################################################################################

import pandas as pd 

df = pd.read_csv("student_performance_ml.csv")

print("--------Student Performance Dataset--------")

# Total number of students
print("Total number of students :",len(df))

# Count how many students passed (FinalResult = 1)
print("Total number of passed students :", (df["FinalResult"] == 1).sum())

# Count how many students failed (FinalResult = 0)
print("Total number of failed students :", (df["FinalResult"] == 0).sum())