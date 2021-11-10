import pandas as pd

raw_data = pd.read_excel('Data.xlsx')
# print(raw_data.shape)
# print(raw_data.head())
# print(raw_data.isnull().any(axis=1))


# Creez dataframe-ul cu proprietatile cailor
horse_data = pd.DataFrame()
horse_data['HorseId'] = raw_data['HorseId'].unique()

# Extrag ultimul FGrating pentru fiecare cal
last_fg_rating = raw_data[['HorseId', 'FGrating', 'Dato']]
last_fg_rating = last_fg_rating.loc[last_fg_rating.groupby('HorseId').Dato.idxmax(), :]
last_fg_rating = last_fg_rating.rename(columns={'FGrating': 'Last FGrating'})
horse_data = pd.merge(horse_data, last_fg_rating[['HorseId', 'Last FGrating']], on='HorseId', how='left')
last_fg_rating = pd.DataFrame()
del last_fg_rating

# Extrag ultima pozitie pentru fiecare cal
last_final_position = raw_data[['HorseId', 'Plassering', 'Dato']]
last_final_position = last_final_position.loc[last_final_position.groupby('HorseId').Dato.idxmax(), :]
horse_data = pd.merge(horse_data, last_final_position[['HorseId', 'Plassering']], on='HorseId', how='left')
last_final_position = pd.DataFrame()
del last_final_position

# Extrag ultimul FGrating pentru Sha-Tin - iarba
last_fg_rating_at_sha_tin_gress = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Gress')]
last_fg_rating_at_sha_tin_gress = last_fg_rating_at_sha_tin_gress[['HorseId', 'FGrating', 'Dato']]
last_fg_rating_at_sha_tin_gress = last_fg_rating_at_sha_tin_gress.loc[
                                  last_fg_rating_at_sha_tin_gress.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_sha_tin_gress = last_fg_rating_at_sha_tin_gress.rename(
    columns={'FGrating': 'Last FGrating at Sha-Tin Grass'})
horse_data = pd.merge(horse_data, last_fg_rating_at_sha_tin_gress[['Last FGrating at Sha-Tin Grass', 'HorseId']],
                      on='HorseId', how='left')
last_fg_rating_at_sha_tin_gress = pd.DataFrame()
del last_fg_rating_at_sha_tin_gress

# Extrag ultimul FGrating pentru Sha-Tin - pamant
last_fg_rating_at_sha_tin_dirt = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Dirt')]
last_fg_rating_at_sha_tin_dirt = last_fg_rating_at_sha_tin_dirt[['HorseId', 'FGrating', 'Dato']]
last_fg_rating_at_sha_tin_dirt = last_fg_rating_at_sha_tin_dirt.loc[
                                 last_fg_rating_at_sha_tin_dirt.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_sha_tin_dirt = last_fg_rating_at_sha_tin_dirt.rename(
    columns={'FGrating': 'Last FGrating at Sha-Tin Dirt'})
horse_data = pd.merge(horse_data, last_fg_rating_at_sha_tin_dirt[['Last FGrating at Sha-Tin Dirt', 'HorseId']],
                      on='HorseId', how='left')
last_fg_rating_at_sha_tin_dirt = pd.DataFrame()
del last_fg_rating_at_sha_tin_dirt

# Extrag ultimul FGrating pentru Happy Valley-iarba
last_fg_rating_at_happy_valley_gress = raw_data.loc[(raw_data.Track == 'Happy Valley') & (raw_data.Surface == 'Gress')]
last_fg_rating_at_happy_valley_gress = last_fg_rating_at_happy_valley_gress[['HorseId', 'FGrating', 'Dato']]
last_fg_rating_at_happy_valley_gress = last_fg_rating_at_happy_valley_gress.loc[
                                       last_fg_rating_at_happy_valley_gress.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_happy_valley_gress = last_fg_rating_at_happy_valley_gress.rename(
    columns={'FGrating': 'Last FGrating at Happy Valley Grass'})
horse_data = pd.merge(horse_data,
                      last_fg_rating_at_happy_valley_gress[['Last FGrating at Happy Valley Grass', 'HorseId']],
                      on='HorseId', how='left')
last_fg_rating_at_happy_valley_gress = pd.DataFrame()
del last_fg_rating_at_happy_valley_gress

# Extrag pozitia finala pentru Sha-Tin - iarba
last_final_position_at_sha_tin_gress = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Gress')]
last_final_position_at_sha_tin_gress = last_final_position_at_sha_tin_gress[['HorseId', 'Plassering', 'Dato']]
last_final_position_at_sha_tin_gress = last_final_position_at_sha_tin_gress.loc[
                                       last_final_position_at_sha_tin_gress.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_sha_tin_gress = last_final_position_at_sha_tin_gress.rename(
    columns={'Plassering': 'Last Final Position at Sha Tin Grass'})
horse_data = pd.merge(horse_data,
                      last_final_position_at_sha_tin_gress[['Last Final Position at Sha Tin Grass', 'HorseId']],
                      on='HorseId', how='left')
last_final_position_at_sha_tin_gress = pd.DataFrame()
del last_final_position_at_sha_tin_gress

# Extrag pozitia finala pentru Sha-Tin - pamant
last_final_position_at_sha_tin_dirt = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Dirt')]
last_final_position_at_sha_tin_dirt = last_final_position_at_sha_tin_dirt[['HorseId', 'Plassering', 'Dato']]
last_final_position_at_sha_tin_dirt = last_final_position_at_sha_tin_dirt.loc[
                                      last_final_position_at_sha_tin_dirt.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_sha_tin_dirt = last_final_position_at_sha_tin_dirt.rename(
    columns={'Plassering': 'Last Final Position at Sha Tin Dirt'})
horse_data = pd.merge(horse_data,
                      last_final_position_at_sha_tin_dirt[['Last Final Position at Sha Tin Dirt', 'HorseId']],
                      on='HorseId', how='left')
last_final_position_at_sha_tin_dirt = pd.DataFrame()
del last_final_position_at_sha_tin_dirt

# Extrag pozitia finala pentru Happy Valley - iarba
last_final_position_at_happy_valley_gress = raw_data.loc[
    (raw_data.Track == 'Happy Valley') & (raw_data.Surface == 'Gress')]
last_final_position_at_happy_valley_gress = last_final_position_at_happy_valley_gress[['HorseId', 'Plassering', 'Dato']]
last_final_position_at_happy_valley_gress = last_final_position_at_happy_valley_gress.loc[
                                            last_final_position_at_happy_valley_gress.groupby(
                                                ['HorseId']).Dato.idxmax(), :]
last_final_position_at_happy_valley_gress = last_final_position_at_happy_valley_gress.rename(
    columns={'Plassering': 'Last Final Position at Happy Valley Grass'})
horse_data = pd.merge(horse_data,
                      last_final_position_at_happy_valley_gress[
                          ['Last Final Position at Happy Valley Grass', 'HorseId']],
                      on='HorseId', how='left')
last_final_position_at_happy_valley_gress = pd.DataFrame()
del last_final_position_at_happy_valley_gress

# Extrag ultimul FGrating pentru distanta de 1000 m
last_fg_rating_at_1000 = raw_data.loc[raw_data.Distance == 1000]
last_fg_rating_at_1000 = last_fg_rating_at_1000[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_1000 = last_fg_rating_at_1000.loc[
                         last_fg_rating_at_1000.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_1000 = last_fg_rating_at_1000.rename(columns={'FGrating': 'Last FGrating at 1000'})
horse_data = pd.merge(horse_data, last_fg_rating_at_1000[['HorseId', 'Last FGrating at 1000']],
                      on='HorseId', how='left')
last_fg_rating_at_1000 = pd.DataFrame()
del last_fg_rating_at_1000

# Extrag ultimul FGrating pentru distanta de 1200 m
last_fg_rating_at_1200 = raw_data.loc[raw_data.Distance == 1200]
last_fg_rating_at_1200 = last_fg_rating_at_1200[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_1200 = last_fg_rating_at_1200.loc[
                         last_fg_rating_at_1200.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_1200 = last_fg_rating_at_1200.rename(columns={'FGrating': 'Last FGrating at 1200'})
horse_data = pd.merge(horse_data, last_fg_rating_at_1200[['HorseId', 'Last FGrating at 1200']],
                      on='HorseId', how='left')
last_fg_rating_at_1200 = pd.DataFrame()
del last_fg_rating_at_1200

# Extrag ultimul FGrating pentru distanta de 1400 m
last_fg_rating_at_1400 = raw_data.loc[raw_data.Distance == 1400]
last_fg_rating_at_1400 = last_fg_rating_at_1400[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_1400 = last_fg_rating_at_1400.loc[
                         last_fg_rating_at_1400.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_1400 = last_fg_rating_at_1400.rename(columns={'FGrating': 'Last FGrating at 1400'})
horse_data = pd.merge(horse_data, last_fg_rating_at_1400[['HorseId', 'Last FGrating at 1400']],
                      on='HorseId', how='left')
last_fg_rating_at_1400 = pd.DataFrame()
del last_fg_rating_at_1400

# Extrag ultimul FGrating pentru distanta de 1600 m
last_fg_rating_at_1600 = raw_data.loc[raw_data.Distance == 1600]
last_fg_rating_at_1600 = last_fg_rating_at_1600[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_1600 = last_fg_rating_at_1600.loc[
                         last_fg_rating_at_1600.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_1600 = last_fg_rating_at_1600.rename(columns={'FGrating': 'Last FGrating at 1600'})
horse_data = pd.merge(horse_data, last_fg_rating_at_1600[['HorseId', 'Last FGrating at 1600']],
                      on='HorseId', how='left')
last_fg_rating_at_1600 = pd.DataFrame()
del last_fg_rating_at_1600

# Extrag ultimul FGrating pentru distanta de 1650 m
last_fg_rating_at_1650 = raw_data.loc[raw_data.Distance == 1650]
last_fg_rating_at_1650 = last_fg_rating_at_1650[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_1650 = last_fg_rating_at_1650.loc[
                         last_fg_rating_at_1650.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_1650 = last_fg_rating_at_1650.rename(columns={'FGrating': 'Last FGrating at 1650'})
horse_data = pd.merge(horse_data, last_fg_rating_at_1650[['HorseId', 'Last FGrating at 1650']],
                      on='HorseId', how='left')
last_fg_rating_at_1650 = pd.DataFrame()
del last_fg_rating_at_1650

# Extrag ultimul FGrating pentru distanta de 1800 m
last_fg_rating_at_1800 = raw_data.loc[raw_data.Distance == 1800]
last_fg_rating_at_1800 = last_fg_rating_at_1800[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_1800 = last_fg_rating_at_1800.loc[
                         last_fg_rating_at_1800.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_1800 = last_fg_rating_at_1800.rename(columns={'FGrating': 'Last FGrating at 1800'})
horse_data = pd.merge(horse_data, last_fg_rating_at_1800[['HorseId', 'Last FGrating at 1800']],
                      on='HorseId', how='left')
last_fg_rating_at_1800 = pd.DataFrame()
del last_fg_rating_at_1800

# Extrag ultimul FGrating pentru distanta de 2000 m
last_fg_rating_at_2000 = raw_data.loc[raw_data.Distance == 2000]
last_fg_rating_at_2000 = last_fg_rating_at_2000[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_2000 = last_fg_rating_at_2000.loc[
                         last_fg_rating_at_2000.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_2000 = last_fg_rating_at_2000.rename(columns={'FGrating': 'Last FGrating at 2000'})
horse_data = pd.merge(horse_data, last_fg_rating_at_2000[['HorseId', 'Last FGrating at 2000']],
                      on='HorseId', how='left')
last_fg_rating_at_2000 = pd.DataFrame()
del last_fg_rating_at_2000

# Extrag ultimul FGrating pentru distanta de 2200 m
last_fg_rating_at_2200 = raw_data.loc[raw_data.Distance == 2200]
last_fg_rating_at_2200 = last_fg_rating_at_2200[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_2200 = last_fg_rating_at_2200.loc[
                         last_fg_rating_at_2200.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_2200 = last_fg_rating_at_2200.rename(columns={'FGrating': 'Last FGrating at 2200'})
horse_data = pd.merge(horse_data, last_fg_rating_at_2200[['HorseId', 'Last FGrating at 2200']],
                      on='HorseId', how='left')
last_fg_rating_at_2200 = pd.DataFrame()
del last_fg_rating_at_2200

# Extrag ultimul FGrating pentru distanta de 2400 m
last_fg_rating_at_2400 = raw_data.loc[raw_data.Distance == 2400]
last_fg_rating_at_2400 = last_fg_rating_at_2400[['HorseId', 'Dato', 'FGrating']]
last_fg_rating_at_2400 = last_fg_rating_at_2400.loc[
                         last_fg_rating_at_2400.groupby(['HorseId']).Dato.idxmax(), :]
last_fg_rating_at_2400 = last_fg_rating_at_2400.rename(columns={'FGrating': 'Last FGrating at 2400'})
horse_data = pd.merge(horse_data, last_fg_rating_at_2400[['HorseId', 'Last FGrating at 2400']],
                      on='HorseId', how='left')
last_fg_rating_at_2400 = pd.DataFrame()
del last_fg_rating_at_2400

# Extrag ultima positie finala pentru distanta de 1000 m
last_final_position_at_1000 = raw_data.loc[raw_data.Distance == 1000]
last_final_position_at_1000 = last_final_position_at_1000[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_1000 = last_final_position_at_1000.loc[
                              last_final_position_at_1000.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_1000 = last_final_position_at_1000.rename(
    columns={'Plassering': 'Last final position at 1000'})
horse_data = pd.merge(horse_data, last_final_position_at_1000[['HorseId', 'Last final position at 1000']],
                      on='HorseId', how='left')
last_final_position_at_1000 = pd.DataFrame()
del last_final_position_at_1000

# Extrag ultima positie finala pentru distanta de 1200 m
last_final_position_at_1200 = raw_data.loc[raw_data.Distance == 1200]
last_final_position_at_1200 = last_final_position_at_1200[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_1200 = last_final_position_at_1200.loc[
                              last_final_position_at_1200.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_1200 = last_final_position_at_1200.rename(
    columns={'Plassering': 'Last final position at 1200'})
horse_data = pd.merge(horse_data, last_final_position_at_1200[['HorseId', 'Last final position at 1200']],
                      on='HorseId', how='left')
last_final_position_at_1200 = pd.DataFrame()
del last_final_position_at_1200

# Extrag ultima positie finala pentru distanta de 1400 m
last_final_position_at_1400 = raw_data.loc[raw_data.Distance == 1400]
last_final_position_at_1400 = last_final_position_at_1400[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_1400 = last_final_position_at_1400.loc[
                              last_final_position_at_1400.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_1400 = last_final_position_at_1400.rename(
    columns={'Plassering': 'Last final position at 1400'})
horse_data = pd.merge(horse_data, last_final_position_at_1400[['HorseId', 'Last final position at 1400']],
                      on='HorseId', how='left')
last_final_position_at_1400 = pd.DataFrame()
del last_final_position_at_1400

# Extrag ultima positie finala pentru distanta de 1600 m
last_final_position_at_1600 = raw_data.loc[raw_data.Distance == 1600]
last_final_position_at_1600 = last_final_position_at_1600[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_1600 = last_final_position_at_1600.loc[
                              last_final_position_at_1600.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_1600 = last_final_position_at_1600.rename(
    columns={'Plassering': 'Last final position at 1600'})
horse_data = pd.merge(horse_data, last_final_position_at_1600[['HorseId', 'Last final position at 1600']],
                      on='HorseId', how='left')
last_final_position_at_1600 = pd.DataFrame()
del last_final_position_at_1600

# Extrag ultima positie finala pentru distanta de 1650 m
last_final_position_at_1650 = raw_data.loc[raw_data.Distance == 1650]
last_final_position_at_1650 = last_final_position_at_1650[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_1650 = last_final_position_at_1650.loc[
                              last_final_position_at_1650.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_1650 = last_final_position_at_1650.rename(
    columns={'Plassering': 'Last final position at 1650'})
horse_data = pd.merge(horse_data, last_final_position_at_1650[['HorseId', 'Last final position at 1650']],
                      on='HorseId', how='left')
last_final_position_at_1650 = pd.DataFrame()
del last_final_position_at_1650

# Extrag ultima positie finala pentru distanta de 1800 m
last_final_position_at_1800 = raw_data.loc[raw_data.Distance == 1800]
last_final_position_at_1800 = last_final_position_at_1800[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_1800 = last_final_position_at_1800.loc[
                              last_final_position_at_1800.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_1800 = last_final_position_at_1800.rename(
    columns={'Plassering': 'Last final position at 1800'})
horse_data = pd.merge(horse_data, last_final_position_at_1800[['HorseId', 'Last final position at 1800']],
                      on='HorseId', how='left')
last_final_position_at_1800 = pd.DataFrame()
del last_final_position_at_1800

# Extrag ultima positie finala pentru distanta de 2000 m
last_final_position_at_2000 = raw_data.loc[raw_data.Distance == 2000]
last_final_position_at_2000 = last_final_position_at_2000[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_2000 = last_final_position_at_2000.loc[
                              last_final_position_at_2000.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_2000 = last_final_position_at_2000.rename(
    columns={'Plassering': 'Last final position at 2000'})
horse_data = pd.merge(horse_data, last_final_position_at_2000[['HorseId', 'Last final position at 2000']],
                      on='HorseId', how='left')
last_final_position_at_2000 = pd.DataFrame()
del last_final_position_at_2000

# Extrag ultima positie finala pentru distanta de 2200 m
last_final_position_at_2200 = raw_data.loc[raw_data.Distance == 2200]
last_final_position_at_2200 = last_final_position_at_2200[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_2200 = last_final_position_at_2200.loc[
                              last_final_position_at_2200.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_2200 = last_final_position_at_2200.rename(
    columns={'Plassering': 'Last final position at 2200'})
horse_data = pd.merge(horse_data, last_final_position_at_2200[['HorseId', 'Last final position at 2200']],
                      on='HorseId', how='left')
last_final_position_at_2200 = pd.DataFrame()
del last_final_position_at_2200

# Extrag ultima positie finala pentru distanta de 2400 m
last_final_position_at_2400 = raw_data.loc[raw_data.Distance == 2400]
last_final_position_at_2400 = last_final_position_at_2400[['HorseId', 'Dato', 'Plassering']]
last_final_position_at_2400 = last_final_position_at_2400.loc[
                              last_final_position_at_2400.groupby(['HorseId']).Dato.idxmax(), :]
last_final_position_at_2400 = last_final_position_at_2400.rename(
    columns={'Plassering': 'Last final position at 2400'})
horse_data = pd.merge(horse_data, last_final_position_at_2400[['HorseId', 'Last final position at 2400']],
                      on='HorseId', how='left')
last_final_position_at_2400 = pd.DataFrame()
del last_final_position_at_2400

# Extrag FGrating mediu pentru fiecare cal
average_fg_rating = raw_data[['HorseId', 'FGrating']]
average_fg_rating = average_fg_rating.groupby('HorseId')
average_fg_rating = average_fg_rating.mean()
average_fg_rating = average_fg_rating.rename(columns={'FGrating': 'Average FGrating'})
horse_data = pd.merge(horse_data, average_fg_rating, on='HorseId', how='left')
average_fg_rating = pd.DataFrame()
del average_fg_rating

# Extrag pozitia finala medie pentru fiecare cal
average_final_position = raw_data[['HorseId', 'Plassering']]
average_final_position = average_final_position.groupby('HorseId')
average_final_position = average_final_position.mean()
average_final_position = average_final_position.rename(columns={'Plassering': 'Average Final Position'})
horse_data = pd.merge(horse_data, average_final_position, on='HorseId', how='left')
average_final_position = pd.DataFrame()
del average_final_position

# Extrag FGrating mediu in ultimele 10 starturi
average_fg_rating_last_10 = raw_data[['HorseId', 'FGrating']]
average_fg_rating_last_10 = average_fg_rating_last_10.groupby('HorseId').tail(10).groupby('HorseId').mean()
average_fg_rating_last_10 = average_fg_rating_last_10.rename(
    columns={'FGrating': 'Average FG rating in last 10 starts'})
horse_data = pd.merge(horse_data, average_fg_rating_last_10, on='HorseId', how='left')
del average_fg_rating_last_10

# Extrag pozitia finala in ultimele 10 starturi
average_final_position_last_10 = raw_data[['HorseId', 'Plassering']]
average_final_position_last_10 = average_final_position_last_10.groupby('HorseId').tail(10).groupby('HorseId').mean()
average_final_position_last_10 = average_final_position_last_10.rename(
    columns={'Plassering': 'Average position in last 10 starts'})
horse_data = pd.merge(horse_data, average_final_position_last_10, on='HorseId', how='left')
del average_final_position_last_10

# Extrag FGrating mediu in ultimele 4 starturi
average_fg_rating_last_4 = raw_data[['HorseId', 'FGrating']]
average_fg_rating_last_4 = average_fg_rating_last_4.groupby('HorseId').tail(4).groupby('HorseId').mean()
average_fg_rating_last_4 = average_fg_rating_last_4.rename(
    columns={'FGrating': 'Average FG rating in last 4 starts'})
horse_data = pd.merge(horse_data, average_fg_rating_last_4, on='HorseId', how='left')
del average_fg_rating_last_4

# Extrag pozitia finala in ultimele 4 starturi
average_final_position_last_4 = raw_data[['HorseId', 'Plassering']]
average_final_position_last_4 = average_final_position_last_4.groupby('HorseId').tail(10).groupby('HorseId').mean()
average_final_position_last_4 = average_final_position_last_4.rename(
    columns={'Plassering': 'Average position in last 4 starts'})
horse_data = pd.merge(horse_data, average_final_position_last_4, on='HorseId', how='left')
del average_final_position_last_4

# Extrag FGrating mediu pentru fiecare cal pentru Sha-Tin - iarba
average_fg_rating_sha_tin_grass = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Gress')]
average_fg_rating_sha_tin_grass = average_fg_rating_sha_tin_grass[['HorseId', 'FGrating']]
average_fg_rating_sha_tin_grass = average_fg_rating_sha_tin_grass.groupby('HorseId')
average_fg_rating_sha_tin_grass = average_fg_rating_sha_tin_grass.mean()
average_fg_rating_sha_tin_grass = average_fg_rating_sha_tin_grass.rename(
    columns={'FGrating': 'Average FGrating on Sha-Tin - grass'})
horse_data = pd.merge(horse_data, average_fg_rating_sha_tin_grass, on='HorseId', how='left')
average_fg_rating_sha_tin_grass = pd.DataFrame()
del average_fg_rating_sha_tin_grass

# Extrag FGrating mediu pentru fiecare cal pentru Sha-Tin - pamant
average_fg_rating_sha_tin_dirt = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Dirt')]
average_fg_rating_sha_tin_dirt = average_fg_rating_sha_tin_dirt[['HorseId', 'FGrating']]
average_fg_rating_sha_tin_dirt = average_fg_rating_sha_tin_dirt.groupby('HorseId')
average_fg_rating_sha_tin_dirt = average_fg_rating_sha_tin_dirt.mean()
average_fg_rating_sha_tin_dirt = average_fg_rating_sha_tin_dirt.rename(
    columns={'FGrating': 'Average FGrating on Sha-Tin - dirt'})
horse_data = pd.merge(horse_data, average_fg_rating_sha_tin_dirt, on='HorseId', how='left')
average_fg_rating_sha_tin_dirt = pd.DataFrame()
del average_fg_rating_sha_tin_dirt

# Extrag FGrating mediu pentru fiecare cal pentru Happy Valley - iarba
average_fg_rating_happy_valley_grass = raw_data.loc[(raw_data.Track == 'Happy Valley') & (raw_data.Surface == 'Gress')]
average_fg_rating_happy_valley_grass = average_fg_rating_happy_valley_grass[['HorseId', 'FGrating']]
average_fg_rating_happy_valley_grass = average_fg_rating_happy_valley_grass.groupby('HorseId')
average_fg_rating_happy_valley_grass = average_fg_rating_happy_valley_grass.mean()
average_fg_rating_happy_valley_grass = average_fg_rating_happy_valley_grass.rename(
    columns={'FGrating': 'Average FGrating on Happy Valley - grass'})
horse_data = pd.merge(horse_data, average_fg_rating_happy_valley_grass, on='HorseId', how='left')
average_fg_rating_happy_valley_grass = pd.DataFrame()
del average_fg_rating_happy_valley_grass

# Extrag pozitia finala medie pentru fiecare cal pentru Sha-Tin - iarba
average_final_position_sha_tin_grass = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Gress')]
average_final_position_sha_tin_grass = average_final_position_sha_tin_grass[['HorseId', 'Plassering']]
average_final_position_sha_tin_grass = average_final_position_sha_tin_grass.groupby('HorseId')
average_final_position_sha_tin_grass = average_final_position_sha_tin_grass.mean()
average_final_position_sha_tin_grass = average_final_position_sha_tin_grass.rename(
    columns={'Plassering': 'Average Final Position on Sha-Tin - grass'})
horse_data = pd.merge(horse_data, average_final_position_sha_tin_grass, on='HorseId', how='left')
average_final_position_sha_tin_grass = pd.DataFrame()
del average_final_position_sha_tin_grass

# Extrag pozitia finala medie pentru fiecare cal pentru Sha-Tin - pamant
average_final_position_sha_tin_dirt = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Dirt')]
average_final_position_sha_tin_dirt = average_final_position_sha_tin_dirt[['HorseId', 'Plassering']]
average_final_position_sha_tin_dirt = average_final_position_sha_tin_dirt.groupby('HorseId')
average_final_position_sha_tin_dirt = average_final_position_sha_tin_dirt.mean()
average_final_position_sha_tin_dirt = average_final_position_sha_tin_dirt.rename(
    columns={'Plassering': 'Average Final Position on Sha-Tin - dirt'})
horse_data = pd.merge(horse_data, average_final_position_sha_tin_dirt, on='HorseId', how='left')
average_final_position_sha_tin_dirt = pd.DataFrame()
del average_final_position_sha_tin_dirt

# Extrag pozitia finala medie pentru fiecare cal pentru Happy Valley - iarba
average_final_position_happy_valley_grass = raw_data.loc[
    (raw_data.Track == 'Happy Valley') & (raw_data.Surface == 'Gress')]
average_final_position_happy_valley_grass = average_final_position_happy_valley_grass[['HorseId', 'Plassering']]
average_final_position_happy_valley_grass = average_final_position_happy_valley_grass.groupby('HorseId')
average_final_position_happy_valley_grass = average_final_position_happy_valley_grass.mean()
average_final_position_happy_valley_grass = average_final_position_happy_valley_grass.rename(
    columns={'Plassering': 'Average Final Position on Happy Valley - grass'})
horse_data = pd.merge(horse_data, average_final_position_happy_valley_grass, on='HorseId', how='left')
average_final_position_happy_valley_grass = pd.DataFrame()
del average_final_position_happy_valley_grass

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 1000 m
average_fg_rating_at_1000 = raw_data.loc[raw_data.Distance == 1000]
average_fg_rating_at_1000 = average_fg_rating_at_1000[['HorseId', 'FGrating']]
average_fg_rating_at_1000 = average_fg_rating_at_1000.groupby('HorseId')
average_fg_rating_at_1000 = average_fg_rating_at_1000.mean()
average_fg_rating_at_1000 = average_fg_rating_at_1000.rename(columns={'FGrating': 'Average FGrating at 1000 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_1000, on='HorseId', how='left')
average_fg_rating_at_1000 = pd.DataFrame()
del average_fg_rating_at_1000

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 1200 m
average_fg_rating_at_1200 = raw_data.loc[raw_data.Distance == 1200]
average_fg_rating_at_1200 = average_fg_rating_at_1200[['HorseId', 'FGrating']]
average_fg_rating_at_1200 = average_fg_rating_at_1200.groupby('HorseId')
average_fg_rating_at_1200 = average_fg_rating_at_1200.mean()
average_fg_rating_at_1200 = average_fg_rating_at_1200.rename(columns={'FGrating': 'Average FGrating at 1200 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_1200, on='HorseId', how='left')
average_fg_rating_at_1200 = pd.DataFrame()
del average_fg_rating_at_1200

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 1400 m
average_fg_rating_at_1400 = raw_data.loc[raw_data.Distance == 1400]
average_fg_rating_at_1400 = average_fg_rating_at_1400[['HorseId', 'FGrating']]
average_fg_rating_at_1400 = average_fg_rating_at_1400.groupby('HorseId')
average_fg_rating_at_1400 = average_fg_rating_at_1400.mean()
average_fg_rating_at_1400 = average_fg_rating_at_1400.rename(columns={'FGrating': 'Average FGrating at 1400 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_1400, on='HorseId', how='left')
average_fg_rating_at_1400 = pd.DataFrame()
del average_fg_rating_at_1400

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 1600 m
average_fg_rating_at_1600 = raw_data.loc[raw_data.Distance == 1600]
average_fg_rating_at_1600 = average_fg_rating_at_1600[['HorseId', 'FGrating']]
average_fg_rating_at_1600 = average_fg_rating_at_1600.groupby('HorseId')
average_fg_rating_at_1600 = average_fg_rating_at_1600.mean()
average_fg_rating_at_1600 = average_fg_rating_at_1600.rename(columns={'FGrating': 'Average FGrating at 1600 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_1600, on='HorseId', how='left')
average_fg_rating_at_1600 = pd.DataFrame()
del average_fg_rating_at_1600

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 1650 m
average_fg_rating_at_1650 = raw_data.loc[raw_data.Distance == 1650]
average_fg_rating_at_1650 = average_fg_rating_at_1650[['HorseId', 'FGrating']]
average_fg_rating_at_1650 = average_fg_rating_at_1650.groupby('HorseId')
average_fg_rating_at_1650 = average_fg_rating_at_1650.mean()
average_fg_rating_at_1650 = average_fg_rating_at_1650.rename(columns={'FGrating': 'Average FGrating at 1650 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_1650, on='HorseId', how='left')
average_fg_rating_at_1650 = pd.DataFrame()
del average_fg_rating_at_1650

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 1800 m
average_fg_rating_at_1800 = raw_data.loc[raw_data.Distance == 1800]
average_fg_rating_at_1800 = average_fg_rating_at_1800[['HorseId', 'FGrating']]
average_fg_rating_at_1800 = average_fg_rating_at_1800.groupby('HorseId')
average_fg_rating_at_1800 = average_fg_rating_at_1800.mean()
average_fg_rating_at_1800 = average_fg_rating_at_1800.rename(columns={'FGrating': 'Average FGrating at 1800 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_1800, on='HorseId', how='left')
average_fg_rating_at_1800 = pd.DataFrame()
del average_fg_rating_at_1800

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 2000 m
average_fg_rating_at_2000 = raw_data.loc[raw_data.Distance == 2000]
average_fg_rating_at_2000 = average_fg_rating_at_2000[['HorseId', 'FGrating']]
average_fg_rating_at_2000 = average_fg_rating_at_2000.groupby('HorseId')
average_fg_rating_at_2000 = average_fg_rating_at_2000.mean()
average_fg_rating_at_2000 = average_fg_rating_at_2000.rename(columns={'FGrating': 'Average FGrating at 2000 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_2000, on='HorseId', how='left')
average_fg_rating_at_2000 = pd.DataFrame()
del average_fg_rating_at_2000

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 2200 m
average_fg_rating_at_2200 = raw_data.loc[raw_data.Distance == 2200]
average_fg_rating_at_2200 = average_fg_rating_at_2200[['HorseId', 'FGrating']]
average_fg_rating_at_2200 = average_fg_rating_at_2200.groupby('HorseId')
average_fg_rating_at_2200 = average_fg_rating_at_2200.mean()
average_fg_rating_at_2200 = average_fg_rating_at_2200.rename(columns={'FGrating': 'Average FGrating at 2200 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_2200, on='HorseId', how='left')
average_fg_rating_at_2200 = pd.DataFrame()
del average_fg_rating_at_2200

# Extrag FGrating mediu pentru fiecare cal pentru distanta de 2400 m
average_fg_rating_at_2400 = raw_data.loc[raw_data.Distance == 2400]
average_fg_rating_at_2400 = average_fg_rating_at_2400[['HorseId', 'FGrating']]
average_fg_rating_at_2400 = average_fg_rating_at_2400.groupby('HorseId')
average_fg_rating_at_2400 = average_fg_rating_at_2400.mean()
average_fg_rating_at_2400 = average_fg_rating_at_2400.rename(columns={'FGrating': 'Average FGrating at 2400 m'})
horse_data = pd.merge(horse_data, average_fg_rating_at_2400, on='HorseId', how='left')
average_fg_rating_at_2400 = pd.DataFrame()
del average_fg_rating_at_2400

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 1000 m
average_final_position_at_1000 = raw_data.loc[raw_data.Distance == 1000]
average_final_position_at_1000 = average_final_position_at_1000[['HorseId', 'Plassering']]
average_final_position_at_1000 = average_final_position_at_1000.groupby('HorseId')
average_final_position_at_1000 = average_final_position_at_1000.mean()
average_final_position_at_1000 = average_final_position_at_1000.rename(
    columns={'Plassering': 'Average Final Position at 1000'})
horse_data = pd.merge(horse_data, average_final_position_at_1000, on='HorseId', how='left')
average_final_position_at_1000 = pd.DataFrame()
del average_final_position_at_1000

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 1200 m
average_final_position_at_1200 = raw_data.loc[raw_data.Distance == 1200]
average_final_position_at_1200 = average_final_position_at_1200[['HorseId', 'Plassering']]
average_final_position_at_1200 = average_final_position_at_1200.groupby('HorseId')
average_final_position_at_1200 = average_final_position_at_1200.mean()
average_final_position_at_1200 = average_final_position_at_1200.rename(
    columns={'Plassering': 'Average Final Position at 1200'})
horse_data = pd.merge(horse_data, average_final_position_at_1200, on='HorseId', how='left')
average_final_position_at_1200 = pd.DataFrame()
del average_final_position_at_1200

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 1400 m
average_final_position_at_1400 = raw_data.loc[raw_data.Distance == 1400]
average_final_position_at_1400 = average_final_position_at_1400[['HorseId', 'Plassering']]
average_final_position_at_1400 = average_final_position_at_1400.groupby('HorseId')
average_final_position_at_1400 = average_final_position_at_1400.mean()
average_final_position_at_1400 = average_final_position_at_1400.rename(
    columns={'Plassering': 'Average Final Position at 1400'})
horse_data = pd.merge(horse_data, average_final_position_at_1400, on='HorseId', how='left')
average_final_position_at_1400 = pd.DataFrame()
del average_final_position_at_1400

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 1600 m
average_final_position_at_1600 = raw_data.loc[raw_data.Distance == 1600]
average_final_position_at_1600 = average_final_position_at_1600[['HorseId', 'Plassering']]
average_final_position_at_1600 = average_final_position_at_1600.groupby('HorseId')
average_final_position_at_1600 = average_final_position_at_1600.mean()
average_final_position_at_1600 = average_final_position_at_1600.rename(
    columns={'Plassering': 'Average Final Position at 1600'})
horse_data = pd.merge(horse_data, average_final_position_at_1600, on='HorseId', how='left')
average_final_position_at_1600 = pd.DataFrame()
del average_final_position_at_1600

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 1650 m
average_final_position_at_1650 = raw_data.loc[raw_data.Distance == 1650]
average_final_position_at_1650 = average_final_position_at_1650[['HorseId', 'Plassering']]
average_final_position_at_1650 = average_final_position_at_1650.groupby('HorseId')
average_final_position_at_1650 = average_final_position_at_1650.mean()
average_final_position_at_1650 = average_final_position_at_1650.rename(
    columns={'Plassering': 'Average Final Position at 1650'})
horse_data = pd.merge(horse_data, average_final_position_at_1650, on='HorseId', how='left')
average_final_position_at_1650 = pd.DataFrame()
del average_final_position_at_1650

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 1800 m
average_final_position_at_1800 = raw_data.loc[raw_data.Distance == 1800]
average_final_position_at_1800 = average_final_position_at_1800[['HorseId', 'Plassering']]
average_final_position_at_1800 = average_final_position_at_1800.groupby('HorseId')
average_final_position_at_1800 = average_final_position_at_1800.mean()
average_final_position_at_1800 = average_final_position_at_1800.rename(
    columns={'Plassering': 'Average Final Position at 1800'})
horse_data = pd.merge(horse_data, average_final_position_at_1800, on='HorseId', how='left')
average_final_position_at_1800 = pd.DataFrame()
del average_final_position_at_1800

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 2000 m
average_final_position_at_2000 = raw_data.loc[raw_data.Distance == 2000]
average_final_position_at_2000 = average_final_position_at_2000[['HorseId', 'Plassering']]
average_final_position_at_2000 = average_final_position_at_2000.groupby('HorseId')
average_final_position_at_2000 = average_final_position_at_2000.mean()
average_final_position_at_2000 = average_final_position_at_2000.rename(
    columns={'Plassering': 'Average Final Position at 2000'})
horse_data = pd.merge(horse_data, average_final_position_at_2000, on='HorseId', how='left')
average_final_position_at_2000 = pd.DataFrame()
del average_final_position_at_2000

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 2200 m
average_final_position_at_2200 = raw_data.loc[raw_data.Distance == 2200]
average_final_position_at_2200 = average_final_position_at_2200[['HorseId', 'Plassering']]
average_final_position_at_2200 = average_final_position_at_2200.groupby('HorseId')
average_final_position_at_2200 = average_final_position_at_2200.mean()
average_final_position_at_2200 = average_final_position_at_2200.rename(
    columns={'Plassering': 'Average Final Position at 2200'})
horse_data = pd.merge(horse_data, average_final_position_at_2200, on='HorseId', how='left')
average_final_position_at_2200 = pd.DataFrame()
del average_final_position_at_2200

# Extrag pozitia finala medie pentru fiecare cal pentru distanta de 2400 m
average_final_position_at_2400 = raw_data.loc[raw_data.Distance == 2400]
average_final_position_at_2400 = average_final_position_at_2400[['HorseId', 'Plassering']]
average_final_position_at_2400 = average_final_position_at_2400.groupby('HorseId')
average_final_position_at_2400 = average_final_position_at_2400.mean()
average_final_position_at_2400 = average_final_position_at_2400.rename(
    columns={'Plassering': 'Average Final Position at 2400'})
horse_data = pd.merge(horse_data, average_final_position_at_2400, on='HorseId', how='left')
average_final_position_at_2400 = pd.DataFrame()
del average_final_position_at_2400

# Extrag maximul FGRating pentru fiecare cal in parte
max_fg_rating = raw_data[raw_data.FGrating == raw_data.groupby(['HorseId'])['FGrating'].transform(max)]
max_fg_rating = max_fg_rating[['FGrating', 'HorseId']].drop_duplicates()
max_fg_rating = max_fg_rating.rename(columns={'FGrating': 'Max FGrating'})
horse_data = pd.merge(horse_data, max_fg_rating[['HorseId', 'Max FGrating']], on='HorseId', how='left')
max_fg_rating = pd.DataFrame()
del max_fg_rating

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 1000 m
max_fg_rating_at_1000 = raw_data.loc[raw_data.Distance == 1000]
max_fg_rating_at_1000 = max_fg_rating_at_1000.loc[
    max_fg_rating_at_1000.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_1000 = max_fg_rating_at_1000.rename(
    columns={'FGrating': 'Max FGrating at 1000'})
horse_data = pd.merge(horse_data, max_fg_rating_at_1000[['HorseId', 'Max FGrating at 1000']],
                      on='HorseId', how='left')
max_fg_rating_at_1000 = pd.DataFrame()
del max_fg_rating_at_1000

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 1200 m
max_fg_rating_at_1200 = raw_data.loc[raw_data.Distance == 1200]
max_fg_rating_at_1200 = max_fg_rating_at_1200.loc[
    max_fg_rating_at_1200.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_1200 = max_fg_rating_at_1200.rename(
    columns={'FGrating': 'Max FGrating at 1200'})
horse_data = pd.merge(horse_data, max_fg_rating_at_1200[['HorseId', 'Max FGrating at 1200']],
                      on='HorseId', how='left')
max_fg_rating_at_1200 = pd.DataFrame()
del max_fg_rating_at_1200

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 1400 m
max_fg_rating_at_1400 = raw_data.loc[raw_data.Distance == 1400]
max_fg_rating_at_1400 = max_fg_rating_at_1400.loc[
    max_fg_rating_at_1400.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_1400 = max_fg_rating_at_1400.rename(
    columns={'FGrating': 'Max FGrating at 1400'})
horse_data = pd.merge(horse_data, max_fg_rating_at_1400[['HorseId', 'Max FGrating at 1400']],
                      on='HorseId', how='left')
max_fg_rating_at_1400 = pd.DataFrame()
del max_fg_rating_at_1400

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 1600 m
max_fg_rating_at_1600 = raw_data.loc[raw_data.Distance == 1600]
max_fg_rating_at_1600 = max_fg_rating_at_1600.loc[
    max_fg_rating_at_1600.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_1600 = max_fg_rating_at_1600.rename(
    columns={'FGrating': 'Max FGrating at 1600'})
horse_data = pd.merge(horse_data, max_fg_rating_at_1600[['HorseId', 'Max FGrating at 1600']],
                      on='HorseId', how='left')
max_fg_rating_at_1600 = pd.DataFrame()
del max_fg_rating_at_1600

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 1650 m
max_fg_rating_at_1650 = raw_data.loc[raw_data.Distance == 1650]
max_fg_rating_at_1650 = max_fg_rating_at_1650.loc[
    max_fg_rating_at_1650.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_1650 = max_fg_rating_at_1650.rename(
    columns={'FGrating': 'Max FGrating at 1650'})
horse_data = pd.merge(horse_data, max_fg_rating_at_1650[['HorseId', 'Max FGrating at 1650']],
                      on='HorseId', how='left')
max_fg_rating_at_1650 = pd.DataFrame()
del max_fg_rating_at_1650

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 1800 m
max_fg_rating_at_1800 = raw_data.loc[raw_data.Distance == 1800]
max_fg_rating_at_1800 = max_fg_rating_at_1800.loc[
    max_fg_rating_at_1800.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_1800 = max_fg_rating_at_1800.rename(
    columns={'FGrating': 'Max FGrating at 1800'})
horse_data = pd.merge(horse_data, max_fg_rating_at_1800[['HorseId', 'Max FGrating at 1800']],
                      on='HorseId', how='left')
max_fg_rating_at_1800 = pd.DataFrame()
del max_fg_rating_at_1800

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 2000 m
max_fg_rating_at_2000 = raw_data.loc[raw_data.Distance == 2000]
max_fg_rating_at_2000 = max_fg_rating_at_2000.loc[
    max_fg_rating_at_2000.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_2000 = max_fg_rating_at_2000.rename(
    columns={'FGrating': 'Max FGrating at 2000'})
horse_data = pd.merge(horse_data, max_fg_rating_at_2000[['HorseId', 'Max FGrating at 2000']],
                      on='HorseId', how='left')
max_fg_rating_at_2000 = pd.DataFrame()
del max_fg_rating_at_2000

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 2200 m
max_fg_rating_at_2200 = raw_data.loc[raw_data.Distance == 2200]
max_fg_rating_at_2200 = max_fg_rating_at_2200.loc[
    max_fg_rating_at_2200.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_2200 = max_fg_rating_at_2200.rename(
    columns={'FGrating': 'Max FGrating at 2200'})
horse_data = pd.merge(horse_data, max_fg_rating_at_2200[['HorseId', 'Max FGrating at 2200']],
                      on='HorseId', how='left')
max_fg_rating_at_2200 = pd.DataFrame()
del max_fg_rating_at_2200

# Extrag maximul FGRating pentru fiecare cal in parte pe distanta de 2400 m
max_fg_rating_at_2400 = raw_data.loc[raw_data.Distance == 2400]
max_fg_rating_at_2400 = max_fg_rating_at_2400.loc[
    max_fg_rating_at_2400.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating']]
max_fg_rating_at_2400 = max_fg_rating_at_2400.rename(
    columns={'FGrating': 'Max FGrating at 2400'})
horse_data = pd.merge(horse_data, max_fg_rating_at_2400[['HorseId', 'Max FGrating at 2400']],
                      on='HorseId', how='left')
max_fg_rating_at_2400 = pd.DataFrame()
del max_fg_rating_at_2400

# Extrag maximul FGrating pentru fiecare cal in parte, pentru Sha-Tin - iarba
max_fg_rating_at_sha_tin_grass = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Gress')]
max_fg_rating_at_sha_tin_grass = \
    max_fg_rating_at_sha_tin_grass.loc[
        max_fg_rating_at_sha_tin_grass.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
        ['HorseId', 'FGrating']]
max_fg_rating_at_sha_tin_grass = max_fg_rating_at_sha_tin_grass.rename(
    columns={'FGrating': 'Max FGrating at Sha-Tin grass'})
horse_data = pd.merge(horse_data, max_fg_rating_at_sha_tin_grass[['HorseId', 'Max FGrating at Sha-Tin grass']],
                      on='HorseId', how='left')
max_fg_rating_at_sha_tin_grass = pd.DataFrame()
del max_fg_rating_at_sha_tin_grass

# Extrag maximul FGrating pentru fiecare cal in parte, pentru Sha-Tin - pamant
max_fg_rating_at_sha_tin_dirt = raw_data.loc[(raw_data.Track == 'Sha Tin') & (raw_data.Surface == 'Dirt')]
max_fg_rating_at_sha_tin_dirt = \
    max_fg_rating_at_sha_tin_dirt.loc[
        max_fg_rating_at_sha_tin_dirt.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
        ['HorseId', 'FGrating']]
max_fg_rating_at_sha_tin_dirt = max_fg_rating_at_sha_tin_dirt.rename(
    columns={'FGrating': 'Max FGrating at Sha-Tin dirt'})
horse_data = pd.merge(horse_data, max_fg_rating_at_sha_tin_dirt[['HorseId', 'Max FGrating at Sha-Tin dirt']],
                      on='HorseId', how='left')
max_fg_rating_at_sha_tin_dirt = pd.DataFrame()
del max_fg_rating_at_sha_tin_dirt

# Extrag maximul FGrating pentru fiecare cal in parte, pentru Happy Valley - iarba
max_fg_rating_at_happy_valley_grass = raw_data.loc[(raw_data.Track == 'Happy Valley') & (raw_data.Surface == 'Gress')]
max_fg_rating_at_happy_valley_grass = \
    max_fg_rating_at_happy_valley_grass.loc[
        max_fg_rating_at_happy_valley_grass.groupby(['HorseId'], sort=False)['FGrating'].idxmax()][
        ['HorseId', 'FGrating']]
max_fg_rating_at_happy_valley_grass = max_fg_rating_at_happy_valley_grass.rename(
    columns={'FGrating': 'Max FGrating at Happy Valley grass'})
horse_data = pd.merge(horse_data,
                      max_fg_rating_at_happy_valley_grass[['HorseId', 'Max FGrating at Happy Valley grass']],
                      on='HorseId', how='left')
max_fg_rating_at_happy_valley_grass = pd.DataFrame()
del max_fg_rating_at_happy_valley_grass

print(horse_data.shape)
print(horse_data.head())
horse_data.to_excel('Date sortate.xlsx')
