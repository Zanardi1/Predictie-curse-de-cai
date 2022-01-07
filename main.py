import computing as c
import pandas as pd

featured_data = pd.read_excel('Data.xlsx')
print(featured_data.shape)
print(featured_data.head())

# Calculez Last FGrating pentru fiecare cal
c.compute_last_fgratings_without_conditions(featured_data)

# Calculez Last Final Position pentru fiecare cal
c.compute_last_final_positions_without_conditions(featured_data)

# Calculez Last FGrating pentru cele trei piste, respectiv pentru fiecare distanta, ambele pentru fiecare cal
c.compute_last_fgratings_with_conditions(featured_data)

# Calculez pozitia finala pentru cele trei piste, respectiv pentru fiecare distanta, ambele pentru fiecare cal
c.compute_last_final_positions_with_conditions(featured_data)

# Calculez FGrating mediu total al fiecarui cal
c.compute_average_fgratings_without_conditions(featured_data)

# Calculez pozitia medie totala pe fiecare cal
c.compute_average_positions_without_conditions(featured_data)

# Calculez FGrating mediu in ultimele 10, respectiv 4 starturi pentru fiecare cal
c.compute_average_fgratings_in_the_last_10_or_4_starts(featured_data)

# Calculez pozitia finala medie in ultimele 10, respectiv 4 starturi pentru fiecare cal
c.compute_average_final_position_in_the_last_10_or_4_starts(featured_data)

# Calculez FGrating mediu pentru fiecare dintre cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
# pentru fiecare cal
c.compute_average_fgratings_for_every_track(featured_data)

# Calculez pozitia medie pentru fiecare dintre cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass
# pentru fiecare cal
c.compute_average_final_position_for_every_track(featured_data)

# Calculez FGrating mediu pentru cele trei tipuri de distante pentru fiecare cal
c.compute_average_fgratings_for_every_distance_type(featured_data)

# Calculez pozitia medie pentru cele trei tipuri de distante pentru fiecare cal
c.compute_average_final_position_for_every_distance_type(featured_data)

# Calculez FGrating maxim pentru fiecare cal
c.compute_max_fg_ratings_without_conditions(featured_data)

# Calculez FGrating maxim pentru cele trei piste:Sha Tin Grass, Sha Tin Dirt si Happy Valley Grass, pentru fiecare cal
c.compute_maximum_fgratings_for_every_track(featured_data)

# Calculez FGrating maxim pentru cele trei tipuri de distante, pentru fiecare cal
c.compute_maximum_fgratings_for_every_distance_type(featured_data)

# Calculez FGrating maxim pentru fiecare cal din ultimele trei starturi
c.compute_maximum_fgratings_in_the_last_3_starts(featured_data)

# Calculez daca un cal a fost varf de forma intr-o anumita cursa
c.compute_top_for_horse(featured_data)

# Calculez numarul de zile de la ultima cursa pentru fiecare cal
c.compute_days_since_last_race(featured_data)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000, 90, respectiv 30 de zile
c.compute_trainer_win_percent_in_the_last_days(featured_data)

# Calculez procentajul de victorii ale unui antrenor in ultimele 1000 de zile, pe cele trei tipuri de distante
c.compute_trainer_win_percent_for_every_distance(featured_data)

# Calculez procentajul de victorii ale unui antrenor, in ultimele 1000 de zile, pe cele trei piste
c.compute_trainer_win_percent_for_every_track(featured_data)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile
c.compute_jockey_win_percent(featured_data)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe cele trei piste, precum si pe piste,
# dar indiferent de suprafata
c.compute_jockey_win_percent_on_tracks_with_and_without_surfaces(featured_data)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare suprafata
c.compute_jockey_win_percent_on_every_surface(featured_data)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare pista
c.compute_jockey_win_percent_on_every_track(featured_data)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile pe fiecare tip de distanta
c.compute_jockey_win_percent_on_every_distance(featured_data)

# Calculez procentajul de victorii al unui jocheu in ultimele 1000 de zile, pe cele trei tipuri de distante
# si pe cele doua tipuri de suprafete
c.compute_jockey_win_percent_on_distances_and_surfaces(featured_data)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile
c.compute_jockey_average_final_position(featured_data)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele doua piste, indiferent de suprafata
c.compute_jockey_average_final_position_on_tracks_disregarding_surfaces(featured_data)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele doua suprafete
c.compute_jockey_average_final_position_on_surfaces(featured_data)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele 2 piste, inclusiv suprafetele
c.compute_jockey_average_final_position_on_tracks_and_surfaces(featured_data)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele trei tipuri de distante
c.compute_jockey_average_final_position_for_every_distance_type(featured_data)

# Calculez pozitia finala medie a unui jocheu in ultimele 1000 de zile pe cele trei tipuri de distante si pe cele doua
# tipuri de suprafata
c.compute_jockey_average_final_position_on_tracks_and_surfaces(featured_data)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile
c.compute_jockey_mean_path(featured_data)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de suprafata
c.compute_jockey_mean_path_on_surface(featured_data)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de pista si suprafata
c.compute_jockey_mean_path_on_tracks_and_surfaces(featured_data)

# Calculez calea ('Path') medie a unui jocheu in ultimele 1000 de zile, in functie de suprafata si distanta
c.compute_jockey_mean_path_on_distances_and_surfaces(featured_data)

# Calculez procentajul de victorii ale unui cal
c.compute_horse_win_percent(featured_data)

featured_data = featured_data.drop(columns='cumsum')
featured_data = featured_data.drop(columns='Win')
featured_data = featured_data.sort_values(by=['Dato', 'Løpsnr', 'Plassering'])
featured_data.to_excel('Date sortate.xlsx')
featured_data = pd.DataFrame()
del featured_data
