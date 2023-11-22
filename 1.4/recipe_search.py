import pickle

def display_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")
    print()

def search_ingredient(data):
    all_ingredients = data['all_ingredients']

    print("Available Ingredients:")
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}. {ingredient}")

    try:
        choice = int(input("Enter the number of the ingredient to search: "))
        ingredient_searched = all_ingredients[choice]
    except (IndexError, ValueError):
        print("Invalid input. Please enter a correct nmber.")
        return
    else:
        print(f"\nRecipes containing {ingredient_searched}:")
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)

def main():
    filename = input("Enter the filename containing your recipe data: ")

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print("File not found. Please ensure the filename is correct.")
        return
    else:
        search_ingredient(data)

if __name__ == '__main__':
    main()