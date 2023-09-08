import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

# 1. Load the data
data = pd.read_csv("C:\\Users\\wamm1\\Desktop\\midterm\\clean_pop.csv")

# 2. Feature Engineering
data['Urbanization Rate'] = data['Urban Population'] / data['Total Population'] * 100
data = data.sort_values(by=['country', 'year'])
data['Infant Mortality Rate Change'] = data.groupby('country')['Infant Mortality Rate'].diff().fillna(0)
data['Fertility Rate Change'] = data.groupby('country')['Fertility Rate'].diff().fillna(0)

# 3. Imputation of missing values
X = data[['Birth Rate', 'Urbanization Rate', 'Infant Mortality Rate', 'Fertility Rate']]
y = data['Life Expectancy']

X['Urbanization Rate'].fillna(X['Urbanization Rate'].median(), inplace=True)
X['Infant Mortality Rate'].fillna(X['Infant Mortality Rate'].median(), inplace=True)
X['Fertility Rate'].fillna(X['Fertility Rate'].median(), inplace=True)
y.fillna(y.median(), inplace=True)

# 4. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Regression analysis
X_train_const = sm.add_constant(X_train)  # Adding a constant for the intercept
model = sm.OLS(y_train, X_train_const).fit()

# Print model summary
print(model.summary())
