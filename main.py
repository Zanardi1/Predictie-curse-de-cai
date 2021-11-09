import pandas as pd

raw_data = pd.read_excel('Data.xlsx')
# print(raw_data.shape)
# print(raw_data.head())
# print(raw_data.isnull().any(axis=1))

horse_data = pd.DataFrame()
horse_data['Horse ID'] = raw_data['HorseId'].unique()
# horse_data['Last FGRating'] = raw_data['FGrating']
print(horse_data.shape)
print(horse_data.head())
