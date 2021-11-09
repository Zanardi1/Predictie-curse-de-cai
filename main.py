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
horse_data = pd.merge(horse_data, last_fg_rating[['HorseId', 'Last FGrating']], on='HorseId')
last_fg_rating = pd.DataFrame()

# Extrag ultima pozitie pentru fiecare cal
last_final_position = raw_data[['HorseId', 'Plassering', 'Dato']]
last_final_position = last_final_position.loc[last_final_position.groupby('HorseId').Dato.idxmax(), :]
horse_data = pd.merge(horse_data, last_final_position[['HorseId', 'Plassering']], on='HorseId')
last_final_position = pd.DataFrame()

# Extrag ultimul FGrating pentru o anumita pista
last_fg_rating_at_track = raw_data[['HorseId', 'FGrating', 'Dato', 'Track']]
last_fg_rating_at_track = last_fg_rating_at_track.loc[
                          last_fg_rating_at_track.groupby(['HorseId', 'Track']).Dato.idxmax(), :]
last_fg_rating_at_track = last_fg_rating_at_track.rename(columns={'FGrating': 'Last FGrating at Track'})
horse_data = pd.merge(horse_data, last_fg_rating_at_track[['Last FGrating at Track', 'HorseId', 'Track']], on='HorseId')
last_fg_rating_at_track = pd.DataFrame()

# Extrag pozitia finala pentru o anumita pista
last_final_position_at_track = raw_data[['HorseId', 'Plassering', 'Dato', 'Track']]
last_final_position_at_track = last_final_position_at_track.loc[
                               last_final_position_at_track.groupby(['HorseId', 'Track']).Dato.idxmax(), :]
last_final_position_at_track = last_final_position_at_track.rename(
    columns={'Plassering': 'Last Final Position at Track'})
horse_data = pd.merge(horse_data, last_final_position_at_track[['Last Final Position at Track', 'HorseId']],
                      on='HorseId')
last_final_position_at_track = pd.DataFrame()

# Extrag ultimul FGrating pentru fiecare distanta
last_fg_rating_at_distance = raw_data[['HorseId', 'Dato', 'FGrating', 'Distance']]
last_fg_rating_at_distance = last_fg_rating_at_distance.loc[
                             last_fg_rating_at_distance.groupby(['HorseId', 'Distance']).Dato.idxmax(), :]
last_fg_rating_at_distance = last_fg_rating_at_distance.rename(columns={'FGrating': 'Last FGrating at distance'})
horse_data = pd.merge(horse_data, last_fg_rating_at_distance[['HorseId', 'Last FGrating at distance', 'Distance']],
                      on='HorseId')
last_fg_rating_at_distance = pd.DataFrame()

# Extrag ultima positie finala pentru fiecare distanta
last_final_position_at_distance = raw_data[['HorseId', 'Dato', 'Plassering', 'Distance']]
last_final_position_at_distance = last_final_position_at_distance.loc[
                                  last_final_position_at_distance.groupby(['HorseId', 'Distance']).Dato.idxmax(), :]
last_final_position_at_distance = last_final_position_at_distance.rename(
    columns={'Plassering': 'Last final position at distance'})
horse_data = pd.merge(horse_data, last_final_position_at_distance[['HorseId', 'Last final position at distance']],
                      on='HorseId')
last_final_position_at_distance = pd.DataFrame()

last_fg_rating_at_surface = raw_data[['HorseId', 'Dato', 'Surface', 'FGrating']]
last_fg_rating_at_surface = last_fg_rating_at_surface.loc[
                            last_fg_rating_at_surface.groupby(['HorseId', 'Surface']).Dato.idxmax(), :]
last_fg_rating_at_surface = last_fg_rating_at_surface.rename(columns={'FGrating': 'Last FGrating at surface'})
horse_data = pd.merge(horse_data, last_fg_rating_at_surface[['HorseId', 'Surface', 'Last FGrating at surface']],
                      on='HorseId')
last_fg_rating_at_surface = pd.DataFrame()

last_final_position_at_surface = raw_data[['HorseId', 'Dato', 'Surface', 'Plassering']]
last_final_position_at_surface = last_final_position_at_surface.loc[
                                 last_final_position_at_surface.groupby(['HorseId', 'Surface']).Dato.idxmax(), :]
last_final_position_at_surface = last_final_position_at_surface.rename(
    columns={'Plassering': 'Last final position at surface'})
horse_data = pd.merge(horse_data, last_final_position_at_surface[['HorseId', 'Last final position at surface']],
                      on='HorseId')
last_final_position_at_surface = pd.DataFrame()

# Extrag maximul FGRating pentru fiecare cal in parte
max_fg_rating = raw_data[raw_data.FGrating == raw_data.groupby(['HorseId'])['FGrating'].transform(max)]
max_fg_rating = max_fg_rating[['FGrating', 'HorseId']].drop_duplicates()
max_fg_rating = max_fg_rating.rename(columns={'FGrating': 'Max FGrating'})
horse_data = pd.merge(horse_data, max_fg_rating[['HorseId', 'Max FGrating']], on='HorseId')
max_fg_rating = pd.DataFrame()

# Extrag maximul FGrating pentru fiecare cal in parte, pentru fiecare pista
max_fg_rating_at_track = raw_data.loc[raw_data.groupby(['HorseId', 'Track'], sort=False)['FGrating'].idxmax()][
    ['HorseId', 'FGrating', 'Track']]
max_fg_rating_at_track = max_fg_rating_at_track.rename(columns={'FGrating': 'Max FGrating at track'})
horse_data = pd.merge(horse_data, max_fg_rating_at_track[['HorseId', 'Max FGrating at track']], on='HorseId')
max_fg_rating_at_track = pd.DataFrame()

print(horse_data.shape)
print(horse_data.head())
horse_data.to_excel('Date sortate.xlsx')
