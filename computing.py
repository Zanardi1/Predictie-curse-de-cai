import filling as f
import pandas as pd
import returning as r


def compute_last_fgrating(df, mask=''):
    if len(mask) == 0:
        return df.groupby('HorseId')['FGrating'].shift(1)
    else:
        return df.loc[mask][['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].shift(1)


def compute_last_final_position(df, mask=''):
    if len(mask) == 0:
        return df.groupby('HorseId')['Plassering'].shift(1)
    else:
        return df.loc[mask][['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].shift(1)


def compute_average_fgrating_in_last_starts(df, no_starts):
    return df.groupby('HorseId')['FGrating'].shift().expanding(min_periods=no_starts).mean()


def compute_average_position_in_last_starts(df, no_starts):
    return df.groupby('HorseId')['Plassering'].shift().expanding(min_periods=no_starts).mean()


def compute_average_fg_rating(df, mask=''):
    if len(mask) == 0:
        df['cumsum'] = df.groupby('HorseId')['FGrating'].shift(fill_value=0).cumsum()
        return df['cumsum'] / df.groupby('HorseId')['FGrating'].cumcount()
    else:
        return df.loc[mask].groupby('HorseId')['FGrating'].shift().expanding().mean()


def compute_average_position(df, mask=''):
    if len(mask) == 0:
        temp = df.groupby('HorseId')['Plassering']
        df['cumsum'] = temp.shift(fill_value=0).cumsum()
        return df['cumsum'] / temp.cumcount()
    else:
        return df.loc[mask].groupby('HorseId')['Plassering'].shift().expanding().mean()


def compute_max_fg_rating(df, mask=''):
    if len(mask) == 0:
        return df.groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding().max())
    else:
        return df.loc[mask].groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding().max())


def compute_trainer_win_percent_in_last_days(df, no_days, mask=''):
    df['Win'] = df['Plassering'].eq(1)
    if len(mask) == 0:
        return (df.reset_index().groupby('TrainerID').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
    else:
        return (df.loc[mask].reset_index().groupby('TrainerID').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))


def compute_jockey_win_percent_in_last_days(df, no_days, mask=''):
    df['Win'] = df['Plassering'].eq(1)
    if len(mask) == 0:
        return (df.reset_index().groupby('JockeyId').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
    else:
        return (df.loc[mask].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))


def compute_jockey_average_final_position_in_last_days(df, no_days, mask=''):
    if len(mask) == 0:
        return (df.set_index('Dato').groupby(['JockeyId', pd.Grouper(freq=no_days)])['Plassering'].transform(
            lambda x: x.expanding().mean()).to_numpy())
    else:
        return (df[mask].set_index('Dato').groupby(['JockeyId', 'Track', pd.Grouper(freq=no_days)])[
                    'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())


def compute_jockey_mean_path_in_last_days(df, no_days, mask=''):
    if len(mask) == 0:
        return df.set_index('Dato').groupby(['JockeyId', pd.Grouper(freq='1000D')])['Path'].transform(
            lambda x: x.expanding().mean()).to_numpy()
    else:
        return df[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
            'Path'].transform(lambda x: x.expanding().mean()).to_numpy()


def compute_horse_win_percentage(df):
    df['Win'] = df['Plassering'].eq(1)
    return (df.reset_index().groupby('HorseId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))


def compute_last_fgratings_on_tracks(df):
    race_track, race_surface, distance, work_columns, mask = r.return_filling_parameters(
        df, 'Tracks')
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Last FGrating')
        df[text] = compute_last_fgrating(df, mask=mask)
        df[text] = f.fill_the_gaps(df, 'Tracks', text, 'FGrating', work_columns, mask, race_track=race_track,
                                   race_surface=race_surface)


def compute_last_fgratings_on_distances(df):
    race_track, race_surface, distance, work_columns, mask = r.return_filling_parameters(
        df, 'Distances')
    for distance in df['Distance'].unique():
        mask, text = r.return_mask_and_text_from_distances(df, distance, 'Last FGrating')
        df[text] = compute_last_fgrating(df, mask=mask)
        df[text] = f.fill_the_gaps(df, 'Distances', text, 'FGrating', work_columns, mask, distance=distance)


def compute_last_fgratings_with_conditions(df):
    compute_last_fgratings_on_tracks(df)
    compute_last_fgratings_on_distances(df)


def compute_last_fgratings_without_conditions(df):
    df['Last FGrating'] = compute_last_fgrating(df)
    df['Last FGrating'] = f.fill_for_all(df, 'Last FGrating', 'HorseId')


def compute_last_final_positions_on_tracks(df):
    race_track, race_surface, distance, work_columns, mask = r.return_filling_parameters(
        df, 'Tracks')
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Last Final Position at')
        df[text] = compute_last_final_position(df, mask=mask)
        df[text] = f.fill_the_gaps(df, 'Tracks', text, 'Plassering', work_columns, mask, race_track=race_track,
                                   race_surface=race_surface)
    # TODO : sa mut functia fill_the_gaps in afara functiei compute_last_final_positions_on_tracks, deoarece
    #  compute_last_final_positions_on_tracks ar executa doua lucruri.


def compute_last_final_positions_on_distances(df):
    race_track, race_surface, distance, work_columns, mask = r.return_filling_parameters(
        df, 'Distances')
    for distance in df['Distance'].unique():
        mask = df.Distance == distance
        text = 'Last Final Position at ' + str(distance) + ' m'
        df[text] = compute_last_final_position(df, mask=mask)
        df[text] = f.fill_the_gaps(df, 'Distances', text, 'Plassering', work_columns, mask, distance=distance)
    # TODO : sa mut functia fill_the_gaps in afara functiei compute_last_final_positions_on_distances, deoarece
    #  compute_last_final_positions_on_distances ar executa doua lucruri


def compute_last_final_positions_with_conditions(df):
    compute_last_final_positions_on_tracks(df)
    compute_last_final_positions_on_distances(df)


def compute_last_final_positions_without_conditions(df):
    df['Last Plassering'] = compute_last_final_position(df)
    df['Last Plassering'] = f.fill_for_all(df, 'Last Plassering', 'HorseId')


def compute_average_fgratings_without_conditions(df, mask='', text='Average FGrating'):
    df[text] = compute_average_fg_rating(df, mask)
    df[text] = f.fill_for_all(df, text, 'HorseId')


def compute_average_positions_without_conditions(df, mask='', text='Average Position'):
    df[text] = compute_average_position(df, mask)
    df[text] = f.fill_for_all(df, text, 'HorseId')


def compute_max_fg_ratings_without_conditions(df, mask='', text='Maximum FGrating'):
    df[text] = compute_max_fg_rating(df, mask)
    df[text] = f.fill_for_all(df, text, 'HorseId')


def compute_trainer_win_percent_without_conditions(df, text, time_length='1000D', mask=''):
    df[text] = compute_trainer_win_percent_in_last_days(df, time_length)
    f.fill_for_all(df, text, 'TrainerID')
