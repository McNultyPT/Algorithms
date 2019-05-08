#!/usr/bin/python
pizza = {
  'dough': 1,
  'cheese': 12,
  'sauce': 5
}

ingredients = {
  'dough': 1,
  'cheese': 7,
  'sauce': 5
}

import math

def recipe_batches(recipe, ingredients):
    batches = []
    recipe_values = [i for i in recipe.values()]
    ingredient_values = [j for j in ingredients.values()]

    for i in range(len(recipe_values)):
        for j in range(len(ingredient_values)):
            if i == j:
                if ingredient_values[j] > recipe_values[i]:
                    print(ingredient_values)
                    print(recipe_values)
                    num = recipe_values[i] % ingredient_values[j]
                    print(num)
                    batch = int(ingredient_values[j] // num)
                    print(batch)
                    batches.append(batch)
                elif ingredient_values[j] == recipe_values[i]:
                    batches.append(1)
                else:
                    batches.append(0)
    if len(recipe_values) > len(batches):
        return 0
    else:
        return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))