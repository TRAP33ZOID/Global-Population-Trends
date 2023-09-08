import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("C:\\Users\\wamm1\\Desktop\\midterm\\clean_pop.csv")
latest_year = data['year'].max()
latest_year_data = data[data['year'] == latest_year]

plt.figure(figsize=(12, 6))
plt.scatter(latest_year_data['Life Expectancy'], latest_year_data['Birth Rate'], color='blue')
plt.title(f'Life Expectancy vs. Birth Rates ({latest_year})')
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Birth Rate (per 1,000 population)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
