import pandas as pd

raw_data = pd.read_excel('Data.xlsx')
print(raw_data.shape)
print(raw_data.head())

featured_data = raw_data.copy()

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
featured_data['Maximum FGrating'] = featured_data.groupby('HorseId')['FGrating'].apply(
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

# Calculez daca o anumita cursa a fost varf de forma
featured_data['Top'] = ((featured_data['FGrating'] - featured_data['Maximum FGrating'] >= 4).map({True: 1, False: 0}))

# Calculez numarul de zile de la ultima cursa
featured_data['Days since last race'] = featured_data.groupby('HorseId')['Dato'].diff()

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.reset_index().groupby('TrainerID').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 90 de zile
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.reset_index().groupby('TrainerID').rolling('90D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 90 days'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 30 de zile
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.reset_index().groupby('TrainerID').rolling('30D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 30 days'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile la distanta de 1000 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 1000].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 1000 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distanta de 1200 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 1200].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 1200 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distanta de 1400 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 1400].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 1400 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distanta de 1600 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 1600].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 1600 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distanta de 1650 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 1650].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 1650 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distanta de 1800 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 1800].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 1800 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distanta de 2000 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 2000].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 2000 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distanta de 2200 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 2200].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 2200 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile pe distanta de 2400 de metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Distance == 2400].reset_index().groupby('TrainerID').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days on 2400 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile la Sha-Tin - iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'TrainerID').rolling('1000D', on='Dato').agg({'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index(
    'index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days at Sha Tin Grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile la Sha-Tin - pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'TrainerID').rolling('1000D', on='Dato').agg({'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index(
    'index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days at Sha Tin Dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile la Happy Valley - iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[
         (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'TrainerID').rolling('1000D', on='Dato').agg({'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index(
    'index').mul(100).round(2))
featured_data['Trainer winning % in the last 1000 days at Sha Tin Grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Sha Tin
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Track == 'Sha Tin'].reset_index().groupby('JockeyId').rolling('1000D',
                                                                                                   on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at Sha Tin'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Happy Valley
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Track == 'Happy Valley'].reset_index().groupby('JockeyId').rolling('1000D',
                                                                                                        on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at Happy Valley'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Surface == 'Gress'].reset_index().groupby('JockeyId').rolling('1000D',
                                                                                                   on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[featured_data.Surface == 'Dirt'].reset_index().groupby('JockeyId').rolling('1000D',
                                                                                                  on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Sha Tin - iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at Sha Tin Grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Sha Tin - pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Track == 'Sha Tin') & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at Sha Tin Dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe Happy Valley - iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[
         (featured_data.Track == 'Happy Valley') & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at Happy Valley Grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1000 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 1000].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1000 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1200 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 1200].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1200 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1400 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 1400].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1400 days at 1000 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1600 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 1600].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1600 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1650 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 1650].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1650 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1800 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 1800].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1800 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2000 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 2000].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2000 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2200 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 2200].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2200 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2400 metri
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (
    featured_data.loc[featured_data.Distance == 2400].reset_index().groupby('JockeyId').rolling('1000D', on='Dato').agg(
        {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2400 m'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1000 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1000) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1000 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1000 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1000) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1000 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1200 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1200) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1200 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1200 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1200) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1200 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1400 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1400) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1400 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1400 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1400) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1400 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1600 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1600) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1600 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1600 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1600) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1600 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1650 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1650) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1650 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1650 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1650) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1650 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1800 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1800) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1800 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 1800 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 1800) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 1800 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2000 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 2000) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2000 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2000 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 2000) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2000 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2200 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 2200) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2200 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2200 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 2200) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2200 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s  # Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2400 metri, pe iarba
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 2400) & (featured_data.Surface == 'Gress')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2400 m on grass'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe distanta de 2400 metri, pe pamant
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.loc[(featured_data.Distance == 2400) & (featured_data.Surface == 'Dirt')].reset_index().groupby(
    'JockeyId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Jockey winning % in the last 1000 days at 2400 m on dirt'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile
featured_data['Average Position of a jockey in the last 1000 days'] = \
    (featured_data.set_index('Dato').groupby(['JockeyId', pd.Grouper(freq='1000D')])['Plassering'].transform(
        lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Sha Tin
mask = featured_data['Track'].eq('Sha Tin')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days at Sha Tin'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Track', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Happy Valley
mask = featured_data['Track'].eq('Happy Valley')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days at Happy Valley'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Track', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba
mask = featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant
mask = featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Sha Tin - iarba
mask = featured_data['Track'].eq('Sha Tin') & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on Sha Tin grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Track', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Sha Tin - pamant
mask = featured_data['Track'].eq('Sha Tin') & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on Sha Tin dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Track', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe Happy Valley - iarba
mask = featured_data['Track'].eq('Happy Valley') & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on Happy Valley grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Track', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 1000 m
mask = featured_data['Distance'].eq(1000)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 1000 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 1200 m
mask = featured_data['Distance'].eq(1200)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 1200 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 1400 m
mask = featured_data['Distance'].eq(1400)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 1400 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 1200 m
mask = featured_data['Distance'].eq(1600)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 1600 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 1650 m
mask = featured_data['Distance'].eq(1650)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 1650 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 1800 m
mask = featured_data['Distance'].eq(1800)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 1800 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 2000 m
mask = featured_data['Distance'].eq(2000)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 2000 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 2200 m
mask = featured_data['Distance'].eq(2200)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 2200 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe distanta de 2400 m
mask = featured_data['Distance'].eq(2400)

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days on 2400 m'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1000 m
mask = featured_data['Distance'].eq(1000) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1000 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1200 m
mask = featured_data['Distance'].eq(1200) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1200 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1400 m
mask = featured_data['Distance'].eq(1400) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1400 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1600 m
mask = featured_data['Distance'].eq(1600) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1600 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1650 m
mask = featured_data['Distance'].eq(1650) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1650 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1800 m
mask = featured_data['Distance'].eq(1800) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1800 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 2000 m
mask = featured_data['Distance'].eq(2000) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 2000 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 2200 m
mask = featured_data['Distance'].eq(2200) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 2200 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe iarba, la 2400 m
mask = featured_data['Distance'].eq(2400) & featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 2400 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1000 m
mask = featured_data['Distance'].eq(1000) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1000 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1200 m
mask = featured_data['Distance'].eq(1200) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1200 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1400 m
mask = featured_data['Distance'].eq(1400) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1400 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1600 m
mask = featured_data['Distance'].eq(1600) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1600 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1650 m
mask = featured_data['Distance'].eq(1650) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1650 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1800 m
mask = featured_data['Distance'].eq(1800) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 1800 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 2000 m
mask = featured_data['Distance'].eq(2000) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 2000 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 2200 m
mask = featured_data['Distance'].eq(2200) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 2200 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe pamant, la 2400 m
mask = featured_data['Distance'].eq(2400) & featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Average Position of a jockey in the last 1000 days 2400 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Distance', pd.Grouper(freq='1000D')])[
         'Plassering'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile
featured_data['Mean path of a jockey in the last 1000 days'] = \
    (featured_data.set_index('Dato').groupby(['JockeyId', pd.Grouper(freq='1000D')])['Path'].transform(
        lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba
mask = featured_data['Surface'].eq('Gress')

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant
mask = featured_data['Surface'].eq('Dirt')

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe Sha Tin - iarba
mask = featured_data['Surface'].eq('Gress') & featured_data['Track'].eq('Sha Tin')

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on Sha Tin grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe Sha Tin - pamant
mask = featured_data['Surface'].eq('Dirt') & featured_data['Track'].eq('Sha Tin')

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on Sha Tin dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe Happy Valley - iarba
mask = featured_data['Surface'].eq('Gress') & featured_data['Track'].eq('Happy Valley')

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days on Happy Valley grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1000 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(1000)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1000 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1200 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(1200)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1200 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1400 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(1400)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1400 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1600 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(1600)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1600 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1650 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(1650)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1650 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 1800 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(1800)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1800 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 2000 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(2000)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 2000 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 2200 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(2200)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 2200 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe iarba, la 2400 m
mask = featured_data['Surface'].eq('Gress') & featured_data['Distance'].eq(2400)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 2400 m, grass'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1000 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(1000)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1000 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1200 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(1200)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1200 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1400 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(1400)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1400 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1600 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(1600)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1600 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1650 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(1650)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1650 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 1800 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(1800)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 1800 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 2000 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(2000)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 2000 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 2200 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(2200)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 2200 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez calea ('Path) medie a unui jocheu in ultimele 1000 de zile pe pamant, la 2400 m
mask = featured_data['Surface'].eq('Dirt') & featured_data['Distance'].eq(2400)

featured_data.loc[mask, 'Mean path of a jockey in the last 1000 days 2400 m, dirt'] = \
    (featured_data[mask].set_index('Dato').groupby(['JockeyId', 'Surface', pd.Grouper(freq='1000D')])[
         'Path'].transform(lambda x: x.expanding().mean()).to_numpy())

# Calculez procentajul de victorii ale unui cal
featured_data['Win'] = featured_data['Plassering'].eq(1)
s = (featured_data.reset_index().groupby('HorseId').rolling('1000D', on='Dato').agg(
    {'Win': 'mean', 'index': 'max'}).reset_index(drop=True).set_index('index').mul(100).round(2))
featured_data['Horse winning %'] = s
featured_data = featured_data.drop(columns='Win')
s = pd.DataFrame()
del s

featured_data.to_excel('Date sortate.xlsx')
featured_data = pd.DataFrame()
del featured_data
