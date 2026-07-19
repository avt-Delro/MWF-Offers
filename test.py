cols_to_hide = []

loc_code = 'fl'

list_loc_code = list(loc_code.upper())

for location in list_loc_code:
    if location == 'V':
        cols_to_hide.extend(['A', 'B', 'C'])
    if location == 'L':
        cols_to_hide.extend(['D', 'E', 'F'])
    if location == 'K':
        cols_to_hide.extend(['G', 'H', 'I'])
    if location == 'F':
        cols_to_hide.extend(['J', 'K', 'L'])
    
print(f'Columns to hide: {cols_to_hide}')