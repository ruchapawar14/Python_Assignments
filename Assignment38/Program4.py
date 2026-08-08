##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 4
##  Date        : 07/08/2026
##################################################################################

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

# Count Pass and Fail students
counts = df["FinalResult"].value_counts()

# Calculate percentage of Pass and Fail students
percentage = df["FinalResult"].value_counts(normalize=True) * 100

# Display Counts
print("Counts:")
print(counts)

# Display Percentage
print("Percentage:")
print(percentage)