import pandas as pd
import os

covid_file_name = '../ch04/data/owid-covid-data.csv'
raw_df = pd.read_csv(covid_file_name, sep=',')

selected_columns = ['iso_code','location','date','total_cases','population']
selected_df = raw_df[selected_columns]
print('='*50)
print(selected_df.head())

kor_df = selected_df[selected_df['location'] == 'South Korea']
print('='*50)
print(kor_df)

#date컬럼을 index로 지정
index_name = 'date'
kor_index_df = kor_df.set_index(index_name)
print('='*50)
print(kor_index_df.head())

#대한민국코로나데이터 저장(csv -> covid_kor.csv)
kor_covid_file_name = './data/covid_kor.csv'
if os.path.exists(kor_covid_file_name):
    os.remove(kor_covid_file_name)
kor_index_df.to_csv(kor_covid_file_name)
#kor_index_df.to_csv(kor_covid_file_name, sep='|', encoding='utf-8')
#kor_index_df.to_csv(kor_covid_file_name, encoding='utf-8', sep='|')

#미국 코로나 발생 데이터 -> df(usa_index_df)
# -> 실습!!!!
usa_df = selected_df[selected_df['iso_code'] == 'USA']
print('='*50)
print(usa_df.head())

#usa데이터에 index지정
usa_index_df = usa_df.set_index(index_name)
print('='*50)
print(usa_index_df.head())

usa_covid_file_name = './data/covid_usa.csv'
if os.path.exists(usa_covid_file_name):
    os.remove(usa_covid_file_name)
usa_index_df.to_csv(usa_covid_file_name)