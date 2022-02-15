def return_columns_that_will_be_used(what_for, column_to_fill, text):
    columns = []
    if what_for == 'Tracks':
        columns = ['Track', 'Surface', column_to_fill, 'HorseId', text]
    elif what_for == 'Distances':
        columns = ['Distance', column_to_fill, 'HorseId', text]
    return columns


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


def return_track_from_text(text):
    return 'Sha Tin' if 'Sha Tin' in text else 'Happy Valley'


def return_surface_from_text(text):
    return 'Gress' if 'Grass' in text else 'Dirt'


def return_track_and_surface_from_text(text):
    track = return_track_from_text(text)
    surface = return_surface_from_text(text)
    return track, surface


def return_distance_from_text(df, text):
    for distance in df['Distance'].unique():
        if str(distance) in text:
            return distance
