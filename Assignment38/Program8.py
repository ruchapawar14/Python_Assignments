##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 8
##  Date        : 07/08/2026
##################################################################################import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

# Draw the boxplot for Attendance

plt.boxplot(df["Attendance"])

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")

plt.show()