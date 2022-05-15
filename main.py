import csv
import json
import random


while True:
    with open('recipe.txt') as f:
        user_input = f.read()

    with open('recipes10.csv', mode='r') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        recipes = []

        for row in csv_reader:
            if user_input and user_input in row["ingredients_raw_str"]:
                recipes.append(row)

    data = {}

    if user_input:
        if len(recipes) < 1:
            data['error'] = "No recipes found. Try a different ingredient"
        else:
            data['recipes'] = random.choices(recipes, k=3)

        final = json.dumps(data, indent=2)

        with open('recipes.json', 'w') as outfile:
            outfile.write(final)
