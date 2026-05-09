recipes = {
    "Pasta": (["pasta","tomato sauce"],"Boil pasta, add sauce",17),
    "Omelate": (["eggs","cheese","veggies"],"Beat eggs, cook with fillings", 10)
}

def show_recipe(name):
    ingredients, steps, time = recipes[name]
    print(f"\n{name} ({time} mins)")  
    print("Ingredients:",','.join(ingredients))
    print("Steps: ",steps)

# add new recipe
recipes["Smoothie"] = (["banana","milk","barries"],"Blend all ingredients", 5)

# display all recipes
for i, recipe in enumerate(recipes.keys(),1):
    print(f"{i}. {recipe}")
show_recipe("Smoothie")