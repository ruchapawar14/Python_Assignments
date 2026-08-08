##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 38
##  Question    : 6
##  Date        : 07/08/2026
##################################################################################

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

# Plot histogram of StudyHours
plt.hist(df["StudyHours"], bins=10)

# Add title
plt.title("Histogram of Study Hours")

# Add X-axis label
plt.xlabel("Study Hours")

# Add Y-axis label
plt.ylabel("Number of Students")

# Display the histogram
plt.show()