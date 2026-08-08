##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 10
##  Date        : 07/08/2026
##################################################################################

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

# Plot SleepHours against FinalResult

plt.scatter(df["SleepHours"], df["FinalResult"])

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")

plt.show()