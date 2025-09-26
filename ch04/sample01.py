import pandas as pd

covid_file_name = './data/owid-covid-data.csv'
raw_pd = pd.read_csv(covid_file_name)

# print(type(raw_pd))
print(raw_pd)