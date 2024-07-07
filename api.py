import requests

API_KEY = "783517db663041da86fca540f6c28a7d"

def search_recipes(name, minCalories=-1, maxCalories=-1):
    url = "https://api.spoonacular.com/recipes/complexSearch"

    query_string = {}
    query_string['apiKey'] = API_KEY
    query_string['name'] = name
    if minCalories != -1 and minCalories >= 50:
        query_string['minCalories'] = minCalories
    if maxCalories != -1 and maxCalories <= 800:
        query_string['maxCalories'] = maxCalories

    response = requests.get(url, params=query_string)

    return response.json()

def detail_recipe(id):
    url = f"https://api.spoonacular.com/recipes/{id}/information"
    print(url)

    query_string = {}
    query_string['apiKey'] = API_KEY

    response = requests.get(url, params=query_string)

    return response.json()