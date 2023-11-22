import pickle

def calc_difficulty(cooking_time, ingredients_count):
    if cooking_time < 10 and ingredients_count < 4:
        return "Easy"
    elif cooking_time < 10 and ingredients_count >= 4:
        return "Medium"
    elif cooking_time >= 10 and ingredients_count < 4:
        return "Intermediate"
    elif cooking_time >= 10 and ingredients_count >= 4:
        return "Hard"
    else:
        return "Unknown"

def take_recipe():
    name = input("Recipe name: ")
    cooking_time = int(input("Cooking time (in minutes): "))
    ingredients = input("Enter ingredients separated by comma: ").split(',')

    difficulty = calc_difficulty(cooking_time, len(ingredients))

    return {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }

def main():
    filename = input("Enter the filename to save recipes: ")

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        data = {'recipes_list': [], 'all_ingredients': []}
    except Exception:
        data = {'recipes_list': [], 'all_ingredients': []}
    else:
        file.close()

    recipes_list, all_ingredients = data['recipes_list'], data['all_ingredients']

    n = int(input("How many recipes would you like to enter? "))
    for _ in range(n):
        recipe = take_recipe()
        recipes_list.append(recipe)
        for ingredient in recipe['ingredients']:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

    with open(filename, 'wb') as file:
        pickle.dump(data, file)

if __name__ == '__main__':
    main()