import pandas as pd

'''
Code Implementation Task: Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.
'''


data = pd.read_csv("filled_vaccination_numbers.csv")
median_vaccinations = data.groupby('country')['daily_vaccinations'].median().reset_index()
top_3_countries = median_vaccinations.nlargest(3, 'daily_vaccinations')
print("Top 3 countries with highest median daily vaccination numbers:")
print(top_3_countries)
