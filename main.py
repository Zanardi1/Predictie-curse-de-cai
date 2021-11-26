import pandas as pd

distances_list = [1000, 1200, 1400, 1600, 1650, 1800, 2000, 2200, 2400]

raw_data = pd.read_excel('Data.xlsx')
print(raw_data.shape)
print(raw_data.head())

featured_data = raw_data.copy()


def compute_last_fgrating(data, mask=''):
    if len(mask) == 0:
        return data.groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))
    else:
        return data.loc[mask][['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))


def compute_last_final_position(data, mask=''):
    if len(mask) == 0:
        return data.groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))
    else:
        return data.loc[mask][['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))


def compute_average_fgrating_in_last_starts(data, no_starts):
    return data.groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding(min_periods=no_starts).mean())


def compute_average_position_in_last_starts(data, no_starts):
    return data.groupby('HorseId')['Plassering'].apply(lambda x: x.shift().expanding(min_periods=no_starts).mean())


def compute_average_fg_rating(data, mask=''):
    if len(mask) == 0:
        temp = data.groupby('HorseId')['FGrating']
        data['cumsum'] = temp.apply(lambda p: p.shift(fill_value=0).cumsum())
        return data['cumsum'] / temp.cumcount()
    else:
        return data.loc[mask].groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding().mean())


def compute_average_position(data, mask=''):
    if len(mask) == 0:
        temp = data.groupby('HorseId')['Plassering']
        data['cumsum'] = temp.apply(lambda p: p.shift(fill_value=0).cumsum())
        return data['cumsum'] / temp.cumcount()
    else:
        return data.loc[mask].groupby('HorseId')['Plassering'].apply(lambda x: x.shift().expanding().mean())


def compute_max_fg_rating(data, mask=''):
    if len(mask) == 0:
        return data.groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding().max())
    else:
        return data.loc[mask].groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding().max())


def compute_trainer_win_percent_in_last_days(data, no_days, mask=''):
    if len(mask) == 0:
        data['Win'] = featured_data['Plassering'].eq(1)
        s = (data.reset_index().groupby('TrainerID').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
        data = data.drop(columns='Win')
    else:
        data['Win'] = data['Plassering'].eq(1)
        s = (data.loc[mask].reset_index().groupby('TrainerID').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
        data = data.drop(columns='Win')
    return s


def compute_jockey_win_percent_in_last_days(data, no_days, mask=''):
    if len(mask) == 0:
        data['Win'] = data['Plassering'].eq(1)
        s = (data.reset_index().groupby('JockeyId').rolling(no_days, on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
        data = data.drop(columns='Win')
    else:
        data['Win'] = data['Plassering'].eq(1)
        s = (data.loc[mask].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
            {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
        data = data.drop(columns='Win')
    return s


def compute_jockey_average_final_position_in_last_days(data, no_days, mask=''):
    if len(mask) == 0:
        return (data.set_index('Dato').groupby(['JockeyId', pd.Grouper(freq=no_days)])['Plassering'].transform(
            lambda x: x.expanding().mean()).to_numpy())
    else:
        return (data[mask].set_index('Dato').groupby(['JockeyId', 'Track', pd.Grouper(freq=no_days)])[
                    'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())


def compute_jockey_mean_path_in_last_days(data, no_days, mask=''):
    if len(mask) == 0:
        return data.set_index('Dato').groupby(['JockeyId', pd.Grouper(freq='1000D')])['Path'].transform(
            lambda x: x.expanding().mean()).to_numpy()
    else:
        return data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
            'Path'].transform(lambda x: x.expanding().mean()).to_numpy()


def compute_horse_win_percentage(data):
    data['Win'] = data['Plassering'].eq(1)
    s = (data.reset_index().groupby('HorseId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
    data = data.drop(columns='Win')
    return s


def return_mask_and_text_from_tracks(data, track_no, metric):
    if track_no == 0:  # Sha Tin - iarba
        mask = (data.Track == 'Sha Tin') & (data.Surface == 'Gress')
        text = str(metric) + ' at Sha-Tin Grass'
    if track_no == 1:  # Sha Tin - pamant
        mask = (data.Track == 'Sha Tin') & (data.Surface == 'Dirt')
        text = str(metric) + ' at Sha-Tin Dirt'
    if track_no == 2:  # Happy Valley - iarba
        mask = (data.Track == 'Happy Valley') & (data.Surface == 'Gress')
        text = str(metric) + ' at Happy Valley Grass'
    if track_no == 3:  # Sha Tin, indiferent de suprafata
        mask = data.Track == 'Sha Tin'
        text = str(metric) + ' at Sha-Tin'
    if track_no == 4:  # Happy Valley, indiferent de suprafata
        mask = data.Track == 'Happy Valley'
        text = str(metric) + ' at Happy Valley'
    return mask, text


def return_mask_and_text_from_distances(data, distance_type, metric):
    if distance_type == 0:  # Distante de sprint
        mask = (data.Distance == 1000) | (data.Distance == 1200)
        text = str(metric) + ' at sprint distances'
    if distance_type == 1:  # Distanta medie
        mask = (data.Distance == 1400) | (data.Distance == 1600) | (data.Distance == 1650) | (data.Distance == 1800)
        text = str(metric) + ' at medium distances'
    if distance_type == 2:  # Distante lungi
        mask = (data.Distance == 2000) | (data.Distance == 2200) | (data.Distance == 2400)
        text = str(metric) + ' at long distances'
    return mask, text


def return_mask_and_text_from_surfaces(data, surface_name, metric):
    if surface_name == 0:  # Iarba
        mask = data.Surface == 'Gress'
        text = str(metric) + ' on grass'
    if surface_name == 1:  # pamant
        mask = data.Surface == 'Dirt'
        text = str(metric) + ' on dirt'
    return mask, text


def return_mask_and_text_from_distances_and_surfaces(data, distance, surface_type, metric):
    if distance == 0:  # Distante scurte
        if surface_type == 0:  # Pe iarba
            mask = ((data.Distance == 1000) | (data.Distance == 1200)) & (data.Surface == 'Gress')
            text = str(metric) + ' at sprint distances on grass'
        if surface_type == 1:  # Pe pamant
            mask = ((data.Distance == 1000) | (data.Distance == 1200)) & (data.Surface == 'Dirt')
            text = str(metric) + ' at sprint distances on dirt'
    if distance == 1:  # Distante medii
        if surface_type == 0:  # Pe iarba
            mask = ((data.Distance == 1400) | (data.Distance == 1600) | (data.Distance == 1650) | (
                    data.Distance == 1800)) & (data.Surface == 'Gress')
            text = str(metric) + ' at middle distances on grass'
        if surface_type == 1:  # Pe pamant
            mask = ((data.Distance == 1400) | (data.Distance == 1600) | (data.Distance == 1650) | (
                    data.Distance == 1800)) & (data.Surface == 'Dirt')
            text = str(metric) + ' at middle distances on dirt'
    if distance == 2:  # Distante lungi
        if surface_type == 0:  # Pe iarba
            mask = ((data.Distance == 2000) | (data.Distance == 2200) | (data.Distance == 2400)) & (
                    data.Surface == 'Gress')
            text = str(metric) + ' at long distance on grass'
        if surface_type == 1:  # Pe pamant
            mask = ((data.Distance == 2000) | (data.Distance == 2200) | (data.Distance == 2400)) & (
                    data.Surface == 'Dirt')
            text = str(metric) + ' at long distance on dirt'
    return mask, text


# Calculez Last FGrating total
featured_data['Last FGrating'] = compute_last_fgrating(featured_data)

# Calculez Last Final Position total
featured_data['Last Plassering'] = compute_last_final_position(featured_data)

# Calculez Last FGrating pentru fiecare dintre cele trei piste: Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Last FGrating')
    featured_data[text] = compute_last_fgrating(featured_data, mask=mask)

# Calculez pozitia finala pentru fiecare dintre cele trei piste: Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Final Position')
    featured_data[text] = compute_last_final_position(featured_data, mask=mask)

# Calculez Last FGrating pentru fiecare distanta
for distance in distances_list:
    mask = featured_data.Distance == distance
    text = 'Last FGRating at ' + str(distance) + ' m'
    featured_data[text] = compute_last_fgrating(featured_data, mask=mask)

# Calculez ultima pozitie finala pentru fiecare distanta
for distance in distances_list:
    mask = featured_data.Distance == distance
    text = 'Last Final Position at ' + str(distance) + ' m'
    featured_data[text] = compute_last_final_position(featured_data, mask=mask)

# Calculez FGrating mediu total al fiecarui cal
featured_data['Average FGrating'] = compute_average_fg_rating(featured_data)

# Calculez pozitia medie totala pe fiecare cal
featured_data['Average Position'] = compute_average_position(featured_data)

# Calculez FGrating mediu in ultimele 10, respectiv 4 starturi pentru fiecare cal
for i in [10, 4]:
    text = 'Average FGrating in the last ' + str(i) + ' starts'
    featured_data[text] = compute_average_fgrating_in_last_starts(featured_data, i)

# Calculez pozitia finala medie in ultimele 10, respectiv 4 starturi pentru fiecare cal
for i in [10, 4]:
    text = 'Average Position in the last ' + str(i) + 'starts'
    featured_data[text] = compute_average_position_in_last_starts(featured_data, i)

# Calculez FGrating mediu pentru fiecare dinte cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Average FGrating')
    featured_data[text] = compute_average_fg_rating(featured_data, mask=mask)

# Calculez pozitia medie pentru fiecare dinte cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Average Position')
    featured_data[text] = compute_average_position(featured_data, mask=mask)

# Calculez FGrating mediu pentru cele trei tipuri de distante pentru fiecare cal
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Average FGrating')
    featured_data[text] = compute_average_fg_rating(featured_data, mask=mask)

# Calculez pozitia medie pentru cele trei tipuri de distante pentru fiecare cal
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Average Position')
    featured_data[text] = compute_average_position(featured_data, mask=mask)

# Calculez FGrating maxim pentru fiecare cal
featured_data['Maximum FGrating'] = compute_max_fg_rating(featured_data)

# Calculez FGrating maxim pentru cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass, pentru fiecare cal
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Maximum FGrating')
    featured_data[text] = compute_max_fg_rating(featured_data, mask=mask)

# Calculez FGrating maxim pentru cele trei tipuri de distante, pentru fiecare cal
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Maximum FGrating')
    featured_data[text] = compute_max_fg_rating(featured_data, mask=mask)

# Calculez FGrating maxim pentru fiecare cal din ultimele trei starturi
featured_data['Maximum FGrating in last 3 starts'] = featured_data.groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding(min_periods=3).max())

# Calculez daca o anumita cursa a fost varf de forma
featured_data['Top'] = (
    (featured_data['FGrating'] - featured_data['Maximum FGrating'] >= 4).map({True: 1, False: 0}))

# Calculez numarul de zile de la ultima cursa
featured_data['Days since last race'] = featured_data.groupby('HorseId')['Dato'].diff()

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000, 90, respectiv 30 de zile
for i in [1000, 90, 30]:
    text = 'Trainer winning % in the last ' + str(i) + ' days'
    time_length = str(i) + 'D'
    featured_data[text] = compute_trainer_win_percent_in_last_days(featured_data, time_length)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile, pe cele trei distante
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Trainer winning % in the last 1000 days')
    featured_data[text] = compute_trainer_win_percent_in_last_days(featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii ale unui antrenor, in ultimele 1000 de zile, pe cele trei piste
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Trainer winning % in the last 1000 days')
    featured_data[text] = compute_trainer_win_percent_in_last_days(featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile
featured_data['Jockey winning % in the last 1000 days'] = compute_jockey_win_percent_in_last_days(featured_data,
                                                                                                  '1000D')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe cele trei piste, precum si pe piste,
# dar indiferent de suprafata
for i in range(5):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare suprafata
for i in [0, 1]:
    mask, text = return_mask_and_text_from_surfaces(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare pista
for i in range(3):
    mask, text = return_mask_and_text_from_tracks(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare distanta
for i in range(3):
    mask, text = return_mask_and_text_from_distances(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile, pe cele trei tipuri de distante si pe cele doua tipuri de suprafete
for i in range(3):
    for j in range(2):
        mask, text = return_mask_and_text_from_distances_and_surfaces(featured_data, i, j,
                                                                      'Jockey winning % in the last 1000 days')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile
featured_data[
    'Average Position of a jockey in the last 1000 days'] = compute_jockey_average_final_position_in_last_days(
    featured_data, '1000D')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Sha Tin
mask = featured_data['Track'].eq('Sha Tin')
featured_data.loc[
    mask, 'Average Position of a jockey in the last 1000 days at Sha Tin'] = compute_jockey_average_final_position_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Happy Valley
mask = featured_data['Track'].eq('Happy Valley')
featured_data.loc[
    mask, 'Average Position of a jockey in the last 1000 days at Happy Valley'] = compute_jockey_average_final_position_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba
mask = featured_data['Surface'].eq('Gress')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on grass'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant
mask = featured_data['Surface'].eq('Dirt')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on dirt'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Sha Tin - iarba
mask = featured_data['Track'].eq('Sha Tin') & featured_data['Surface'].eq('Gress')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on Sha Tin grass'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Sha Tin - pamant
mask = featured_data['Track'].eq('Sha Tin') & featured_data['Surface'].eq('Dirt')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on Sha Tin dirt'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Happy Valley - iarba
mask = featured_data['Track'].eq('Happy Valley') & featured_data['Surface'].eq('Gress')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on Happy Valley grass'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distante scurte
mask = (featured_data['Distance'].eq(1000)) | (featured_data['Distance'].eq(1200))
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days at sprint distances'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distante medii
mask = (featured_data['Distance'].eq(1400)) | (featured_data['Distance'].eq(1600)) | (
    featured_data['Distance'].eq(1650)) | (featured_data['Distance'].eq(1800))
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days at middle distances'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distante lungi
mask = (featured_data['Distance'].eq(2000)) | (featured_data['Distance']).eq(2200) | (featured_data['Distance']).eq(
    2400)
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 2000 m'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la distante scurte
mask = ((featured_data['Distance'].eq(1000)) | (featured_data['Distance'].eq(1200))) & (
    featured_data['Surface'].eq('Gress'))
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on sprint distances, grass'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la distante medii
mask = ((featured_data['Distance'].eq(1400)) | (featured_data['Distance']).eq(1600) | (
    featured_data['Distance'].eq(1650)) | (featured_data['Distance'].eq(1800))) & featured_data['Surface'].eq(
    'Gress')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on middle distances, grass'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la distante lungi
mask = (featured_data['Distance'].eq(2000) | (featured_data['Distance'].eq(2200)) | (
    featured_data['Distance'].eq(2400))) & featured_data['Surface'].eq('Gress')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on long distances, grass'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la distante scurte
mask = ((featured_data['Distance'].eq(1000)) | (featured_data['Distance'].eq(1200))) & featured_data['Surface'].eq(
    'Dirt')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on sprint distances, dirt'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la distante medii
mask = ((featured_data['Distance'].eq(1400)) | (featured_data['Distance'].eq(1600)) | (
    featured_data['Distance'].eq(1650)) | (featured_data['Distance'].eq(1800))) & featured_data['Surface'].eq('Dirt')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on middle distances, dirt'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la distante lungi
mask = ((featured_data['Distance'].eq(2000)) | (featured_data['Distance'].eq(2200)) | (
    featured_data['Distance'].eq(2400))) & featured_data['Surface'].eq('Dirt')
featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on long distances, dirt'] = \
    compute_jockey_average_final_position_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile
featured_data['Mean path of a jockey in the last 1000 days'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe iarba
mask = featured_data['Surface'].eq('Gress')
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on grass'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe pamant
mask = featured_data['Surface'].eq('Dirt')
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on dirt'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe Sha Tin - iarba
mask = featured_data['Surface'].eq('Gress') & featured_data['Track'].eq('Sha Tin')
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on Sha Tin grass'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe Sha Tin - pamant
mask = featured_data['Surface'].eq('Dirt') & featured_data['Track'].eq('Sha Tin')
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on Sha Tin dirt'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe Happy Valley - iarba
mask = featured_data['Surface'].eq('Gress') & featured_data['Track'].eq('Happy Valley')
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on Happy Valley grass'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe iarba, la distante de sprint
mask = featured_data['Surface'].eq('Gress') & (
        (featured_data['Distance'].eq(1000)) | (featured_data['Distance'].eq(1200)))
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on short distances, grass'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe iarba, la distante medii
mask = featured_data['Surface'].eq('Gress') & (
        (featured_data['Distance'].eq(1400)) | (featured_data['Distance'].eq(1600)) | (
    featured_data['Distance'].eq(1650)) | (featured_data['Distance'].eq(1800)))
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on middle distances, grass'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe iarba, la distante lungi
mask = featured_data['Surface'].eq('Gress') & (
        (featured_data['Distance'].eq(2000)) | (featured_data['Distance'].eq(2200)) | (
    featured_data['Distance'].eq(2400)))
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on long distances, grass'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe pamant, la distante scurte
mask = featured_data['Surface'].eq('Dirt') & (
        (featured_data['Distance'].eq(1000)) | (featured_data['Distance'].eq(1200)))
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on short distances, dirt'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe pamant, la distante medii
mask = featured_data['Surface'].eq('Dirt') & (
        (featured_data['Distance'].eq(1400)) | (featured_data['Distance'].eq(1600)) | (
    featured_data['Distance'].eq(1650)) | (featured_data['Distance'].eq(1800)))
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on middle distances, dirt'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile pe pamant, la distante lungi
mask = featured_data['Surface'].eq('Dirt') & (
        (featured_data['Distance'].eq(2000)) | (featured_data['Distance'].eq(2200)) | (
    featured_data['Distance'].eq(2400)))
featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on long distances, dirt'] = \
    compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii ale unui cal
featured_data['Horse winning %'] = compute_horse_win_percentage(featured_data)

featured_data = featured_data.drop(columns='cumsum')
featured_data = featured_data.sort_values(by=['Dato', 'Løpsnr', 'Plassering'])
featured_data.to_excel('Date sortate.xlsx')
featured_data = pd.DataFrame()
del featured_data
