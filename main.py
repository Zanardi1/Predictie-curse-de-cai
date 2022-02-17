import datetime as dt

import computing as c
import pandas as pd

featured_data = pd.read_excel('Data.xlsx')
print(featured_data.shape)
print(featured_data.head())
featured_data = featured_data.sort_values(by=['Dato', 'Løpsnr', 'Plassering'])
featured_data = featured_data.reset_index(drop=True)

begin = dt.datetime.now()
print('Calculez Last FGrating pentru fiecare cal. Ora: ', begin)
c.compute_last_fgratings_without_conditions(featured_data)

print('Calculez Last Final Position pentru fiecare cal. Ora: ', dt.datetime.now())
c.compute_last_final_positions_without_conditions(featured_data)

print(
    'Calculez Last FGrating pentru cele trei piste, respectiv pentru fiecare distanta, ambele pentru fiecare cal. Ora: ',
    dt.datetime.now())
c.compute_last_fgratings_with_conditions(featured_data)

print(
    'Calculez pozitia finala pentru cele trei piste, respectiv pentru fiecare distanta, ambele pentru fiecare cal. Ora: ',
    dt.datetime.now())
c.compute_last_final_positions_with_conditions(featured_data)

print('Calculez FGrating mediu total al fiecarui cal. Ora: ', dt.datetime.now())
c.compute_average_fgratings_without_conditions(featured_data)

print('Calculez pozitia medie totala pe fiecare cal. Ora: ', dt.datetime.now())
c.compute_average_positions_without_conditions(featured_data)

print('Calculez FGrating mediu in ultimele 10, respectiv 4 starturi pentru fiecare cal. Ora: ', dt.datetime.now(),
      )
c.compute_average_fgratings_in_the_last_10_or_4_starts(featured_data)

print('Calculez pozitia finala medie in ultimele 10, respectiv 4 starturi pentru fiecare cal. Ora: ',
      dt.datetime.now())
c.compute_average_final_position_in_the_last_10_or_4_starts(featured_data)

print(
    'Calculez FGrating mediu pentru fiecare dintre cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass pentru fiecare cal. Ora: ',
    dt.datetime.now())
c.compute_average_fgratings_for_every_track(featured_data)

print(
    'Calculez pozitia medie pentru fiecare dintre cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass pentru fiecare cal. Ora: ',
    dt.datetime.now())
c.compute_average_final_position_for_every_track(featured_data)

print('Calculez FGrating mediu pentru cele trei tipuri de distante pentru fiecare cal. Ora: ', dt.datetime.now(),
      )
c.compute_average_fgratings_for_every_distance_type(featured_data)

print('Calculez pozitia medie pentru cele trei tipuri de distante pentru fiecare cal. Ora: ', dt.datetime.now())
c.compute_average_final_position_for_every_distance_type(featured_data)

print('Calculez FGrating maxim pentru fiecare cal. Ora: ', dt.datetime.now())
c.compute_max_fg_ratings_without_conditions(featured_data)

print(
    'Calculez FGrating maxim pentru cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass, pentru fiecare cal. Ora: ',
    dt.datetime.now())
c.compute_maximum_fgratings_for_every_track(featured_data)

print('Calculez FGrating maxim pentru cele trei tipuri de distante, pentru fiecare cal. Ora: ', dt.datetime.now())
c.compute_maximum_fgratings_for_every_distance_type(featured_data)

print('Calculez FGrating maxim pentru fiecare cal din ultimele trei starturi. Ora: ', dt.datetime.now())
c.compute_maximum_fgratings_in_the_last_3_starts(featured_data)

print('Calculez daca un cal a fost varf de forma intr-o anumita cursa. Ora: ', dt.datetime.now())
c.compute_top_for_horse(featured_data)

print('Calculez numarul de zile de la ultima cursa pentru fiecare cal. Ora: ', dt.datetime.now())
c.compute_days_since_last_race(featured_data)

print('Calculez procentajul de victorii ale unui antrenor in ultimele 1000, 90, respectiv 30 de zile. Ora: ',
      dt.datetime.now())
c.compute_trainer_win_percent_in_the_last_days(featured_data)

print(
    'Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile, pe cele trei tipuri de distante. Ora: ',
    dt.datetime.now())
c.compute_trainer_win_percent_for_every_distance(featured_data)

print('Calculez procentajul de victorii ale unui antrenor, in ultimele 1000 de zile, pe cele trei piste. Ora: ',
      dt.datetime.now())
c.compute_trainer_win_percent_for_every_track(featured_data)

print('Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile. Ora: ', dt.datetime.now())
c.compute_jockey_win_percent(featured_data)

print(
    'Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe cele trei piste, precum si pe piste, dar indiferent de suprafata. Ora: ',
    dt.datetime.now())
c.compute_jockey_win_percent_on_tracks_with_and_without_surfaces(featured_data)

print('Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare suprafata. Ora: ',
      dt.datetime.now())
c.compute_jockey_win_percent_on_every_surface(featured_data)

print('Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare pista. Ora: ',
      dt.datetime.now())
c.compute_jockey_win_percent_on_every_track(featured_data)

print('Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare tip de distanta. Ora: ',
      dt.datetime.now())
c.compute_jockey_win_percent_on_every_distance(featured_data)

print(
    'Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile, pe cele trei tipuri de distante si pe cele doua tipuri de suprafete. Ora: ',
    dt.datetime.now())
c.compute_jockey_win_percent_on_distances_and_surfaces(featured_data)

print('Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile. Ora: ', dt.datetime.now())
c.compute_jockey_average_final_position(featured_data)

print(
    'Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele doua piste, indiferent de suprafata. Ora: ',
    dt.datetime.now())
c.compute_jockey_average_final_position_on_tracks_disregarding_surfaces(featured_data)

print('Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele doua suprafete. Ora: ',
      dt.datetime.now())
c.compute_jockey_average_final_position_on_surfaces(featured_data)

print(
    'Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele 2 piste, inclusiv suprafetele. Ora: ',
    dt.datetime.now())
c.compute_jockey_average_final_position_on_tracks_and_surfaces(featured_data)

print('Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele trei tipuri de distante. Ora: ',
      dt.datetime.now())
c.compute_jockey_average_final_position_for_every_distance_type(featured_data)

print(
    'Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele trei tipuri de distante si pe cele doua tipuri de suprafata. Ora: ',
    dt.datetime.now())
c.compute_jockey_average_final_position_on_tracks_and_surfaces(featured_data)

print('Calculez pozitia medie de plecare ('"Path"') a unui jocheu in ultimele 1000 de zile. Ora: ', dt.datetime.now())
c.compute_jockey_mean_path(featured_data)

print(
    'Calculez pozitia medie de plecare ('"Path"') a unui jocheu in ultimele 1000 de zile, in functie de suprafata. Ora: ',
    dt.datetime.now())
c.compute_jockey_mean_path_on_surface(featured_data)

print(
    'Calculez pozitia medie de plecare ('"Path"') a unui jocheu in ultimele 1000 de zile, in functie de pista si suprafata. Ora: ',
    dt.datetime.now())
c.compute_jockey_mean_path_on_tracks_and_surfaces(featured_data)

print(
    'Calculez pozitia medie de plecare ('"Path"') a unui jocheu in ultimele 1000 de zile, in functie de suprafata si distanta. Ora: ',
    dt.datetime.now())
c.compute_jockey_mean_path_on_distances_and_surfaces(featured_data)

print('Calculez procentajul de victorii ale unui cal. Ora: ', dt.datetime.now())
c.compute_horse_win_percent(featured_data)

featured_data = featured_data.drop(columns='cumsum')
featured_data = featured_data.drop(columns='Index')
print('Generez fisierul cu rezultate. Ora: ', dt.datetime.now())
featured_data.to_excel('Date sortate.xlsx')
featured_data = pd.DataFrame()
del featured_data
end = dt.datetime.now()
print('Final. Ora: ', end)
print('Durata totala: ', end - begin)
