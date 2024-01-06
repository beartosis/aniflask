from calculations import CoatPattern


coat_patterns = [
    CoatPattern('black',     'Black',     'Legendary'   ),
    CoatPattern('blue',      'Blue',      'Rare'        ),
    CoatPattern('chocolate', 'Chocolate', 'Common'      ),
    CoatPattern('cream',     'Cream',     'Uncommon'    ),
    CoatPattern('fawn',      'Fawn',      'Uncommon'    ),
    CoatPattern('gold',      'Gold',      'Rare'        ),
    CoatPattern('gray',      'Gray',      'Common'      ),
    CoatPattern('lilac',     'Lilac',     'Rare'        ),
    CoatPattern('liver',     'Liver',     'Uncommon'    ),
    CoatPattern('red',       'Red',       'Legendary'   ),
    CoatPattern('white',     'White',     'Legendary'   ),
    CoatPattern('yellow',    'Yellow',    'Common'      ),
]


def match_patterns(selected_patterns, coat_patterns_list):
    matched_dictionary = {}
    pattern_dict = {cp.pattern_id: cp for cp in coat_patterns_list}

    for key, pattern_id in selected_patterns.items():
        if pattern_id is not None:
            matched_dictionary[key] = pattern_dict.get(pattern_id)

    return matched_dictionary
    

