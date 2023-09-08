import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data into a DataFrame
data = pd.read_csv("C:\\Users\\wamm1\\Desktop\\midterm\\clean_pop.csv")

# Filter the dataset to identify countries with negative growth rates
negative_growth_data = data[data["Growth Rate"] < 0]

# Create a bar plot to visualize negative growth rates by country and year
plt.figure(figsize=(15, 10))
sns.barplot(data=negative_growth_data, x="country", y="Growth Rate", hue="year", palette="viridis")
plt.title("Countries with Negative Growth Rates (2016-2022)")
plt.ylabel("Growth Rate (%)")
plt.xlabel("Country")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Year")
plt.tight_layout()
plt.savefig("Negative_Growth_Rates.png")
plt.show()
