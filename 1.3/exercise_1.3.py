recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("What would you like to name your next recipe? ")
    cooking_time = int(input("How long does this recipe take to cook? (In minutes) "))
    ingredients = []
    print("Enter ingredients one by one. Type 'done' when finished: ")
    while True:
        ingredient = input("Enter an ingredient: ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    if(cooking_time < 10 and len(ingredients) < 4):
        difficulty = "Easy"
    elif(cooking_time < 10 and len(ingredients) >= 4):
        difficulty = "Medium"
    elif(cooking_time >= 10 and len(ingredients) < 4):
        difficulty = "Intermediate"
    elif(cooking_time >= 10 and len(ingredients) >= 4):
        difficulty = "Hard"
    else:
        difficulty = "Unknown"

    return {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}


def main():
    n = int(input("How many recipes would you like to enter? "))
    for _ in range(n):
        recipe = take_recipe()
        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
        recipes_list.append(recipe)

    for recipe in recipes_list:
        print(f"Recipe: {recipe['name']}")
        print(f"Cooking Time (min): {recipe['cooking_time']}")
        print(f"Difficulty: {recipe['difficulty']}")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f" - {ingredient}")
        print()  # empty line for better separation between recipes
              
    ingredients_list.sort()
    print("\nIngredients available across all recipes:")
    for ingredient in ingredients_list:
        print(ingredient)

if __name__ == "__main__":
    main()