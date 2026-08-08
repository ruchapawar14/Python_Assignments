##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 5
##  Date        : 07/08/2026
##################################################################################

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

# Calculate average StudyHours for Passed students
study_hours_pass = df[df["FinalResult"] == 1]["StudyHours"].mean()
print("Average Study Hours for Passed Students:", study_hours_pass)


# Calculate average StudyHours for Failed students
study_hours_fail = df[df["FinalResult"] == 0]["StudyHours"].mean()
print("Average Study Hours for Failed Students:", study_hours_fail)


# Calculate average Attendance for Passed students
attendance_pass = df[df["FinalResult"] == 1]["Attendance"].mean()
print("\nAverage Attendance for Passed Students:", attendance_pass)

# Calculate average Attendance for Failed students
attendance_fail = df[df["FinalResult"] == 0]["Attendance"].mean()
print("Average Attendance for Failed Students:", attendance_fail)