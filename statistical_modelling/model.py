import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
data = pd.read_csv("C:\\Users\\wamm1\\Desktop\\midterm\\clean_pop.csv")

# 2. Feature Engineering
data['Urbanization Rate'] = data['Urban Population'] / data['Total Population'] * 100
data = data.sort_values(by=['country', 'year'])
data['Infant Mortality Rate Change'] = data.groupby('country')['Infant Mortality Rate'].diff().fillna(0)
data['Fertility Rate Change'] = data.groupby('country')['Fertility Rate'].diff().fillna(0)

# 3. Scatter plots for relationship visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
sns.scatterplot(data=data, x='Birth Rate', y='Life Expectancy', ax=axes[0, 0], alpha=0.5)
axes[0, 0].set_title('Life Expectancy vs. Birth Rate')
sns.scatterplot(data=data, x='Urbanization Rate', y='Life Expectancy', ax=axes[0, 1], alpha=0.5)
axes[0, 1].set_title('Life Expectancy vs. Urbanization Rate')
sns.scatterplot(data=data, x='Infant Mortality Rate', y='Life Expectancy', ax=axes[1, 0], alpha=0.5)
axes[1, 0].set_title('Life Expectancy vs. Infant Mortality Rate')
sns.scatterplot(data=data, x='Fertility Rate', y='Life Expectancy', ax=axes[1, 1], alpha=0.5)
axes[1, 1].set_title('Life Expectancy vs. Fertility Rate')
plt.tight_layout()
plt.show()