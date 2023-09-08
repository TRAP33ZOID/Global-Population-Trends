import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data into a DataFrame
data = pd.read_csv("C:\\Users\\wamm1\\Desktop\\midterm\\clean_pop.csv")

# Filter the dataset for Canada
canada_data = data[data["country"] == "Canada"]

# Plotting the urban vs. rural growth for Canada
plt.figure(figsize=(12, 7))
plt.plot(canada_data["year"], canada_data["Urban Population"], label="Urban Population", marker='o', linestyle='-')
plt.plot(canada_data["year"], canada_data["Rural Population"], label="Rural Population", marker='o', linestyle='--')
plt.title("Urban vs. Rural Population Growth for Canada (2016-2022)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.savefig("Canada_Urban_vs_Rural_Population_Growth.png")
plt.show()
