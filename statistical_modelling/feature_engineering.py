import pandas as pd

# Read the provided CSV file
data = pd.read_csv("C:\\Users\\wamm1\\Desktop\\midterm\\clean_pop.csv")


# Calculate the urbanization rate
data['Urbanization Rate'] = data['Urban Population'] / data['Total Population'] * 100
print("Urbanization Rate for the first few rows:")
print(data[['country', 'year', 'Urbanization Rate']].head())

# Ensure data is sorted by country and year for accurate calculations
data = data.sort_values(by=['country', 'year'])

# Calculate yearly change for Infant Mortality Rate and Fertility Rate
data['Infant Mortality Rate Change'] = data.groupby('country')['Infant Mortality Rate'].diff().fillna(0)
data['Fertility Rate Change'] = data.groupby('country')['Fertility Rate'].diff().fillna(0)

print("\nYearly change in Infant Mortality Rate and Fertility Rate for the first few rows:")
print(data[['country', 'year', 'Infant Mortality Rate', 'Infant Mortality Rate Change', 'Fertility Rate', 'Fertility Rate Change']].head(10))
data.to_csv('featured_pop_data.csv', index=False)