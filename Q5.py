import pandas as pd

'''
Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.  
Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero). 
'''

data = pd.read_csv("daily_vaccination_numbers.csv")
min_vaccinations = data.groupby('country')['daily_vaccinations'].min().reset_index()
data = pd.merge(data, min_vaccinations, on='country', suffixes=('', '_min'))
data['daily_vaccinations'] = data['daily_vaccinations'].fillna(data['daily_vaccinations_min'])
data['daily_vaccinations'] = data['daily_vaccinations'].fillna(0)
data.to_csv("filled_vaccination_numbers2.csv", index=False)
