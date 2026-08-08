##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 3
##  Date        : 07/08/2026
##################################################################################

import pandas as pd 

df = pd.read_csv("student_performance_ml.csv")

# Average StudyHours
print("Average Study Hours:", df["StudyHours"].mean())

# Average Attendance
print("Average Attendance:", df["Attendance"].mean())

# Maximum PreviousScore
print("Maximum Previous Score:", df["PreviousScore"].max())

# Minimum SleepHours
print("Minimum Sleep Hours:", df["SleepHours"].min())