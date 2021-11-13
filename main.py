import pandas as pd

raw_data = pd.read_excel('Data.xlsx')
print(raw_data.shape)
print(raw_data.head())

featured_data = raw_data

# Calculez Last FGrating total
featured_data['Last FGrating'] = featured_data.groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last Final Position total
featured_data['Last Plassering'] = featured_data.groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru Sha-Tin - iarba
featured_data['Last FGrating at Sha-Tin Grass'] = \
    featured_data.loc[(featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')][
        ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru Sha-Tin - pamant
featured_data['Last FGrating at Sha-Tin Dirt'] = featured_data.loc[
    (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')][['HorseId', 'FGrating']].groupby('HorseId')[
    'FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru Happy Valley - iarba
featured_data['Last FGrating at Happy Valley Grass'] = featured_data.loc[
    (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')][['HorseId', 'FGrating']].groupby(
    'HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Pozitia finala pentru Sha-Tin - iarba
featured_data['Last Final Position at Sha-Tin Grass'] = \
    featured_data.loc[(featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')][
        ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez Pozitia finala pentru Sha-Tin - pamant
featured_data['Last Final Position at Sha-Tin Dirt'] = featured_data.loc[
    (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')][['HorseId', 'Plassering']].groupby(
    'HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez Pozitia finala pentru Happy Valley - iarba
featured_data['Last Final Position at Happy Valley Grass'] = featured_data.loc[
    (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')][['HorseId', 'Plassering']].groupby(
    'HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 1000 m
featured_data['Last FGrating at 1000 m'] = featured_data.loc[(featured_data.Distance == 1000)][
    ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 1200 m
featured_data['Last FGrating at 1200 m'] = \
    featured_data.loc[(featured_data.Distance == 1200)][['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 1400 m
featured_data['Last FGrating at 1400 m'] = featured_data.loc[(featured_data.Distance == 1400)][
    ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 1600 m
featured_data['Last FGrating at 1600 m'] = featured_data.loc[featured_data.Distance == 1600][
    ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 1650 m
featured_data['Last FGrating at 1650 m'] = featured_data.loc[featured_data.Distance == 1650][
    ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 1800 m
featured_data['Last FGrating at 1800 m'] = featured_data.loc[featured_data.Distance == 1800][
    ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 2000 m
featured_data['Last FGrating at 2000 m'] = featured_data.loc[featured_data.Distance == 2000][
    ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 2200 m
featured_data['Last FGrating at 2200 m'] = featured_data.loc[featured_data.Distance == 2200][
    ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez Last FGrating pentru distanta de 2400 m
featured_data['Last FGrating at 2400 m'] = featured_data.loc[featured_data.Distance == 2400][
    ['HorseId', 'FGrating']].groupby('HorseId')['FGrating'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 1000 m
featured_data['Last Final Position at 1000 m'] = featured_data.loc[(featured_data.Distance == 1000)][
    ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 1200 m
featured_data['Last Final Position at 1200 m'] = \
    featured_data.loc[(featured_data.Distance == 1200)][['HorseId', 'Plassering']].groupby('HorseId')[
        'Plassering'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 1400 m
featured_data['Last Final Position at 1400 m'] = featured_data.loc[(featured_data.Distance == 1400)][
    ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 1600 m
featured_data['Last Final Position at 1600 m'] = featured_data.loc[featured_data.Distance == 1600][
    ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 1650 m
featured_data['Last Final Position at 1650 m'] = featured_data.loc[featured_data.Distance == 1650][
    ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 1800 m
featured_data['Last Final Position at 1800 m'] = featured_data.loc[featured_data.Distance == 1800][
    ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 2000 m
featured_data['Last Final Position at 2000 m'] = featured_data.loc[featured_data.Distance == 2000][
    ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 2200 m
featured_data['Last Final Position at 2200 m'] = featured_data.loc[featured_data.Distance == 2200][
    ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

# Calculez pozitia finala pentru distanta de 2400 m
featured_data['Last Final Position at 2400 m'] = featured_data.loc[featured_data.Distance == 2400][
    ['HorseId', 'Plassering']].groupby('HorseId')['Plassering'].apply(lambda x: x.shift(1))

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
featured_data['Average FGrating in the last 10 starts'] = featured_data.groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding(min_periods=10).mean())

# Calculez pozitia finala madie in ultimele 10 starturi pentru fiecare cal
featured_data['Average Position in the last 10 starts'] = featured_data.groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding(min_periods=10).mean())

# Calculez FGrating mediu in ultimele 4 starturi pentru fiecare cal
featured_data['Average FGrating in the last 4 starts'] = featured_data.groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding(min_periods=4).mean())

# Calculez pozitia finala madie in ultimele 4 starturi pentru fiecare cal
featured_data['Average Position in the last 4 starts'] = featured_data.groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding(min_periods=4).mean())

# Calculez FGrating mediu pentru Sha Tin - iarba, pentru fiecare cal
featured_data['Average FGrating at Sha Tin Grass'] = featured_data.loc[
    (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru Sha Tin - pamant, pentru fiecare cal
featured_data['Average FGrating at Sha Tin Dirt'] = featured_data.loc[
    (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru Happy Valley - iarba, pentru fiecare cal
featured_data['Average FGrating at Happy Valley Grass'] = featured_data.loc[
    (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru Sha-Tin - iarba pentru fiecare cal
featured_data['Average Position at Sha Tin Grass'] = featured_data.loc[
    (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru Sha-Tin - pamant pentru fiecare cal
featured_data['Average Position at Sha Tin Dirt'] = featured_data.loc[
    (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru Happy Valley - iarba pentru fiecare cal
featured_data['Average Position at Happy Valley Grass'] = featured_data.loc[
    (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')].groupby('HorseId')[
    'Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 1000 m, pentru fiecare cal
featured_data['Average FGrating at 1000 m'] = featured_data.loc[
    (featured_data.Distance == 1000)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 1200 m, pentru fiecare cal
featured_data['Average FGrating at 1200 m'] = featured_data.loc[
    (featured_data.Distance == 1200)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 1400 m, pentru fiecare cal
featured_data['Average FGrating at 1400 m'] = featured_data.loc[
    (featured_data.Distance == 1400)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 1600 m, pentru fiecare cal
featured_data['Average FGrating at 1600 m'] = featured_data.loc[
    (featured_data.Distance == 1600)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 1650 m, pentru fiecare cal
featured_data['Average FGrating at 1650 m'] = featured_data.loc[
    (featured_data.Distance == 1650)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 1800 m, pentru fiecare cal
featured_data['Average FGrating at 1800 m'] = featured_data.loc[
    (featured_data.Distance == 1800)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 2000 m, pentru fiecare cal
featured_data['Average FGrating at 2000 m'] = featured_data.loc[
    (featured_data.Distance == 2000)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 2200 m, pentru fiecare cal
featured_data['Average FGrating at 2200 m'] = featured_data.loc[
    (featured_data.Distance == 2200)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating mediu pentru distanta de 2400 m, pentru fiecare cal
featured_data['Average FGrating at 2400 m'] = featured_data.loc[
    (featured_data.Distance == 2400)].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 1000 m, pentru fiecare cal
featured_data['Average Position at 1000 m'] = featured_data.loc[
    (featured_data.Distance == 1000)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 1200 m, pentru fiecare cal
featured_data['Average Position at 1200 m'] = featured_data.loc[
    (featured_data.Distance == 1200)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 1400 m, pentru fiecare cal
featured_data['Average Position at 1400 m'] = featured_data.loc[
    (featured_data.Distance == 1400)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 1600 m, pentru fiecare cal
featured_data['Average Position at 1600 m'] = featured_data.loc[
    (featured_data.Distance == 1600)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 1650 m, pentru fiecare cal
featured_data['Average Position at 1650 m'] = featured_data.loc[
    (featured_data.Distance == 1650)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 1800 m, pentru fiecare cal
featured_data['Average Position at 1800 m'] = featured_data.loc[
    (featured_data.Distance == 1800)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 2000 m, pentru fiecare cal
featured_data['Average Position at 2000 m'] = featured_data.loc[
    (featured_data.Distance == 2000)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 2200 m, pentru fiecare cal
featured_data['Average Position at 2200 m'] = featured_data.loc[
    (featured_data.Distance == 2200)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez pozitia medie pentru distanta de 2400 m, pentru fiecare cal
featured_data['Average Position at 2400 m'] = featured_data.loc[
    (featured_data.Distance == 2400)].groupby('HorseId')['Plassering'].apply(
    lambda x: x.shift().expanding().mean())

# Calculez FGrating maxim pentru fiecare cal
featured_data['Maximum FGrating '] = featured_data.groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru Sha-Tin - iarba
featured_data['Maximum FGrating at Sha Tin Grass'] = featured_data.loc[
    (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru Sha-Tin - pamant
featured_data['Maximum FGrating at Sha Tin Dirt'] = featured_data.loc[
    (featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru Happy Valley - iarba
featured_data['Maximum FGrating at Happy Valley Grass'] = featured_data.loc[
    (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')].groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 1000 m
featured_data['Maximum FGrating at 1000 m'] = \
    featured_data.loc[featured_data.Distance == 1000].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 1200 m
featured_data['Maximum FGrating at 1200 m'] = \
    featured_data.loc[featured_data.Distance == 1200].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 1400 m
featured_data['Maximum FGrating at 1400 m'] = \
    featured_data.loc[featured_data.Distance == 1400].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 1600 m
featured_data['Maximum FGrating at 1600 m'] = \
    featured_data.loc[featured_data.Distance == 1600].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 1650 m
featured_data['Maximum FGrating at 1650 m'] = \
    featured_data.loc[featured_data.Distance == 1650].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 1800 m
featured_data['Maximum FGrating at 1800 m'] = \
    featured_data.loc[featured_data.Distance == 1800].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 2000 m
featured_data['Maximum FGrating at 2000 m'] = \
    featured_data.loc[featured_data.Distance == 2000].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 2200 m
featured_data['Maximum FGrating at 2200 m'] = \
    featured_data.loc[featured_data.Distance == 2200].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru distanta de 2400 m
featured_data['Maximum FGrating at 2400 m'] = \
    featured_data.loc[featured_data.Distance == 2400].groupby('HorseId')['FGrating'].apply(
        lambda x: x.shift().expanding().max())

# Calculez FGrating maxim pentru fiecare cal din ultimele trei starturi
featured_data['Maximum FGrating in last 3 starts'] = featured_data.groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding(min_periods=3).max())

featured_data.to_excel('Date sortate.xlsx')
featured_data = pd.DataFrame()
del featured_data
