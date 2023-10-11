'''
Write the dictionaty structure for storing recipes for food.
Hardcode your own data.
Get user input for the name of the recipe, and then print the recipe.
'''

# Dictionary structure for storing recipes
recipes = {
    "Chicken biryani": {
        "ingredients": ["Chicken", "Basmati Rice", "Onion", "Tomato", "Spices", "Yogurt"],
        "instructions": "1. Marinate chicken with yogurt and spices. 2. Cook rice separately. 3. Layer rice and chicken in a pot. 4. Cook until done."
    },
    "Tea": {
        "ingredients": ["Tea Leaves", "Water", "Milk", "Sugar"],
        "instructions": "1. Boil water and add tea leaves. 2. Add milk and sugar. 3. Strain and serve."
    },
    "Coffee": {
        "ingredients": ["Ground Coffee", "Water", "Milk", "Sugar"],
        "instructions": "1. Brew coffee with hot water. 2. Add milk and sugar to taste. 3. Stir and enjoy."
    },
    "Egg curry": {
        "ingredients": ["Eggs", "Onion", "Tomato", "Spices", "Oil"],
        "instructions": "1. Boil eggs. 2. Make a curry base with onion, tomato, and spices. 3. Add boiled eggs and simmer."
    },
    "Butter chicken": {
        "ingredients": ["Chicken", "Tomato Sauce", "Cream", "Butter", "Spices"],
        "instructions": "1. Cook chicken and set aside. 2. Make a sauce with tomato, cream, and spices. 3. Add cooked chicken and simmer."
    }
}

# Get user input for the name of the recipe
recipe_name = input("Enter the name of the recipe: ")

# Check if the recipe exists in the dictionary
if recipe_name in recipes:
    print(f"Here is the recipe for {recipe_name}:")
    ingredients = ", ".join(recipes[recipe_name]["ingredients"])
    instructions = recipes[recipe_name]["instructions"]
    print(f"You need ingredients: {ingredients}.")
    print(f"Instructions: {instructions}")
else:
    print(f"Recipe for {recipe_name} not found.")
