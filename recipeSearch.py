import random
import requests
import pprint


labels = {0: "chinese", 1: "vegan",
          2: "5_ingredients_or_less", 3: "under_30_minutes", 4: "vegetarian"}
for i in range(len(labels)):
    print(str(i+1) + "." + labels[i])

user_selectType = int(
    input("What are you feeling like eating right now?(Input number): "))-1
user_selectType = labels[user_selectType]


url = "https://tasty.p.rapidapi.com/recipes/list"
querystring = {"from": "0", "size": "30", "tags": user_selectType}

headers = {
    'x-rapidapi-key': "b1e1ab1091mshcc9d4bcef44cbf0p1f1095jsn68c0743c6ce6",
    'x-rapidapi-host': "tasty.p.rapidapi.com"
}

response = (requests.get(url, headers=headers, params=querystring)).json()

# print(response.text)
responseResult = response["results"]
random_number = random.randint(0, len(responseResult))

tempAllList = responseResult[random_number]
thenName = (tempAllList["name"]).encode('ascii')

pprint.pprint(thenName)
print("\n")


# entree_ideas = ['Hamburger', "Pizza", "Lamb Roast", "Chicken Noodle Soup",
#                 "Fried Rice", "Stir Fry Bok Choy", "Seafood Soup", "Steamed Eggplant"]
# random_number = random.randint(0, len(entree_ideas))

# print("The chosen dish is: " + entree_ideas[random_number])
