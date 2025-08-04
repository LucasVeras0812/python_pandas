import pandas as pd

titanic = pd.read_excel('data/titanic.xlsx')

print(titanic.head())

ages = titanic['Age']

print(ages.head())

print(type(titanic['Age']))

age_sex = titanic[['Age', 'Sex']]
print(age_sex.head())
print(type(titanic[['Age', 'Sex']]))

above_35 = titanic[titanic['Age'] > 35]

print(above_35.head())

class_23 = titanic[titanic['Pclass'].isin([2, 3])]

print(class_23.head())

age_no_na = titanic[titanic['Age'].notna()]

print(age_no_na.head())

adult_names = titanic.loc[titanic['Age'] > 35, 'Name']

print(adult_names.head())

print(titanic.iloc[9:25, 2:5])

titanic.iloc[0:3, 3] = 'anonymous'

import pandas._testing as tm