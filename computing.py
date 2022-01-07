import filling as f
import pandas as pd
import returning as r


def compute_last_fgrating(df, mask=''):
    if len(mask) == 0:
        return df.groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))
    else:
        return df.loc[mask][['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))


def compute_last_final_position(df, mask=''):
    if len(mask) == 0:
        return df.groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))
    else:
        return df.loc[mask][['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))


def compute_average_fgrating_in_last_starts(df, no_starts):
    return df.groupby('HorseId')['FGrating'].transform(lambda x: x.shift(1).rolling(no_starts, 1).mean())


def compute_average_position_in_last_starts(df, no_starts):
    return df.groupby('HorseId')['Plassering'].transform(lambda x: x.shift(1).rolling(no_starts, 1).mean())


def compute_average_fg_rating(df, mask=''):
    if len(mask) == 0:
        df['cumsum'] = df.groupby('HorseId')['FGrating'].apply(lambda x: x.shift(fill_value=0).cumsum())
        return df['cumsum'] / df.groupby('HorseId')['FGrating'].cumcount()
    else:
        return df.loc[mask].groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding().mean())


def compute_average_position(df, mask=''):
    if len(mask) == 0:
        temp = df.groupby('HorseId')['Plassering']
        df['cumsum'] = temp.apply(lambda x: x.shift(fill_value=0).cumsum())
        return df['cumsum'] / temp.cumcount()
    else:
        return df.loc[mask].groupby('HorseId')['Plassering'].apply(lambda x: x.shift().expanding().mean())


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
        return (df.loc[mask].reset_index().groupby('JockeyId').rolling(no_days, on='Dato').agg(
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
    df[text] = compute_trainer_win_percent_in_last_days(df, time_length, mask=mask)
    f.fill_for_all(df, text, 'TrainerID')


def compute_average_fgratings_in_the_last_10_or_4_starts(df):
    for i in [10, 4]:
        text = 'Average FGrating in the last ' + str(i) + ' starts'
        df[text] = compute_average_fgrating_in_last_starts(df, i)
        df[text] = f.fill_for_all(df, text, 'HorseId')


def compute_average_final_position_in_the_last_10_or_4_starts(df):
    for i in [10, 4]:
        text = 'Average Position in the last ' + str(i) + ' starts'
        df[text] = compute_average_position_in_last_starts(df, i)
        df[text] = f.fill_for_all(df, text, 'HorseId')


def compute_average_fgratings_for_every_track(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Average FGrating')
        compute_average_fgratings_without_conditions(df, mask, text)


def compute_average_final_position_for_every_track(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Average Position')
        compute_average_positions_without_conditions(df, mask, text)


def compute_average_fgratings_for_every_distance_type(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_distance_types(df, i, 'Average FGrating')
        compute_average_fgratings_without_conditions(df, mask, text)


def compute_average_final_position_for_every_distance_type(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_distance_types(df, i, 'Average Position')
        compute_average_positions_without_conditions(df, mask, text)


def compute_maximum_fgratings_for_every_track(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Maximum FGrating')
        compute_max_fg_ratings_without_conditions(df, mask, text)


def compute_maximum_fgratings_for_every_distance_type(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_distance_types(df, i, 'Maximum FGrating')
        compute_max_fg_ratings_without_conditions(df, mask, text)


def compute_maximum_fgratings_in_the_last_3_starts(df):
    df['Maximum FGrating in last 3 starts'] = df.groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding(min_periods=3).max())
    df['Maximum FGrating in last 3 starts'] = f.fill_for_all(df, 'Maximum FGrating in last 3 starts', 'HorseId')


def compute_top_for_horse(df):
    df['Top'] = ((df['FGrating'] - df['Maximum FGrating'] >= 4).map({True: 1, False: 0}))


def compute_days_since_last_race(df):
    df['Days since last race'] = df.groupby('HorseId')['Dato'].apply(
        lambda x: x.diff().fillna(method='ffill').fillna(pd.NaT))


def compute_trainer_win_percent_in_the_last_days(df):
    for i in [1000, 90, 30]:
        text = 'Trainer winning % in the last ' + str(i) + ' days'
        time_length = str(i) + 'D'
        compute_trainer_win_percent_without_conditions(df, text, time_length=time_length)


def compute_trainer_win_percent_for_every_distance(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_distance_types(df, i, 'Trainer winning % in the last 1000 days')
        compute_trainer_win_percent_without_conditions(df, text, mask=mask)


def compute_trainer_win_percent_for_every_track(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Trainer winning % in the last 1000 days')
        compute_trainer_win_percent_without_conditions(df, text, mask=mask)


def compute_jockey_win_percent(df):
    df['Jockey winning % in the last 1000 days'] = compute_jockey_win_percent_in_last_days(df, '1000D')
    df['Jockey winning % in the last 1000 days'] = df.groupby('JockeyId')[
        'Jockey winning % in the last 1000 days'].fillna(method='ffill').fillna(0)


def compute_jockey_win_percent_on_tracks_with_and_without_surfaces(df):
    for i in range(5):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Jockey winning % in the last 1000 days')
        df[text] = compute_jockey_win_percent_in_last_days(df, '1000D', mask=mask)


def compute_jockey_win_percent_on_every_surface(df):
    for i in [0, 1]:
        mask, text = r.return_mask_and_text_from_surfaces(df, i, 'Jockey winning % in the last 1000 days')
        df[text] = compute_jockey_win_percent_in_last_days(df, '1000D', mask=mask)


def compute_jockey_win_percent_on_every_track(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Jockey winning % in the last 1000 days')
        df[text] = compute_jockey_win_percent_in_last_days(df, '1000D', mask=mask)


def compute_jockey_win_percent_on_every_distance(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_distance_types(df, i, 'Jockey winning % in the last 1000 days')
        df[text] = compute_jockey_win_percent_in_last_days(df, '1000D', mask=mask)


def compute_jockey_win_percent_on_distances_and_surfaces(df):
    for i in range(3):
        for j in range(2):
            mask, text = r.return_mask_and_text_from_distances_and_surfaces(df, i, j,
                                                                            'Jockey winning % in the last 1000 days')
            df[text] = compute_jockey_win_percent_in_last_days(df, '1000D', mask=mask)


def compute_jockey_average_final_position(df):
    df['Average Position of a jockey in the last 1000 days'] = compute_jockey_average_final_position_in_last_days(df,
                                                                                                                  '1000D')
    df['Average Position of a jockey in the last 1000 days'] = f.fill_for_all(df,
                                                                              'Average Position of a jockey in the last 1000 days',
                                                                              'JockeyId')


def compute_jockey_average_final_position_on_tracks_disregarding_surfaces(df):
    for i in [3, 4]:
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Average Position of a jockey in the last 1000 days')
        df.loc[mask, text] = compute_jockey_average_final_position_in_last_days(df, '1000D', mask=mask)
        df[text] = f.fill_for_all(df, text, 'JockeyId')


def compute_jockey_average_final_position_on_surfaces(df):
    for i in range(2):
        mask, text = r.return_mask_and_text_from_surfaces(df, i, 'Average Position of a jockey in the last 1000 days')
        df.loc[mask, text] = compute_jockey_average_final_position_in_last_days(df, '1000D', mask=mask)
        df[text] = f.fill_for_all(df, text, 'JockeyId')


def compute_jockey_average_final_position_on_tracks_and_surfaces(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Average Position of a jockey in the last 1000 days')
        df.loc[mask, text] = compute_jockey_average_final_position_in_last_days(df, '1000D', mask=mask)
        df[text] = f.fill_for_all(df, text, 'JockeyId')


def compute_jockey_average_final_position_for_every_distance_type(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_distance_types(df, i,
                                                                'Average Position of a jockey in the last 1000 days')
        df.loc[mask, text] = compute_jockey_average_final_position_in_last_days(df, '1000D', mask=mask)
        df[text] = f.fill_for_all(df, text, 'JockeyId')


def compute_jockey_average_final_position_on_tracks_and_surfaces(df):
    for i in range(3):
        for j in range(2):
            mask, text = r.return_mask_and_text_from_distances_and_surfaces(df, i, j,
                                                                            'Average Position of a jockey in the last 1000 days')
            df.loc[mask, text] = compute_jockey_average_final_position_in_last_days(df, '1000D', mask=mask)
            df[text] = f.fill_for_all(df, text, 'JockeyId')


def compute_jockey_mean_path(df):
    df['Mean path of a jockey in the last 1000 days'] = compute_jockey_mean_path_in_last_days(df, '1000D')
    df['Mean path of a jockey in the last 1000 days'] = f.fill_for_all(df,
                                                                       'Mean path of a jockey in the last 1000 days',
                                                                       'JockeyId')


def compute_jockey_mean_path_on_surface(df):
    for i in range(2):
        mask, text = r.return_mask_and_text_from_surfaces(df, i, 'Mean path of a jockey in the last 1000 days')
        df.loc[mask, text] = compute_jockey_mean_path_in_last_days(df, '1000D', mask=mask)
        df[text] = f.fill_for_all(df, text, 'JockeyId')


def compute_jockey_mean_path_on_tracks_and_surfaces(df):
    for i in range(3):
        mask, text = r.return_mask_and_text_from_tracks(df, i, 'Mean path of a jockey in the last 1000 days')
        df.loc[mask, text] = compute_jockey_mean_path_in_last_days(df, '1000D', mask=mask)
        df[text] = f.fill_for_all(df, text, 'JockeyId')


def compute_jockey_mean_path_on_distances_and_surfaces(df):
    for i in range(3):
        for j in range(2):
            mask, text = r.return_mask_and_text_from_distances_and_surfaces(df, i, j,
                                                                            'Mean path of a jockey in the last 1000 days')
            df.loc[mask, text] = compute_jockey_mean_path_in_last_days(df, '1000D', mask=mask)
            df[text] = f.fill_for_all(df, text, 'JockeyId')


def compute_horse_win_percent(df):
    df['Horse winning %'] = compute_horse_win_percentage(df)
    df['Horse winning %'] = df.groupby('HorseId')['Horse winning %'].fillna(method='ffill').fillna(0)
