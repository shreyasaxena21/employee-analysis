# employee_performance_analysis.py
# Author: 22f3001013@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# -----------------------------
# 1. Load Employee Dataset
# -----------------------------
# Save your dataset as employee_data.csv before running this script
df = pd.read_csv("employee_data.csv")

# -----------------------------
# 2. Frequency count of Finance
# -----------------------------
finance_count = df["department"].value_counts().get("Finance", 0)
print("Frequency count for Finance Department:", finance_count)

# -----------------------------
# 3. Histogram of Departments
# -----------------------------
plt.figure(figsize=(8, 5))
df["department"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.tight_layout()

# -----------------------------
# 4. Save as HTML
# -----------------------------
html_file = "employee_performance_analysis.html"
mpld3.save_html(plt.gcf(), html_file)

print(f"✅ Analysis complete. HTML file saved as {html_file}")
