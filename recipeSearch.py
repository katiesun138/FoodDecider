import random
import requests
import pprint


labels = {0: "Breakfast", 1: "Lunch",
          2: "Appetizers", 3: "Dinner", 4: "Desserts"}
for i in range(len(labels)):
    print(str(i+1) + "." + labels[i])


url = "https://tasty.p.rapidapi.com/recipes/list"
querystring = {"from": "0", "size": "", "tags": "under_30_minutes"}

headers = {
    'x-rapidapi-key': "b1e1ab1091mshcc9d4bcef44cbf0p1f1095jsn68c0743c6ce6",
    'x-rapidapi-host': "tasty.p.rapidapi.com"
}

response = (requests.get(url, headers=headers, params=querystring)).json()

# print(response.text)
responseResult = response["results"]
thenName = responseResult[0]["name"]

pprint.pprint(thenName)


# entree_ideas = ['Hamburger', "Pizza", "Lamb Roast", "Chicken Noodle Soup",
#                 "Fried Rice", "Stir Fry Bok Choy", "Seafood Soup", "Steamed Eggplant"]
# random_number = random.randint(0, len(entree_ideas))

# print("The chosen dish is: " + entree_ideas[random_number])
