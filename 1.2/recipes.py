recipe_1 = {
'name': 'Tea',
'cooking_time': 5,
'ingredients': ['Tea leaves', 'Sugar', 'Water']
}

all_recipes = [recipe_1]

recipe_2 = {'name': 'Coffee', 'cooking_time': 10, 'ingredients': ['Coffee beans', 'Sugar', 'Water', 'Creamer']}
recipe_3 = {'name': 'Pasta', 'cooking_time': 30, 'ingredients': ['Pasta', 'Tomato Sauce', 'Cheese']}
recipe_4 = {'name': 'Salad', 'cooking_time': 15, 'ingredients': ['Lettuce', 'Tomato', 'Cucumber', 'Olive oil']}
recipe_5 = {'name': 'Sandwich', 'cooking_time': 10, 'ingredients': ['Bread', 'Cheese', 'Ham', 'Lettuce']}

all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])

for recipe in all_recipes:
    print(f"Ingredients for {recipe['name']}: {recipe['ingredients']}")