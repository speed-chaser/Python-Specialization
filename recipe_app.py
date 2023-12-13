from sqlalchemy import Column, create_engine
from sqlalchemy.types import String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('mysql://cf-python:password@localhost/my_database')

Session = sessionmaker(bind=engine)

session = Session()

class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    def __str__(self):
        return f"Recipe ID: {self.id}\nName: {self.name}\nIngredients: {self.ingredients}\nCooking Time: \
            {self.cooking_time} minutes\nDifficulty: {self.difficulty}"
    def calculate_difficulty(self):
        if self.cooking_time <= 15 and len(self.ingredients.split(', ')) <= 3:
            self.difficulty = "Easy"
        if self.cooking_time <= 30 and len(self.ingredients.split(', ')) <= 5:
            self.difficulty = "Medium"
        if self.cooking_time <= 45 and len(self.ingredients.split(', ')) <= 7:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"
    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        else:
            ingredients_list = self.ingredients.split(',')
            return ingredients_list

Base.metadata.create_all(engine)    

def create_recipe():
    print("Create a new recipe")
    
    while True:
        name = input("Enter the recipe name: ")
        if len(name) > 50 or not name.isalnum():
            print("Recipe name must be alphanumeric and less than 50 characters.")
        else:
            break
    
    while True:
        try:
            num_ingredients = int(input("Enter the number of ingredients: "))
            if num_ingredients > 0:
                break
            else:
                print("Please enter a valid number of ingredients.")
        except ValueError:
            print("Please enter a valid number.")
    
    ingredients_list = []
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients_list.append(ingredient)
    
    ingredients = ", ".join(ingredients_list)
    
    while True:
        cooking_time_str = input("Enter the cooking time (in minutes): ")
        if cooking_time_str.isnumeric():
            cooking_time = int(cooking_time_str)
            break
        else:
            print("Cooking time must be a valid number.")
    
    new_recipe = Recipe(name=name, ingredients=ingredients, cooking_time=cooking_time)
    
    new_recipe.calculate_difficulty()

    session.add(new_recipe)
    session.commit()
    
    print("Recipe created successfully!")

def view_all_recipes():
    print("View all recipes")
    
    all_recipes = session.query(Recipe).all()
    
    if not all_recipes:
        print("There are no recipes in the database.")
        return  
    
    for recipe in all_recipes:
        print(recipe)  

def search_by_ingredients():
    print("Search for recipes by ingredients")
    
    num_entries = session.query(Recipe).count()
    if num_entries == 0:
        print("There are no recipes in the database.")
        return  
    
    results = session.query(Recipe.ingredients).all()
    
    all_ingredients = set()
    
    for result in results:
        ingredients_list = result[0].split(', ')
        for ingredient in ingredients_list:
            all_ingredients.add(ingredient)
    
    print("Ingredients to search by:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")
    
    user_input = input("Enter ingredient numbers separated by spaces: ")
    
    selected_numbers = user_input.split()
    
    for num in selected_numbers:
        if not num.isdigit() or int(num) < 1 or int(num) > len(all_ingredients):
            print("Invalid input. Please select valid ingredient numbers.")
            return  
    
    search_ingredients = [list(all_ingredients)[int(num) - 1] for num in selected_numbers]
    
    conditions = []
    
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))
    
    matching_recipes = session.query(Recipe).filter(*conditions).all()
    
    if not matching_recipes:
        print("No recipes found matching the selected ingredients.")
    else:
        print("Matching recipes:")
        for recipe in matching_recipes:
            print(recipe)  


def edit_recipe():
    print("Edit a recipe")
    
    num_entries = session.query(Recipe).count()
    if num_entries == 0:
        print("There are no recipes in the database.")
        return  
    
    results = session.query(Recipe.id, Recipe.name).all()
    
    print("Available recipes to edit:")
    for i, (recipe_id, recipe_name) in enumerate(results, start=1):
        print(f"{i}. Recipe ID: {recipe_id}, Name: {recipe_name}")
    
    try:
        selected_index = int(input("Enter the number of the recipe you want to edit: ")) - 1
        if selected_index < 0 or selected_index >= len(results):
            print("Invalid input. Please select a valid recipe number.")
            return  
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return  
    
    selected_recipe_id, selected_recipe_name = results[selected_index]
    recipe_to_edit = session.query(Recipe).filter_by(id=selected_recipe_id).first()
    
    print(f"Editing Recipe ID: {selected_recipe_id}, Name: {selected_recipe_name}")
    print("Select an attribute to edit:")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")
    
    try:
        selected_attribute = int(input("Enter the number of the attribute you want to edit: "))
        if selected_attribute not in [1, 2, 3]:
            print("Invalid input. Please select a valid attribute number.")
            return 
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return  
    
    if selected_attribute == 1:
        new_name = input("Enter the new name: ")
        recipe_to_edit.name = new_name
    elif selected_attribute == 2:
        new_ingredients = input("Enter the new ingredients (comma-separated): ")
        recipe_to_edit.ingredients = new_ingredients
    elif selected_attribute == 3:
        try:
            new_cooking_time = int(input("Enter the new cooking time (in minutes): "))
            recipe_to_edit.cooking_time = new_cooking_time
        except ValueError:
            print("Invalid input. Please enter a valid number for cooking time.")
            return  

    recipe_to_edit.calculate_difficulty()
    

    session.commit()
    print("Recipe successfully updated.")

def delete_recipe():
    print("Delete a recipe")

    num_entries = session.query(Recipe).count()
    if num_entries == 0:
        print("There are no recipes in the database.")
        return

    results = session.query(Recipe.id, Recipe.name).all()

    print("Available recipes to delete:")
    for i, (recipe_id, recipe_name) in enumerate(results, start=1):
        print(f"{i}. Recipe ID: {recipe_id}, Name: {recipe_name}")

    try:
        selected_index = int(input("Enter the number of the recipe you would like to delete: "))
        if selected_index < 0 or selected_index > len(results):
            print("Invalid input. Please select a valid recipe number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    selected_recipe_id, selected_recipe_name = results[selected_index - 1]
    recipe_to_delete = session.query(Recipe).filter_by(id=selected_recipe_id).first()

    print(f"Deleting Recipe ID: {selected_recipe_id}, Name: {selected_recipe_name}")
    confirmation = input("Are you sure you want to delete this recipe? (yes/no): ").strip().lower()

    if confirmation == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe successfully deleted.")
    else:
        print("Deletion canceled.  Recipe not deleted.")


while True:
    print("\nMain Menu")
    print("1. Create a new recipe")
    print("2. View all recipes")
    print("3. Search for recipes by ingredients")
    print("4. Edit a recipe")
    print("5. Delete a recipe")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        create_recipe()
    elif choice == "2":
        view_all_recipes()
    elif choice == "3":
        search_by_ingredients()
    elif choice == "4":
        edit_recipe()
    elif choice == "5":
        delete_recipe()
    elif choice =="6":
        print("Goodbye!")
        session.close()
        engine.dispose()
        break
    else:
        print("Invalid choice. Please enter a nubmer between 1 and 6.")