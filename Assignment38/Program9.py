##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 9
##  Date        : 07/08/2026
##################################################################################

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

# Create a scatter plot of AssignmentsCompleted and FinalResult

plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")

plt.show()