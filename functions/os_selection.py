def os_selection(row):
    if 'Windows' in row['os']:
         return 'Windows'
    elif 'Linux' in row['os']:
        return 'Linux'
    elif 'Macintosh' in row['os']:
        return 'Macintosh'
    elif 'iPhone' in row['os']:
        return 'iPhone'
    elif 'iPod' in row['os']:
        return 'iPod'
    elif 'Android' in row['os']:
        return 'Android'
    elif 'iPad' in row['os']:
        return 'iPad'
    else:
        return 'Other'