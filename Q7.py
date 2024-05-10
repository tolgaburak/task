import pandas as pd

'''
Code Implementation Task: Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.
'''

data = pd.read_csv("filled_vaccination_numbers.csv")
date = '2021-01-06'
total_vaccinations_on_date = data[data['date'] == date]['daily_vaccinations'].sum()
print(total_vaccinations_on_date)
