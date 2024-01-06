import random


class CoatPattern:
    def __init__(self, pattern_id, pattern_name, rarity):
        self.pattern_id = pattern_id
        self.pattern_name = pattern_name
        self.rarity = rarity







# Define mock family tree with coat patterns
family_tree = {
    'grandparent1': CoatPattern('spotted_red', 'Spotted Red', 'Common'),
    'grandparent2': CoatPattern('striped_blue', 'Striped Blue', 'Uncommon'),
    'grandparent3': CoatPattern('solid_gold', 'Solid Gold', 'Rare'),
    'grandparent4': CoatPattern('albino', 'Albino', 'Legendary'),
    'parent1': CoatPattern('striped_blue', 'Striped Blue', 'Uncommon'),
    'parent2': CoatPattern('spotted_red', 'Spotted Red', 'Common'),
    'child': None,
}

def select_coat_pattern(family_tree):
    weights = {
    'Common': {
        'parents':         45.0,
        'grandparents':    25.0,
        'g-grandparents':  15.0,
    }, 
    'Uncommon': { 
        'parents':         25.0,
        'grandparents':    15.0,
        'g-grandparents':   5.0,
    }, 
    'Rare': { 
        'parents':         10.0,
        'grandparents':     5.0,
        'g-grandparents':   2.5,
    }, 
    'Legendary': { 
        'parents':          5.0,
        'grandparents':     2.5,
        'g-grandparents':   1.0,
    }
}
    

    def calculate_individual_chances(family_tree, weights):
            family_tree_percentage = {}
            total_chance = 0.0

            # Calculate individual chances
            for relation, coat_pattern in family_tree.items():
                if coat_pattern is None:  # Skip the "None" child value
                    continue
                rarity = coat_pattern.rarity
                if relation.startswith('parent'):
                    chance = weights[rarity]['parents']
                elif relation.startswith('grandparent'):
                    chance = weights[rarity]['grandparents']
                elif relation.startswith('g-grandparent'):
                    chance = weights[rarity]['g-grandparents']
                else:
                    continue

                # Add the chance to the total
                total_chance += chance
                # Store the individual chance
                family_tree_percentage[relation] = chance

            # Normalize individual chances to sum up to 100%
            for relation in family_tree_percentage:
                normalized_chance = (family_tree_percentage[relation] / total_chance) * 100
                family_tree_percentage[relation] = round(normalized_chance, 2)

            return family_tree_percentage

    pattern_chances = {}
    total_chance = 0.0

    # Calculate chances
    #########################################################################################
    #            Reusing code from above  "calculate_individual_chances"  function          #
    #########################################################################################
    for relation, coat_pattern in family_tree.items():
        if coat_pattern is None:  # Skip the "None" child value
            continue
        rarity = coat_pattern.rarity
        pattern = f'({coat_pattern.rarity}) {coat_pattern.pattern_name}'
        if relation.startswith('parent'):
            chance = weights[rarity]['parents']
        elif relation.startswith('grandparent'):
            chance = weights[rarity]['grandparents']
        elif relation.startswith('g-grandparent'):
            chance = weights[rarity]['g-grandparents']
        else:
            continue
    ##############################   End Reusing   ##########################################

        pattern_chances[pattern] = pattern_chances.get(pattern, 0) + chance
        total_chance += chance

    # Move to the bottom?
    family_tree_percentage = calculate_individual_chances(family_tree, weights)

    # Normalize chances to sum up to 100% and round to 2 decimal places
    for pattern in pattern_chances:
        normalized_chance = (pattern_chances[pattern] / total_chance) * 100
        pattern_chances[pattern] = round(normalized_chance, 2)

    # Select coat pattern
    cumulative_distribution = []
    current = 0
    for pattern, chance in pattern_chances.items():
        current += chance
        cumulative_chance = round(current, 2)
        cumulative_distribution.append((cumulative_chance, pattern))

    random_number = round(random.uniform(0, 100), 2)

    for value, pattern in cumulative_distribution:
        if random_number <= value:
            selected_coat = next(coat for coat in family_tree.values() if f'({coat.rarity}) {coat.pattern_name}' == pattern)
            break

    return selected_coat, family_tree_percentage, pattern_chances



selected_coat, family_tree_percentage, pattern_chances = select_coat_pattern(family_tree)
print()
print()
print()
print()
print()
print()
print(f"Selected coat pattern is '{selected_coat.pattern_name}' with a chance of {pattern_chances[f'({selected_coat.rarity}) {selected_coat.pattern_name}']}%.")
print(f"Normalized chances of passing on the skin: {pattern_chances}")
print(f"Individual chances of passing on the skin: {family_tree_percentage}")
