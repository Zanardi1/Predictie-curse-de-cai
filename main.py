import pandas as pd

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
        pass
    else:
        return data.loc[mask].groupby('HorseId')['FGrating'].apply(lambda x: x.shift().expanding().mean())


def compute_average_position(data, mask=''):
    if len(mask) == 0:
        pass
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


# Calculez Last FGrating total
featured_data['Last FGrating'] = compute_last_fgrating(featured_data)

# Calculez Last Final Position total
featured_data['Last Plassering'] = compute_last_final_position(featured_data)

# Calculez Last FGrating pentru Sha-Tin - iarba
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')
featured_data['Last FGrating at Sha-Tin Grass'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru Sha-Tin - pamant
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')
featured_data['Last FGrating at Sha-Tin Dirt'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru Happy Valley - iarba
mask = (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')
featured_data['Last FGrating at Happy Valley Grass'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Pozitia finala pentru Sha-Tin - iarba
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')
featured_data['Last Final Position at Sha-Tin Grass'] = compute_last_final_position(featured_data, mask=mask)

# Calculez Pozitia finala pentru Sha-Tin - pamant
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')
featured_data['Last Final Position at Sha-Tin Dirt'] = compute_last_final_position(featured_data, mask=mask)

# Calculez Pozitia finala pentru Happy Valley - iarba
mask = (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')
featured_data['Last Final Position at Happy Valley Grass'] = compute_last_final_position(featured_data,
                                                                                         mask=mask)

# Calculez Last FGrating pentru distanta de 1000 m
mask = featured_data.Distance == 1000
featured_data['Last FGrating at 1000 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru distanta de 1200 m
mask = featured_data.Distance == 1200
featured_data['Last FGrating at 1200 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru distanta de 1400 m
mask = featured_data.Distance == 1400
featured_data['Last FGrating at 1400 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru distanta de 1600 m
mask = featured_data.Distance == 1600
featured_data['Last FGrating at 1600 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru distanta de 1650 m
mask = featured_data.Distance == 1650
featured_data['Last FGrating at 1650 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru distanta de 1800 m
mask = featured_data.Distance == 1800
featured_data['Last FGrating at 1800 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru distanta de 2000 m
mask = featured_data.Distance == 2000
featured_data['Last FGrating at 2000 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru distanta de 2200 m
mask = featured_data.Distance == 2200
featured_data['Last FGrating at 2200 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez Last FGrating pentru distanta de 2400 m
mask = featured_data.Distance == 2400
featured_data['Last FGrating at 2400 m'] = compute_last_fgrating(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 1000 m
mask = featured_data.Distance == 1000
featured_data['Last Final Position at 1000 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 1200 m
mask = (featured_data.Distance == 1200)
featured_data['Last Final Position at 1200 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 1400 m
mask = featured_data.Distance == 1400
featured_data['Last Final Position at 1400 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 1600 m
mask = featured_data.Distance == 1600
featured_data['Last Final Position at 1600 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 1650 m
mask = featured_data.Distance == 1650
featured_data['Last Final Position at 1650 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 1800 m
mask = featured_data.Distance == 1800
featured_data['Last Final Position at 1800 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 2000 m
mask = featured_data.Distance == 2000
featured_data['Last Final Position at 2000 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 2200 m
mask = featured_data.Distance == 2200
featured_data['Last Final Position at 2200 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez pozitia finala pentru distanta de 2400 m
mask = featured_data.Distance == 2400
featured_data['Last Final Position at 2400 m'] = compute_last_final_position(featured_data, mask=mask)

# Calculez FGrating mediu total al fiecarui cal
temp = featured_data.groupby('HorseId')['FGrating']
featured_data['cumsum'] = temp.apply(lambda p: p.shift(fill_value=0).cumsum())
featured_data['Average FGrating'] = featured_data['cumsum'] / temp.cumcount()
featured_data = featured_data.drop(columns='cumsum')
temp = pd.DataFrame()
del temp

# Calculez pozitia medie totala pe fiecare cal
temp = featured_data.groupby('HorseId')['Plassering']
featured_data['cumsum'] = temp.apply(lambda p: p.shift(fill_value=0).cumsum())
featured_data['Average Position'] = featured_data['cumsum'] / temp.cumcount()
featured_data = featured_data.drop(columns='cumsum')
temp = pd.DataFrame()
del temp

# Calculez FGrating mediu in ultimele 10 starturi pentru fiecare cal
featured_data['Average FGrating in the last 10 starts'] = compute_average_fgrating_in_last_starts(featured_data,
                                                                                                  10)

# Calculez pozitia finala madie in ultimele 10 starturi pentru fiecare cal
featured_data['Average Position in the last 10 starts'] = compute_average_position_in_last_starts(featured_data,
                                                                                                  10)

# Calculez FGrating mediu in ultimele 4 starturi pentru fiecare cal
featured_data['Average FGrating in the last 4 starts'] = compute_average_fgrating_in_last_starts(featured_data,
                                                                                                 4)

# Calculez pozitia finala madie in ultimele 4 starturi pentru fiecare cal
featured_data['Average Position in the last 4 starts'] = compute_average_position_in_last_starts(featured_data,
                                                                                                 4)

# Calculez FGrating mediu pentru Sha Tin - iarba, pentru fiecare cal
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')
featured_data['Average FGrating at Sha Tin Grass'] = compute_average_fg_rating(featured_data, mask=mask)

# Calculez FGrating mediu pentru Sha Tin - pamant, pentru fiecare cal
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')
featured_data['Average FGrating at Sha Tin Dirt'] = compute_average_fg_rating(featured_data, mask=mask)

# Calculez FGrating mediu pentru Happy Valley - iarba, pentru fiecare cal
mask = (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')
featured_data['Average FGrating at Happy Valley Grass'] = compute_average_fg_rating(featured_data, mask=mask)

# Calculez pozitia medie pentru Sha-Tin - iarba pentru fiecare cal
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')
featured_data['Average Position at Sha Tin Grass'] = compute_average_position(featured_data, mask=mask)

# Calculez pozitia medie pentru Sha-Tin - pamant pentru fiecare cal
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')
featured_data['Average Position at Sha Tin Dirt'] = compute_average_position(featured_data, mask=mask)

# Calculez pozitia medie pentru Happy Valley - iarba pentru fiecare cal
mask = (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')
featured_data['Average FGrating at Happy Valley Grass'] = compute_average_position(featured_data, mask=mask)

# Calculez FGrating mediu pentru distantele de sprint, pentru fiecare cal
mask = (featured_data.Distance == 1000) | (featured_data.Distance == 1200)
featured_data['Average FGrating at sprint distances'] = compute_average_fg_rating(featured_data, mask=mask)

# Calculez FGrating mediu pentru distantele medii, pentru fiecare cal
mask = (featured_data.Distance == 1400) | (featured_data.Distance == 1600) | (
        featured_data.Distance == 1650) | (
               featured_data.Distance == 1800)
featured_data['Average FGrating at medium distances'] = compute_average_fg_rating(featured_data, mask=mask)

# Calculez FGrating mediu pentru distantele mari, pentru fiecare cal
mask = (featured_data.Distance == 2000) | (featured_data.Distance == 2200) | (featured_data.Distance == 2400)
featured_data['Average FGrating at long distances'] = compute_average_fg_rating(featured_data, mask=mask)

# Calculez pozitia medie pentru distantele de sprint, pentru fiecare cal
mask = ((featured_data.Distance == 1000) | (featured_data.Distance == 1200))
featured_data['Average Position at sprint distances'] = compute_average_position(featured_data, mask=mask)

# Calculez pozitia medie pentru distantele medii, pentru fiecare cal
mask = (featured_data.Distance == 1400) | (featured_data.Distance == 1600) | (
        featured_data.Distance == 1650) | (
               featured_data.Distance == 1800)
featured_data['Average Position at medium distances'] = compute_average_position(featured_data, mask=mask)

# Calculez pozitia medie pentru distantele medii, pentru fiecare cal
mask = (featured_data.Distance == 2000) | (featured_data.Distance == 2200) | (featured_data.Distance == 2400)
featured_data['Average Position at long distances'] = compute_average_position(featured_data, mask=mask)

# Calculez FGrating maxim pentru fiecare cal
featured_data['Maximum FGrating'] = compute_max_fg_rating(featured_data)

# Calculez FGrating maxim pentru Sha-Tin - iarba
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')
featured_data['Maximum FGrating at Sha Tin Grass'] = compute_max_fg_rating(featured_data, mask=mask)

# Calculez FGrating maxim pentru Sha-Tin - pamant
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')
featured_data['Maximum FGrating at Sha Tin Dirt'] = compute_max_fg_rating(featured_data, mask=mask)

# Calculez FGrating maxim pentru Happy Valley - iarba
mask = (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')
featured_data['Maximum FGrating at Happy Valley Grass'] = compute_max_fg_rating(featured_data, mask=mask)

# Calculez FGrating maxim pentru distante de sprint
mask = (featured_data.Distance == 1000) | (featured_data.Distance == 1200)
featured_data['Maximum FGrating at sprint distances'] = compute_max_fg_rating(featured_data, mask=mask)

# Calculez FGrating maxim pentru distante medii
mask = (featured_data.Distance == 1400) | (featured_data.Distance == 1600) | (
        featured_data.Distance == 1650) | (
               featured_data.Distance == 1800)
featured_data['Maximum FGrating at medium distances'] = compute_max_fg_rating(featured_data, mask=mask)

# Calculez FGrating maxim pentru distante lungi
mask = (featured_data.Distance == 2000) | (featured_data.Distance == 2200) | (featured_data.Distance == 2400)
featured_data['Maximum FGrating at long distances'] = compute_max_fg_rating(featured_data, mask=mask)

# Calculez FGrating maxim pentru fiecare cal din ultimele trei starturi
featured_data['Maximum FGrating in last 3 starts'] = featured_data.groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding(min_periods=3).max())

# Calculez daca o anumita cursa a fost varf de forma
featured_data['Top'] = (
    (featured_data['FGrating'] - featured_data['Maximum FGrating'] >= 4).map({True: 1, False: 0}))

# Calculez numarul de zile de la ultima cursa
featured_data['Days since last race'] = featured_data.groupby('HorseId')['Dato'].diff()

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile
featured_data['Trainer winning % in the last 1000 days'] = compute_trainer_win_percent_in_last_days(featured_data,
                                                                                                    '1000D')
# Calculez procentajul de victorii ale unui antrenor in ultimele 90 de zile
featured_data['Trainer winning % in the last 90 days'] = compute_trainer_win_percent_in_last_days(featured_data,
                                                                                                  '90D')

# Calculez procentajul de victorii ale unui antrenor in ultimele 30 de zile
featured_data['Trainer winning % in the last 30 days'] = compute_trainer_win_percent_in_last_days(featured_data,
                                                                                                  '30D')

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distante de sprint
mask = (featured_data.Distance == 1000) | (featured_data.Distance == 1200)
featured_data[
    'Trainer winning % in the last 1000 days at sprint distances'] = compute_trainer_win_percent_in_last_days(

    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distante medii
mask = (featured_data.Distance == 1400) | (featured_data.Distance == 1600) | (featured_data.Distance == 1650) | (
        featured_data.Distance == 1800)
featured_data['Trainer winning % in the last 1000 days at middle distances'] = compute_trainer_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distante lungi
mask = (featured_data.Distance == 2000) | (featured_data.Distance == 2200) | (
        featured_data.Distance == 2400)
featured_data['Trainer winning % in the last 1000 days at long distances'] = compute_trainer_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile la Sha-Tin - iarba
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')
featured_data['Trainer winning % in the last 1000 days at Sha Tin Grass'] = compute_trainer_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile la Sha-Tin - pamant
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')
featured_data['Trainer winning % in the last 1000 days at Sha Tin Dirt'] = compute_trainer_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile la Happy Valley - iarba
mask = (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')
featured_data['Trainer winning % in the last 1000 days at Sha Tin Grass'] = compute_trainer_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile
featured_data['Jockey winning % in the last 1000 days'] = compute_jockey_win_percent_in_last_days(featured_data,
                                                                                                  '1000D')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Sha Tin
mask = featured_data.Track == 'Sha Tin'
featured_data['Jockey winning % in the last 1000 days at Sha Tin'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Happy Valley
mask = featured_data.Track == 'Happy Valley'
featured_data['Jockey winning % in the last 1000 days at Happy Valley'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe iarba
mask = featured_data.Surface == 'Gress'
featured_data['Jockey winning % in the last 1000 days on grass'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe pamant
mask = featured_data.Surface == 'Dirt'
featured_data['Jockey winning % in the last 1000 days on dirt'] = compute_jockey_win_percent_in_last_days(featured_data,
                                                                                                          '1000D',
                                                                                                          mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Sha Tin - iarba
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')
featured_data['Jockey winning % in the last 1000 days at Sha Tin Grass'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Sha Tin - pamant
mask = (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')
featured_data['Jockey winning % in the last 1000 days at Sha Tin Dirt'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Happy Valley - iarba
mask = (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')
featured_data['Jockey winning % in the last 1000 days at Happy Valley Grass'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante de sprint
mask = (featured_data.Distance == 1000) | (featured_data.Distance == 1200)
featured_data['Jockey winning % in the last 1000 days at sprint distances'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante medii
mask = (featured_data.Distance == 1400) | (featured_data.Distance == 1600) | (featured_data.Distance == 1650) | (
        featured_data.Distance == 1800)
featured_data['Jockey winning % in the last 1000 days at middle distances'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante lungi
mask = (featured_data.Distance == 2000) | (featured_data.Distance == 2200) | (
        featured_data.Distance == 2400)
featured_data['Jockey winning % in the last 1000 days at long distances'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante scurte, pe iarba
mask = ((featured_data.Distance == 1000) | (featured_data.Distance == 1200)) & (
        featured_data.Surface == 'Gress')
featured_data[
    'Jockey winning % in the last 1000 days at sprint distances on grass'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante scurte, pe pamant
mask = ((featured_data.Distance == 1000) | (featured_data.Distance == 1200)) & (
        featured_data.Surface == 'Dirt')
featured_data['Jockey winning % in the last 1000 days at 1000 m on dirt'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante medii, pe iarba
mask = ((featured_data.Distance == 1400) | (featured_data.Distance == 1600) | (featured_data.Distance == 1650) | (
        featured_data.Distance == 1800)) & (featured_data.Surface == 'Gress')
featured_data[
    'Jockey winning % in the last 1000 days at middle distances on grass'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante medii, pe pamant
mask = ((featured_data.Distance == 1400) | (featured_data.Distance == 1600) | (featured_data.Distance == 1650) | (
        featured_data.Distance == 1800)) & (featured_data.Surface == 'Dirt')
featured_data[
    'Jockey winning % in the last 1000 days at middle distances on dirt'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante lungi, pe iarba
mask = ((featured_data.Distance == 2000) | (featured_data.Distance == 2200) | (featured_data.Distance == 2400)) & (
        featured_data.Surface == 'Gress')
featured_data[
    'Jockey winning % in the last 1000 days at long distance on grass'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distante lungi, pe pamant
mask = ((featured_data.Distance == 2000) | (featured_data.Distance == 2200) | (featured_data.Distance == 2400)) & (
        featured_data.Surface == 'Dirt')
featured_data[
    'Jockey winning % in the last 1000 days at long distance on dirt'] = compute_jockey_win_percent_in_last_days(
    featured_data, '1000D', mask=mask)

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

featured_data = featured_data.sort_values(by=['Dato', 'Løpsnr', 'Plassering'])
featured_data.to_excel('Date sortate.xlsx')
featured_data = pd.DataFrame()
del featured_data
