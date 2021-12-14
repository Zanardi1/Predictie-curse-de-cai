import computing as c
import filling as f
import pandas as pd
import returning as r
import datetime

start = datetime.datetime.now()

raw_data = pd.read_excel('Data.xlsx')
print(raw_data.shape)
print(raw_data.head())

featured_data = raw_data.copy()

# Calculez Last FGrating pentru fiecare cal
featured_data['Last FGrating'] = c.compute_last_fgrating(featured_data)
featured_data['Last FGrating'] = f.fill_for_all(featured_data, 'Last FGrating', 'HorseId')

# Calculez Last Final Position pentru fiecare cal
featured_data['Last Plassering'] = c.compute_last_final_position(featured_data)
featured_data['Last Plassering'] = f.fill_for_all(featured_data, 'Last Plassering', 'HorseId')

# Calculez Last FGrating pentru cele trei piste, respectiv pentru fiecare distanta, ambele pentru fiecare cal
c.compute_last_fgratings_with_conditions(featured_data)

# Calculez pozitia finala pentru cele trei piste, respectiv pentru fiecare distanta, ambele pentru fiecare cal
c.compute_last_final_positions_with_conditions(featured_data)

# Calculez FGrating mediu total al fiecarui cal
featured_data['Average FGrating'] = c.compute_average_fg_rating(featured_data)
featured_data['Average FGrating'] = f.fill_for_all(featured_data, 'Average FGrating', 'HorseId')

# Calculez pozitia medie totala pe fiecare cal
featured_data['Average Position'] = c.compute_average_position(featured_data)
featured_data['Average Position'] = f.fill_for_all(featured_data, 'Average Position', 'HorseId')

# Calculez FGrating mediu in ultimele 10, respectiv 4 starturi pentru fiecare cal
for i in [10, 4]:
    text = 'Average FGrating in the last ' + str(i) + ' starts'
    featured_data[text] = c.compute_average_fgrating_in_last_starts(featured_data, i)
    featured_data[text] = f.fill_for_all(featured_data, text, 'HorseId')

# Calculez pozitia finala medie in ultimele 10, respectiv 4 starturi pentru fiecare cal
for i in [10, 4]:
    text = 'Average Position in the last ' + str(i) + 'starts'
    featured_data[text] = c.compute_average_position_in_last_starts(featured_data, i)
    featured_data[text] = f.fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating mediu pentru fiecare dintre cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
# pentru fiecare cal

for i in range(3):
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i, 'Average FGrating')
    featured_data[text] = c.compute_average_fg_rating(featured_data, mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'HorseId')

# Calculez pozitia medie pentru fiecare dinte cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
# pentru fiecare cal

for i in range(3):
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i, 'Average Position')
    featured_data[text] = c.compute_average_position(featured_data, mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating mediu pentru cele trei tipuri de distante pentru fiecare cal
for i in range(3):
    mask, text = r.return_mask_and_text_from_distance_types(featured_data, i, 'Average FGrating')
    featured_data[text] = c.compute_average_fg_rating(featured_data, mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'HorseId')

# Calculez pozitia medie pentru cele trei tipuri de distante pentru fiecare cal
for i in range(3):
    mask, text = r.return_mask_and_text_from_distance_types(featured_data, i, 'Average Position')
    featured_data[text] = c.compute_average_position(featured_data, mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating maxim pentru fiecare cal
featured_data['Maximum FGrating'] = c.compute_max_fg_rating(featured_data)
featured_data['Maximum FGrating'] = f.fill_for_all(featured_data, 'Maximum FGrating', 'HorseId')

# Calculez FGrating maxim pentru cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass, pentru fiecare cal
for i in range(3):
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i, 'Maximum FGrating')
    featured_data[text] = c.compute_max_fg_rating(featured_data, mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating maxim pentru cele trei tipuri de distante, pentru fiecare cal
for i in range(3):
    mask, text = r.return_mask_and_text_from_distance_types(featured_data, i, 'Maximum FGrating')
    featured_data[text] = c.compute_max_fg_rating(featured_data, mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'HorseId')

# Calculez FGrating maxim pentru fiecare cal din ultimele trei starturi
featured_data['Maximum FGrating in last 3 starts'] = featured_data.groupby('HorseId')['FGrating'].apply(
    lambda x: x.shift().expanding(min_periods=3).max())
featured_data['Maximum FGrating in last 3 starts'] = f.fill_for_all(featured_data, 'Maximum FGrating in last 3 starts',
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
    featured_data[text] = c.compute_trainer_win_percent_in_last_days(featured_data, time_length)
    featured_data[text] = f.fill_for_all(featured_data, text, 'TrainerID')

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile, pe cele trei tipuri de distante
for i in range(3):
    mask, text = r.return_mask_and_text_from_distance_types(featured_data, i, 'Trainer winning % in the last 1000 days')
    featured_data[text] = c.compute_trainer_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'TrainerID')

# Calculez procentajul de victorii ale unui antrenor, in ultimele 1000 de zile, pe cele trei piste
for i in range(3):
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i, 'Trainer winning % in the last 1000 days')
    featured_data[text] = c.compute_trainer_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'TrainerID')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile
featured_data['Jockey winning % in the last 1000 days'] = c.compute_jockey_win_percent_in_last_days(featured_data,
                                                                                                    '1000D')
featured_data['Jockey winning % in the last 1000 days'] = featured_data.groupby('JockeyId')[
    'Jockey winning % in the last 1000 days'].fillna(method='ffill').fillna(0)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe cele trei piste, precum si pe piste,
# dar indiferent de suprafata
for i in range(5):
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = c.compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare suprafata
for i in [0, 1]:
    mask, text = r.return_mask_and_text_from_surfaces(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = c.compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare pista
for i in range(3):
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = c.compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare tip de distanta
for i in range(3):
    mask, text = r.return_mask_and_text_from_distance_types(featured_data, i, 'Jockey winning % in the last 1000 days')
    featured_data[text] = c.compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile, pe cele trei tipuri de distante
# si pe cele doua tipuri de suprafete
for i in range(3):
    for j in range(2):
        mask, text = r.return_mask_and_text_from_distances_and_surfaces(featured_data, i, j,
                                                                        'Jockey winning % in the last 1000 days')
        featured_data[text] = c.compute_jockey_win_percent_in_last_days(featured_data, '1000D', mask=mask)
        featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile
featured_data[
    'Average Position of a jockey in the last 1000 days'] = c.compute_jockey_average_final_position_in_last_days(
    featured_data, '1000D')
featured_data['Average Position of a jockey in the last 1000 days'] = f.fill_for_all(featured_data,
                                                                                     'Average Position of a jockey in the last 1000 days',
                                                                                     'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele doua piste, indiferent de suprafata
for i in [3, 4]:
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i,
                                                    'Average Position of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = c.compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                         mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele doua suprafete
for i in range(2):
    mask, text = r.return_mask_and_text_from_surfaces(featured_data, i,
                                                      'Average Position of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = c.compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                         mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele 2 piste, inclusiv suprafetele
for i in range(3):
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i,
                                                    'Average Position of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = c.compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                         mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele trei tipuri de distante
for i in range(3):
    mask, text = r.return_mask_and_text_from_distance_types(featured_data, i,
                                                            'Average Position of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = c.compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                         mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele trei tipuri de distante si pe cele doua tipuri de suprafata
for i in range(3):
    for j in range(2):
        mask, text = r.return_mask_and_text_from_distances_and_surfaces(featured_data, i, j,
                                                                        'Average Position of a jockey in the last 1000 days')
        featured_data.loc[mask, text] = c.compute_jockey_average_final_position_in_last_days(featured_data, '1000D',
                                                                                             mask=mask)
        featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile
featured_data['Mean path of a jockey in the last 1000 days'] = \
    c.compute_jockey_mean_path_in_last_days(featured_data, '1000D')
featured_data['Mean path of a jockey in the last 1000 days'] = f.fill_for_all(featured_data,
                                                                              'Mean path of a jockey in the last 1000 days',
                                                                              'JockeyId')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de suprafata
for i in range(2):
    mask, text = r.return_mask_and_text_from_surfaces(featured_data, i, 'Mean path of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = c.compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de pista si suprafata
for i in range(3):
    mask, text = r.return_mask_and_text_from_tracks(featured_data, i, 'Mean path of a jockey in the last 1000 days')
    featured_data.loc[mask, text] = c.compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)
    featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de suprafata si distanta
for i in range(3):
    for j in range(2):
        mask, text = r.return_mask_and_text_from_distances_and_surfaces(featured_data, i, j,
                                                                        'Mean path of a jockey in the last 1000 days')
        featured_data.loc[mask, text] = c.compute_jockey_mean_path_in_last_days(featured_data, '1000D', mask=mask)
        featured_data[text] = f.fill_for_all(featured_data, text, 'JockeyId')

# Calculez procentajul de victorii ale unui cal
featured_data['Horse winning %'] = c.compute_horse_win_percentage(featured_data)
featured_data['Horse winning %'] = featured_data.groupby('HorseId')['Horse winning %'].fillna(method='ffill').fillna(0)

featured_data = featured_data.drop(columns='cumsum')
featured_data = featured_data.drop(columns='Win')
featured_data = featured_data.sort_values(by=['Dato', 'Løpsnr', 'Plassering'])
stop = datetime.datetime.now()
print(stop - start)
featured_data.to_excel('Date sortate.xlsx')
featured_data = pd.DataFrame()
del featured_data

stop2 = datetime.datetime.now()
print(stop2 - start)
