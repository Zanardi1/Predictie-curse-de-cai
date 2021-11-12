import pandas as pd

raw_data = pd.read_excel('Data.xlsx')
print(raw_data.shape)
print(raw_data.head())

featured_data = raw_data

# Calculez Last FGrating
featured_data['Last FGrating'] = featured_data.groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last Final Position
featured_data['Last Plassering'] = featured_data.groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru Sha-Tin - iarba
featured_data['Last FGrating at Sha-Tin Grass'] = featured_data.groupby(['HorseId', 'Track', 'Surface'])[
    'FGrating'].apply(lambda x: x.shift(1)) if (
                                                       featured_data.Track == 'Sha Tin') & (
                                                           featured_data.Surface == 'Gress') else 2

featured_data.to_excel('Date sortate.xlsx')
