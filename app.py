# app.py
from flask import Flask, render_template, request
from calculations import CoatPattern, select_coat_pattern
from coat_patterns import coat_patterns, match_patterns

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    selected_patterns = {
        'grandparent1': None,
        'grandparent2': None,
        'grandparent3': None,
        'grandparent4': None,
        'parent1': None,
        'parent2': None,
        'child': None
    }
    if request.method == 'POST':
        
        for i in range(1, 5):
            pattern = request.form.get(f'grandparent{i}')
            selected_patterns[f'grandparent{i}'] = pattern
        for i in range(1, 3):
            pattern = request.form.get(f'parent{i}')
            selected_patterns[f'parent{i}'] = pattern        



        print(selected_patterns)
        matched_patterns = match_patterns(selected_patterns, coat_patterns)
        print(matched_patterns)
        coat_pattern_result, family_tree_percentage, pattern_chances= select_coat_pattern(matched_patterns)
        print(f'coat = {coat_pattern_result}')
        print(family_tree_percentage)
        print(pattern_chances)
        
        selected_patterns['child'] = coat_pattern_result

    return render_template(
        'calculator.html',
        coat_patterns=coat_patterns,
        result=result,
        selected_patterns=selected_patterns,
        family_tree_percentage=family_tree_percentage,
        pattern_chances=pattern_chances)



if __name__ == '__main__':
    app.run(debug=True)


