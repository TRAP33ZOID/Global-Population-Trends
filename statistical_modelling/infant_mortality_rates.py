import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
data = pd.read_csv("C:\\Users\\wamm1\\Desktop\\midterm\\clean_pop.csv")

# List of countries for visualization
countries = ['Canada', 'India', 'Kenya', 'Brazil', 'Ukraine']

# Filter data for these countries
selected_countries = data[data['country'].isin(countries)]

# Plot
plt.figure(figsize=(12, 7))
sns.lineplot(data=selected_countries, x='year', y='Infant Mortality Rate', hue='country')
plt.title('Infant Mortality Rate Over the Years')
plt.ylabel('Infant Mortality Rate')
plt.xlabel('Year')
plt.legend(title='Country')
plt.show()
