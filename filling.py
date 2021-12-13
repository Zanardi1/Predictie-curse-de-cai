import returning as r
import pandas as pd


def filling_na_s_engine(df, what_for, text, column_to_fill):
    columns = r.return_columns_that_will_be_used(what_for, column_to_fill, text)
    for horse_id in df['HorseId'].unique():
        data_to_be_processed = df.loc[df.HorseId == horse_id][columns]
        df.loc[df.HorseId == horse_id, text] = fill_na_s(data_to_be_processed, text, what_for,
                                                         column_to_fill)
        return df.loc[df.HorseId == horse_id, text]


def fill_na_s(df, column_name, what_for, column_to_fill):
    if what_for == 'Tracks':
        race_track, race_surface = r.return_track_and_surface_from_text(column_name)
        work_columns = ['Track', 'Surface']
        mask = (df.Track == race_track) & (df.Surface == race_surface)
    elif what_for == 'Distances':
        distance = r.return_distance_from_text(df, column_name)
        work_columns = ['Distance']
        mask = (df.Distance == distance)
    else:
        print('Eroare')
        return None

    if len(df[work_columns].index) > 1:
        set_track_and_surface_data = df[work_columns].loc[mask]
        first_race_index = set_track_and_surface_data.index[0] if len(set_track_and_surface_data.index) > 0 else df[
            work_columns].index.max()
    else:
        first_race_index = df[work_columns].index.min()
    value_to_replace = 0
    for i in range(df[work_columns].index.min(), first_race_index + 1):
        df.loc[i, column_name] = 0
    for i in range(first_race_index, df[work_columns].index.max() + 1):
        if pd.isnull(df.loc[i, column_name]):
            df.loc[i, column_name] = value_to_replace
        else:
            value_to_replace = df.loc[i, column_to_fill]
    df = df.drop(columns=[column_to_fill, 'HorseId'] + work_columns)
    return df


def fill_for_all(df, column, group_by):
    result = df.groupby(group_by)[column].fillna(method='ffill').fillna(0)
    return result
