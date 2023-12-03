import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password',

    )
    print("Successfully connected to MySQL")

    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS task_database')
    cursor.execute("USE task_database")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty  VARCHAR(20)
    )
    """
    cursor.execute(create_table_query)
    conn.commit()


    def calculate_difficulty(cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            return "Easy"
        elif cooking_time < 10 and len(ingredients) >= 4:
            return "Medium"
        elif cooking_time >= 10 and len(ingredients) < 4:
            return "Intermediate"
        else:
            return "Hard"

    def create_recipe(conn, cursor):
        try:
            name = input("Enter the recipe name: ")
            cooking_time = int(input("Enter the cooking time in minutes: "))
            ingredients = input("Enter the ingredients separated by a comma: ").split(", ")
            difficulty = calculate_difficulty(cooking_time, ingredients)

            ingredients_str = ", ".join(ingredients)
            query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, ingredients_str, cooking_time, difficulty))
            conn.commit()
            print("Recipe added successfully.")
        except mysql.connector.Error as err:
            print("Error occurred:", err)
        except Exception as e:
            print("An error occurred:", e)

    def search_recipe(conn, cursor):
        try:
            cursor.execute("SELECT ingredients FROM Recipes")
            results = cursor.fetchall()

            all_ingredients = set()
            for row in results:
                ingredients_list = row[0].split(", ")
                for ingredient in ingredients_list:
                    all_ingredients.add(ingredient.strip())
            
            if not all_ingredients:
                print("No matching ingredients found.")
                return
            
            print("Available ingredients:")
            sorted_ingredients = sorted(all_ingredients)
            for idx, ingredient in enumerate(sorted(all_ingredients), start=1):
                print(f"{idx}. {ingredient}")

            choice = int(input("Select an ingredient number to search for: "))
            if choice < 1 or choice > len(sorted_ingredients):
                print("Invalid ingredient number.")
                return
            
            search_ingredient = list(sorted(all_ingredients))[choice - 1]

            query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
            cursor.execute(query, ('%' + search_ingredient + '%',))

            found_recipes = cursor.fetchall()
            if found_recipes:
                for recipe in found_recipes:
                    print(f"ID: {recipe[0]}, Name: {recipe[1]}, Ingredients: {recipe[2]}, Cooking Time: {recipe[3]}, Difficulty: {recipe[4]}")
            else:
                print(f"No recipes found containing {search_ingredient}.")
        except mysql.connector.Error as err:
            print("Error occurred:", err)
        except Exception as e:
            print("An error occurred:", e)

    def update_recipe(conn, cursor):
        try:
            cursor.execute("SELECT id, name FROM Recipes")
            all_recipes = cursor.fetchall()

            if not all_recipes:
                print("No matching recipe found.")
                return

            print("Available recipes:")
            recipe_ids = [recipe[0] for recipe in all_recipes]
            for recipe in all_recipes:
                print(f"ID: {recipe[0]}, Name: {recipe[1]}")

            recipe_id = int(input("Enter the ID of the recipe to update: "))
            if recipe_id not in recipe_ids:
                print("Invalid recipe ID.")
                return
            
            column = input("Which detail do you want to update? (name, ingredients, cooking_time): ")
            new_value = input(f"Enter the new value for {column}: ")

            if column in ['cooking_time', 'ingredients']:
                cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
                row = cursor.fetchone()
                if row:
                    current_cooking_time, current_ingredients = row
                    if column == 'cooking_time':
                        new_cooking_time = int(new_value)
                        new_ingredients = current_ingredients.split(", ")
                    else:
                        new_cooking_time = current_cooking_time
                        new_ingredients = new_value.split(", ")


                    new_difficulty = calculate_difficulty(new_cooking_time, new_ingredients)

                    update_query = "UPDATE Recipes SET cooking_time = %s, ingredients = %s, difficulty = %s WHERE id = %s"
                    cursor.execute(update_query, (new_cooking_time, ", ".join(new_ingredients), new_difficulty, recipe_id))
                else:
                    print(f"No recipe found with ID {recipe_id}")
                    return
            else:
                update_query = f"UPDATE Recipes SET {column} = %s WHERE id = %s"
                cursor.execute(update_query, (new_value, recipe_id))

            conn.commit()
            print(f"Recipe ID {recipe_id} has been updated.")
        except mysql.connector.Error as err:
            print("Error occurred:", err)
        except ValueError:
            print("Invalid input for cooking time. Please enter an integer.")
        except Exception as e:
            print("An error occurred:", e)

    def delete_recipe(conn, cursor):
        try:
            cursor.execute("SELECT id, name FROM Recipes")
            all_recipes = cursor.fetchall()

            if not all_recipes:
                print("No matching recipe found.")
                return
            
            print("Available recipes:")
            recipe_ids = [recipe[0] for recipe in all_recipes]
            for recipe in all_recipes:
                print(f"ID: {recipe[0]}, Name: {recipe[1]}")

            recipe_id = int(input("Enter the ID of the recipe to delete: "))
            if recipe_id not in recipe_ids:
                print("Invalid recipe ID.")
                return
            
            confirm = input(f"You are about to delete recipe with ID {recipe_id}. Are you sure? Type confirm to continue or cancel to stop: ")
            if confirm.lower() != "confirm":
                print("Recipe was not deleted.")
                return
            
            query = "DELETE FROM Recipes WHERE id = %s"
            cursor.execute(query, (recipe_id,))
            conn.commit()

            print(f"Recipe with ID {recipe_id}  has been deleted.")
        except mysql.connector.Error as err:
            print("Error occured:", err)
        except Exception as e:
            print("An error occurred:", e)


    def main_menu(conn, cursor):
        while True:
            print("1. Add a new recipe")
            print("2. Search for a recipe")
            print("3. Update an existing recipe")
            print("4. Delete a recipe")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                create_recipe(conn, cursor)
            elif choice == '2':
                search_recipe(conn, cursor)
            elif choice == '3':
                update_recipe(conn, cursor)
            elif choice == '4':
                delete_recipe(conn, cursor)
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")


    try:
        main_menu(conn, cursor)
    finally:
        cursor.close()
        conn.close()

except mysql.connector.Error as err:
    print("Error: ", err)