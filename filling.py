import pandas as pd
import returning as r


def count_the_number_of_nan_s_before_first_number(df):
    return df.isna().cumprod().sum()


def fill_preprocessing(df, columns, horse_id):
    return df.loc[df.HorseId == horse_id][columns]


def fill_na_s(df, column_name, column_to_fill):
    df[column_name] = df[column_name].fillna(0, limit=count_the_number_of_nan_s_before_first_number(df[column_name]))
    df[column_name] = df[column_name].ffill()
    df = df.drop(columns=[column_to_fill, 'HorseId'])
    return df


def fill_for_all(df, column, group_by):
    return df.groupby(group_by)[column].fillna(method='ffill').fillna(0)


def fill_the_gaps(df, what_for, text, column_to_fill):
    columns = r.return_columns_that_will_be_used(what_for, column_to_fill, text)
    df = df.loc[:, columns]
    for horse_id in df['HorseId'].unique():
        preprocessed_data = fill_preprocessing(df, columns, horse_id)
        df.loc[df.HorseId == horse_id, text] = fill_na_s(preprocessed_data, text, column_to_fill)
    return df.loc[:, text]
# TODO: functia aceasta e neobisnuit de inceata. Sa vad de ce (profiling)
