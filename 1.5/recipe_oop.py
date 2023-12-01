class Recipe(object):
    all_ingredients = set()

    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    def add_ingredients(self, *args):
        for ingredient in args:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10:
            self.difficulty = "Medium"
        elif len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)

    def __str__(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return f"Recipe for {self.name}: Ingredients: {', '.join(self.ingredients)}, Cooking Time: {self.cooking_time} minutes, Difficulty: {self.difficulty}"

    def recipe_search(data, search_term):
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)


# Recipes
tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")

recipes_list = [tea, coffee, cake, banana_smoothie]

for recipe in recipes_list:
    print(recipe)

print("\nRecipes containing Water:")
Recipe.recipe_search(recipes_list, "Water")

print("\nRecipes containing Sugar:")
Recipe.recipe_search(recipes_list, "Sugar")

print("\nRecipes containing Bananas:")
Recipe.recipe_search(recipes_list, "Bananas")
    