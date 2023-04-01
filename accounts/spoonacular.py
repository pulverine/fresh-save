import requests

# def search_recipes_by_ingredient(ingredient):
#     url = 'https://api.spoonacular.com/recipes/findByIngredients'
#     params = {
#         'apiKey': '8eca12a5acfe4b7d91fe5a6cb93fd52f',
#         'ingredients': ingredient,
#         'number': 5  # Change this to however many recipes you want to display
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     recipes = []
#     for recipe in data:
#         recipe_info = {
#             'id': recipe['id'],
#             'title': recipe['title'],
#             'image': recipe['image'],
#             'missed_ingredients': recipe['missedIngredients'],
#             'used_ingredients': recipe['usedIngredients'],
#             'unused_ingredients': recipe['unusedIngredients']
#         }
#         recipes.append(recipe_info)
#     return recipes

def search_recipes(ingredient):
    url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey=<8eca12a5acfe4b7d91fe5a6cb93fd52f>&query={ingredient}'
    response = requests.get(url)
    response_data = response.json()
    # if 'results' not in response_data:
    #     return []
    recipes = response_data
    return recipes
def get_recipe_information(recipe_id):
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey=<8eca12a5acfe4b7d91fe5a6cb93fd52f>'
    response = requests.get(url)
    recipe = response.json()
    return recipe
