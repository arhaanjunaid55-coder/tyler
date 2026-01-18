# shoppingList = ["milk", "eggs", "bread"]

# print("shopping list:",shoppingList)
# for i in range(len(shoppingList)):
#     print("shopping list at index", i, shoppingList[i])

# shoppingDict = {"dairy": "milk", "protein": "eggs", "grain": "bread"}
# print("shopping dictionary:",shoppingDict)
# for i in shoppingDict:
#      print("shopping dictionary at index", i, shoppingDict[i])

location = 1
cart =[]

world = {
    1: {"up": 2, "down": 16, "right": 14},
    2: {"up": 3, "down": 1, "right": 15, "left": 5},
    3: {"down": 2,"left": 4},
    4: {"down": 6, "right": 3},
    5: { "down":7, "right":2 },
    6: {"up": 4,  "right":7},
    7: {"up":5, "down": 8, "right": 16, "left": 6},
    8: {"up": 7,  "right": 9},
    9: { "down":11 , "right": 10, "left": 8},
    10: {"up":14,  "left": 9},
    11: {"up":9,  "right": 12 },
    12: {"up": 13,  "left": 11},
    13: { "down": 12, "left": 14},
    14: {"up":15, "down":10, "right": 13, "left": 1},
    15: { "down": 14, "left": 2},
    16: {"up": 1,  "left": 7},
}

locationNames = {
    1: "entrance",
    2: "produce",
    3: "dairy",
    4: "hallway",
    5: "grains",
    6: "meat",
    7: "beverages",
    8: "candy",
    9: "hallway",
    10: "restaurant",
    11: "pharmacy",
    12: "bathroom",
    13: "clothing",
    14: "helpdesk",
    15: "checkout",
    16: "exit", 
}


store = {
    "produce": {
        "apples": 3,
        "bananas": 5,
        "carrots": 4,
        "lettuce": 2
    },

    "dairy": {
        "milk": 4,
        "cheese": 6,
        "yogurt": 5,
        "butter": 3
    },

    "grains": {
        "bread": 3,
        "rice": 10,
        "pasta": 4,
        "cereal": 5
    },

    "meat": {
        "chicken": 8,
        "beef": 12,
        "pork": 9,
        "fish": 11
    },

    "beverages": {
        "water": 2,
        "soda": 3,
        "juice": 4,
        "coffee": 6
    },

    "candy": {
        "chocolate": 2,
        "gummies": 1,
        "lollipop": 1,
        "caramel": 2
    },

    "restaurant": {
        "burger": 10,
        "pizza": 12,
        "salad": 8,
        "fries": 4
    },

    "pharmacy": {
        "pain_reliever": 6,
        "vitamins": 10,
        "bandages": 4,
        "cough_syrup": 7
    },

    "clothing": {
        "t_shirt": 15,
        "jeans": 40,
        "jacket": 60,
        "socks": 5
    }
}


def returnLocationName (locationNumber):
    if locationNumber in locationNames:
        return locationNames[locationNumber]
    else:
        return "Not a Location"

def movementNames(location):
    for i in world[location]:
        print(f"Move {i} to {returnLocationName(world[location][i])}")
        
def displayProducts(location):
    location_name = returnLocationName(location)
    if location_name in store:
        print("Products available:")
        for item, price in store[location_name].items():
            print(f"  {item}: ${price}")
    else:
        print("No products available here.")


def movement():
    global location
    
    print(f"You are at location: {returnLocationName(location)}")
    displayProducts(location)
    movementNames(location)
    userInput = input("\n\t\t\t\t\tEnter where you want to move: ").lower()

    if userInput == "quit":
        return

    if userInput in world[location]:
        location = world[location][userInput]
    else:
        print("You are at a Wall")
        
while True:
    movement()
