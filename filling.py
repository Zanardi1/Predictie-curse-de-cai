import pandas as pd
import returning as r


def fill_preprocessing(df, what_for, text, column_to_fill, columns, horse_id):
    return df.loc[df.HorseId == horse_id][columns]


def fill_na_s(df, column_name, what_for, column_to_fill, work_columns, mask, race_track='', race_surface='',
              distance=''):
    if len(df[work_columns].index) > 1:
        set_track_and_surface_data = df[work_columns].loc[mask]
        first_race_index = set_track_and_surface_data.index[0] if len(set_track_and_surface_data.index) > 0 else df[
            work_columns].index.max()
    else:
        first_race_index = df[work_columns].index.min()
    value_to_replace = 0
    df[column_name] = df[column_name].fillna(0, limit=first_race_index + 1 - df[work_columns].index.min())
    for i in df[work_columns].index:
        if pd.isnull(df.loc[i, column_name]):
            df.loc[i, column_name] = value_to_replace
        else:
            value_to_replace = df.loc[i, column_to_fill]
    df = df.drop(columns=[column_to_fill, 'HorseId'] + work_columns)
    return df


def fill_for_all(df, column, group_by):
    result = df.groupby(group_by)[column].fillna(method='ffill').fillna(0)
    return result


def fill_the_gaps(df, what_for, text, column_to_fill, work_columns, mask, race_track='', race_surface='', distance=''):
    columns = r.return_columns_that_will_be_used(what_for, column_to_fill, text)
    df = df.loc[:, columns]
    for horse_id in df['HorseId'].unique():
        preprocessed_data = fill_preprocessing(df, what_for, text, column_to_fill, columns, horse_id)
        df.loc[df.HorseId == horse_id, text] = fill_na_s(preprocessed_data, text, what_for, column_to_fill,
                                                         work_columns, mask, race_track=race_track,
                                                         race_surface=race_surface, distance=distance)
    return df.loc[:, text]
# TODO: functia aceasta e neobisnuit de inceata. Sa vad de ce.
