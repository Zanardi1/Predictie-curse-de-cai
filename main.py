import pandas as pd


def compute_last_fgrating(df, mask=''):
    if len(mask) == 0:
        return df.groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))
    else:
        return df.loc[mask][['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(
            lambda x: x.shift(1))


def compute_last_final_position(df, mask=''):
    if len(mask) == 0:
        return df.groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))
    else:
        return df.loc[mask][['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))


def compute_average_fgrating_in_last_starts(df, no_starts):
    return df.groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding(min_periods=no_starts).mean())


def compute_average_position_in_last_starts(df, no_starts):
    return df.groupby('HorseId')['Plassering'].apply(lambda x: x.shift().expanding(min_periods=no_starts).mean())


def compute_average_fg_rating(df, mask=''):
    if len(mask) == 0:
        df['cumsum'] = df.groupby('HorseId')['FGrating'].apply(lambda p: p.shift(fill_value=0).cumsum())
        return df['cumsum'] / df.groupby('HorseId')['FGrating'].cumcount()
    else:
        return df.loc[mask].groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding().mean())


def compute_average_position(df, mask=''):
    if len(mask) == 0:
        temp = df.groupby('HorseId')['Plassering']
        df['cumsum'] = temp.apply(lambda p: p.shift(fill_value=0).cumsum())
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
        s = (df.reset_index().groupby('TrainerID').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
    else:
        s = (df.loc[mask].reset_index().groupby('TrainerID').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
    return s


def compute_jockey_win_percent_in_last_days(df, no_days, mask=''):
    df['Win'] = df['Plassering'].eq(1)
    if len(mask) == 0:
        s = (df.reset_index().groupby('JockeyId').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
    else:
        s = (df.loc[mask].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
    return s


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
    s = (df.reset_index().groupby('HorseId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
    return s


def return_columns_that_will_be_used(what_for, column_to_fill, text):
    columns = []
    if what_for == 'Tracks':
        columns = ['Track', 'Surface', column_to_fill, 'HorseId', text]
    elif what_for == 'Distances':
        columns = ['Distance', column_to_fill, 'HorseId', text]
    return columns


def filling_na_s_engine(what_for, text, column_to_fill):
    columns = return_columns_that_will_be_used(what_for, column_to_fill, text)
    for horse_id in horse_ids_list:
        data_to_be_processed = featured_data.loc[featured_data.HorseId == horse_id][columns]
        featured_data.loc[featured_data.HorseId == horse_id, text] = fill_na_s(data_to_be_processed, text, what_for,
                                                                               column_to_fill)


def compute_last_fgratings_on_tracks():
    for i in range(3):
        mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Last FGrating')
        featured_data[text] = compute_last_fgrating(featured_data, mask=mask)
        filling_na_s_engine('Tracks', text, 'FGrating')


def compute_last_fgratings_on_distances():
    for distance in distances_list:
        mask, text = return_mask_and_text_from_distances(featured_data, distance, 'Last FGrating')
        featured_data[text] = compute_last_fgrating(featured_data, mask=mask)
        filling_na_s_engine('Distances', text, 'FGrating')


def compute_last_fgratings_with_conditions():
    compute_last_fgratings_on_tracks()
    compute_last_fgratings_on_distances()


def compute_last_final_positions_on_tracks():
    for i in range(3):
        mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Final Position')
        featured_data[text] = compute_last_final_position(featured_data, mask=mask)
        filling_na_s_engine('Tracks', text, 'Plassering')


def compute_last_final_positions_on_distances():
    for distance in distances_list:
        mask = featured_data.Distance == distance
        text = 'Last Final Position at ' + str(distance) + ' m'
        featured_data[text] = compute_last_final_position(featured_data, mask=mask)
        filling_na_s_engine('Distances', text, 'Plassering')


def compute_last_final_positions_with_conditions():
    compute_last_final_positions_on_tracks()
    compute_last_final_positions_on_distances()


def return_mask_and_text_from_tracks(df, track_no, metric):
    if track_no == 0:  # Sha Tin - iarba
        mask = (df.Track == 'Sha Tin') & (df.Surface == 'Gress')
        text = str(metric) + ' at Sha Tin Grass'
    if track_no == 1:  # Sha Tin - pamant
        mask = (df.Track == 'Sha Tin') & (df.Surface == 'Dirt')
        text = str(metric) + ' at Sha Tin Dirt'
    if track_no == 2:  # Happy Valley - iarba
        mask = (df.Track == 'Happy Valley') & (df.Surface == 'Gress')
        text = str(metric) + ' at Happy Valley Grass'
    if track_no == 3:  # Sha Tin, indiferent de suprafata
        mask = df.Track == 'Sha Tin'
        text = str(metric) + ' at Sha Tin'
    if track_no == 4:  # Happy Valley, indiferent de suprafata
        mask = df.Track == 'Happy Valley'
        text = str(metric) + ' at Happy Valley'
    return mask, text


def return_mask_and_text_from_distance_types(df, distance_type, metric):
    if distance_type == 0:  # Distante de sprint
        mask = (df.Distance == 1000) | (df.Distance == 1200)
        text = str(metric) + ' at sprint distances'
    if distance_type == 1:  # Distanta medie
        mask = (df.Distance == 1400) | (df.Distance == 1600) | (df.Distance == 1650) | (df.Distance == 1800)
        text = str(metric) + ' at medium distances'
    if distance_type == 2:  # Distante lungi
        mask = (df.Distance == 2000) | (df.Distance == 2200) | (df.Distance == 2400)
        text = str(metric) + ' at long distances'
    return mask, text


def return_mask_and_text_from_distances(df, distance, metric):
    mask = df.Distance == distance
    text = str(metric) + ' at ' + str(distance) + ' m'
    return mask, text


def return_mask_and_text_from_surfaces(df, surface_name, metric):
    if surface_name == 0:  # Iarba
        mask = df.Surface == 'Gress'
        text = str(metric) + ' on grass'
    if surface_name == 1:  # pamant
        mask = df.Surface == 'Dirt'
        text = str(metric) + ' on dirt'
    return mask, text


def return_mask_and_text_from_distances_and_surfaces(df, distance, surface_type, metric):
    if distance == 0:  # Distante scurte
        if surface_type == 0:  # Pe iarba
            mask = ((df.Distance == 1000) | (df.Distance == 1200)) & (df.Surface == 'Gress')
            text = str(metric) + ' at sprint distances on grass'
        if surface_type == 1:  # Pe pamant
            mask = ((df.Distance == 1000) | (df.Distance == 1200)) & (df.Surface == 'Dirt')
            text = str(metric) + ' at sprint distances on dirt'
    if distance == 1:  # Distante medii
        if surface_type == 0:  # Pe iarba
            mask = ((df.Distance == 1400) | (df.Distance == 1600) | (df.Distance == 1650) | (
                    df.Distance == 1800)) & (df.Surface == 'Gress')
            text = str(metric) + ' at middle distances on grass'
        if surface_type == 1:  # Pe pamant
            mask = ((df.Distance == 1400) | (df.Distance == 1600) | (df.Distance == 1650) | (
                    df.Distance == 1800)) & (df.Surface == 'Dirt')
            text = str(metric) + ' at middle distances on dirt'
    if distance == 2:  # Distante lungi
        if surface_type == 0:  # Pe iarba
            mask = ((df.Distance == 2000) | (df.Distance == 2200) | (df.Distance == 2400)) & (
                    df.Surface == 'Gress')
            text = str(metric) + ' at long distance on grass'
        if surface_type == 1:  # Pe pamant
            mask = ((df.Distance == 2000) | (df.Distance == 2200) | (df.Distance == 2400)) & (
                    df.Surface == 'Dirt')
            text = str(metric) + ' at long distance on dirt'
    return mask, text


def return_track_and_surface_from_text(text):
    if 'Sha Tin' in text:
        track = 'Sha Tin'
    else:
        track = 'Happy Valley'
    if 'Grass' in text:
        surface = 'Gress'
    else:
        surface = 'Dirt'
    return track, surface


def return_distance_from_text(text):
    for distance in distances_list:
        if str(distance) in text:
            return distance


def fill_na_s(df, column_name, what_for, column_to_fill):
    if what_for == 'Tracks':
        race_track, race_surface = return_track_and_surface_from_text(column_name)
        work_columns = ['Track', 'Surface']
        mask = (df.Track == race_track) & (df.Surface == race_surface)
    elif what_for == 'Distances':
        distance = return_distance_from_text(column_name)
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
            # value_to_replace = df.loc[df[work_columns].index.min(), column_to_fill]
    df = df.drop(columns=[column_to_fill, 'HorseId'] + work_columns)
    return df


def fill_for_all(df, column, group_by):
    result = df.groupby(group_by)[column].fillna(method='ffill').fillna(0)
    return result


raw_data = pd.read_excel('Data.xlsx')
print(raw_data.shape)
print(raw_data.head())

featured_data = raw_data.copy()

horse_ids_list = featured_data['HorseId'].unique()
distances_list = featured_data['Distance'].unique()

# Calculez Last FGrating pentru fiecare cal
featured_data['Last FGrating'] = compute_last_fgrating(featured_data)
featured_data['Last FGrating'] = fill_for_all(featured_data, 'Last FGrating', 'HorseId')

# Calculez Last Final Position pentru fiecare cal
featured_data['Last Plassering'] = compute_last_final_position(featured_data)
featured_data['Last Plassering'] = fill_for_all(featured_data, 'Last Plassering', 'HorseId')

# Calculez Last FGrating pentru cele trei piste, respectiv pentru fiecare distanta, ambele pentru fiecare cal
compute_last_fgratings_with_conditions()

# Calculez pozitia finala pentru cele trei piste, respectiv pentru fiecare distanta, ambele pentru fiecare cal
compute_last_final_positions_with_conditions()

# Calculez FGrating mediu total al fiecarui cal
featured_data['Average FGrating'] = compute_average_fg_rating(featured_data)
featured_data['Average FGrating'] = fill_for_all(featured_data, 'Average FGrating', 'HorseId')

# Calculez pozitia medie totala pe fiecare cal
featured_data['Average Position'] = compute_average_position(featured_data)
featured_data['Average Position'] = fill_for_all(featured_data, 'Average Position', 'HorseId')

# Calculez FGrating mediu in ultimele 10, respectiv 4 starturi pentru fiecare cal
for i in [10, 4]:
    text = 'Average FGrating in the last ' + str(i) + ' starts'
    featured_data[text] = compute_average_fgrating_in_last_starts(featured_data, i)
    featured_data[text] = fill_for_all(featured_data, text, 'HorseId')

# Calculez pozitia finala medie in ultimele 10, respectiv 4 starturi pentru fiecare cal
for i in [10, 4]:
    text = 'Average Position in the last ' + str(i) + 'starts'
    featured_data[text] = compute_average_position_in_last_starts(featured_data, i)
    featured_data[text] = fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating mediu pentru fiecare dintre cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
# pentru fiecare cal

for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Average FGrating')
    featured_data[text] = compute_average_fg_rating(featured_data, mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'HorseId')

# Calculez pozitia medie pentru fiecare dinte cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
# pentru fiecare cal

for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Average Position')
    featured_data[text] = compute_average_position(featured_data, mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating mediu pentru cele trei tipuri de distante pentru fiecare cal
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Average FGrating')
    featured_data[text] = compute_average_fg_rating(featured_data, mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'HorseId')

# Calculez pozitia medie pentru cele trei tipuri de distante pentru fiecare cal
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Average Position')
    featured_data[text] = compute_average_position(featured_data, mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating maxim pentru fiecare cal
featured_data['Maximum FGrating'] = compute_max_fg_rating(featured_data)
featured_data['Maximum FGrating'] = fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating maxim pentru cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass, pentru fiecare cal
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Maximum FGrating')
    featured_data[text] = compute_max_fg_rating(featured_data, mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating maxim pentru cele trei tipuri de distante, pentru fiecare cal
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Maximum FGrating')
    featured_data[text] = compute_max_fg_rating(featured_data, mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating maxim pentru fiecare cal din ultimele trei starturi
featured_data['Maximum FGrating in last 3 starts'] = featured_data.groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding(min_periods=3).max())
featured_data['Maximum FGrating in last 3 starts'] = fill_for_all(featured_data, 'Maximum FGrating in last 3 starts',
                                                                  'HorseId')

# Calculez daca un cal a fost varf de forma intr-o anumita cursa
featured_data['Top'] = (
    (featured_data['FGrating'] - featured_data['Maximum FGrating'] >= 4).map({True: 1, False: 0}))

# Calculez numarul de zile de la ultima cursa pentru fiecare cal
featured_data['Days since last race'] = featured_data.groupby('HorseId')['Dato'].diff().fillna(method='ffill').fillna(
    pd.NaT)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000, 90, respectiv 30 de zile
for i in [1000, 90, 30]:
    text = 'Trainer winning % in the last ' + str(i) + ' days'
    time_length = str(i) + 'D'
    featured_data[text] = compute_trainer_win_percent_in_last_days(featured_data, time_length)
    featured_data[text] = fill_for_all(featured_data, text, 'TrainerID')

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile, pe cele trei distante
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Trainer winning % in the last 1000 days')
    featured_data[text] = compute_trainer_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'TrainerID')

# Calculez procentajul de victorii ale unui antrenor, in ultimele 1000 de zile, pe cele trei piste
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Trainer winning % in the last 1000 days')
    featured_data[text] = compute_trainer_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'TrainerID')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile
featured_data['Jockey winning % in the last 1000 days'] = compute_jockey_win_percent_in_last_days(featured_data,
                                                                                                  '1000D')
featured_data['Jockey winning % in the last 1000 days'] = featured_data.groupby('JockeyId')[
    'Jockey winning % in the last 1000 days'].fillna(method='ffill').fillna(0)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe cele trei piste, precum si pe piste,
# dar indiferent de suprafata
for i in range(5):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare suprafata
for i in [0, 1]:
    mask, text = return_mask_and_text_from_surfaces(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare pista
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare distanta
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile, pe cele trei tipuri de distante
# si pe cele doua tipuri de suprafete
for i in range(3):
    for j in range(2):
        mask, text = return_mask_and_text_from_distances_and_surfaces(featured_data, i, j,
                                                                      'Jockey winning % in the last 1000 days')
        featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
        featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile
featured_data[
    'Average Position of a jockey in the last 1000 days'] = compute_jockey_average_final_position_in_last_days(
    featured_data, '1000D')
featured_data['Average Position of a jockey in the last 1000 days'] = fill_for_all(featured_data,
                                                                                   'Average Position of a jockey in the last 1000 days',
                                                                                   'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele doua piste, indiferent de suprafata
for i in [3, 4]:
    mask, text = return_mask_and_text_from_tracks(featured_data, i,
                                                  'Average Position of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                       mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele doua suprafete
for i in range(2):
    mask, text = return_mask_and_text_from_surfaces(featured_data, i,
                                                    'Average Position of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                       mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele 2 piste, inclusiv suprafetele
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i,
                                                  'Average Position of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                       mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele trei tipuri de distante
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i,
                                                     'Average Position of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                       mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele trei tipuri de distante si pe cele doua tipuri de suprafata
for i in range(3):
    for j in range(2):
        mask, text = return_mask_and_text_from_distances_and_surfaces(featured_data, i, j,
                                                                      'Average Position of a jockey in the last 1000 days')
        featured_data.loc[mask, text] = compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                           mask=mask)
        featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile
featured_data['Mean path of a jockey in the last 1000 days'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D')
featured_data['Mean path of a jockey in the last 1000 days'] = fill_for_all(featured_data,
                                                                            'Mean path of a jockey in the last 1000 days',
                                                                            'JockeyId')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de suprafata
for i in range(2):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Mean path of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de pista si suprafata
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Mean path of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de suprafata si distanta
for i in range(3):
    for j in range(2):
        mask, text = return_mask_and_text_from_distances_and_surfaces(featured_data, i, j,
                                                                      'Mean path of a jockey in the last 1000 days')
        featured_data.loc[mask, text] = compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)
        featured_data[text] = fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii ale unui cal
featured_data['Horse winning %'] = compute_horse_win_percentage(featured_data)
featured_data['Horse winning %'] = featured_data.groupby('HorseId')['Horse winning %'].fillna(method='ffill').fillna(0)

featured_data = featured_data.drop(columns='cumsum')
featured_data = featured_data.drop(columns='Win')
featured_data = featured_data.sort_values(by=['Dato', 'Løpsnr', 'Plassering'])
featured_data.to_excel('Date sortate.xlsx')
featured_data = pd.DataFrame()
del featured_data
