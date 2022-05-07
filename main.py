import csv
import json
import time

while True:
    with open('recipe.txt') as f:
        user_input = f.read()

    with open('recipes10.csv', mode='r') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        recipes = []

        for row in csv_reader:
            if line_count < 3:
                if user_input and user_input in row["ingredients_raw_str"]:
                    recipes.append(row)
                    line_count += 1

    data = {}

    time.sleep(3)

    if user_input:
        if len(recipes) < 1:
            data['error'] = "No recipes found. Try different ingredient"
        else:
            data['recipes'] = recipes
    # else:
    #     data['error'] = "Please enter an ingredient"

        final = json.dumps(data, indent=2)

        with open('recipes.json', 'w') as outfile:
            outfile.write(final)
