# shoppingList = ["milk", "eggs", "bread"]

# print("shopping list:",shoppingList)
# for i in range(len(shoppingList)):
#     print("shopping list at index", i, shoppingList[i])

# shoppingDict = {"dairy": "milk", "protein": "eggs", "grain": "bread"}
# print("shopping dictionary:",shoppingDict)
# for i in shoppingDict:
#      print("shopping dictionary at index", i, shoppingDict[i])
import random

location = 1
cart = []
totalSum = 0
playerMoney = random.randint(10, 100)

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
    12: "hallway",
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
    print("\n" + "-" * 60)
    print("  AVAILABLE EXITS:")
    print("-" * 60)
    for i in world[location]:
        print(f"    ➜  Move {i.upper():<8} to {returnLocationName(world[location][i]).upper()}")
    print("-" * 60)
        
def displayProducts(location):
    location_name = returnLocationName(location)
    if location_name in store:
        print("\n" + "=" * 60)
        print(f"  🛒 PRODUCTS AVAILABLE AT {location_name.upper()}:")
        print("=" * 60)
        for item, price in store[location_name].items():
            print(f"    • {item.replace('_', ' ').title():<25} ${price:>5}")
        print("=" * 60)
    else:
        print("\n    ℹ️  No products available here.\n")

def displayCart():
    global totalSum
    
    totalPrice = 0
    
    print("\n" + "=" * 60)
    print("  🛍️  YOUR SHOPPING CART:")
    print("=" * 60)
    
    if not cart:
        print("    (Cart is empty)")
    else:
        for i in cart:
            for j in store:
                for k in store[j]:
                    if k == i:     
                        print(f"    • {i.replace('_', ' ').title():<25} ${store[j][k]:>5}")
                        totalPrice = totalPrice + store[j][k]
        print("-" * 60)
        print(f"    TOTAL PRICE: ${totalPrice:>5}")
    
    print("=" * 60)
    
    totalSum = totalPrice

def buyProducts(location):
    product_locations_list = [2, 3, 5, 6, 7, 8, 10, 11, 13]
    
    if location in product_locations_list:
        displayProducts(location)
        userInput = input("\n  ➤ Enter item to add to cart (or 'x' to stop): ").lower()
    
        while userInput != 'x':
            if userInput != 'x':
                cart.append(userInput)
                print(f"\n    ✓ Added '{userInput}' to cart!")
                displayCart()
            userInput = input("\n  ➤ Enter item to add to cart (or 'x' to stop): ").lower()
        
        print(f"\n    👋 Thank you for visiting {returnLocationName(location).upper()}!\n")
    
def checkoutCart(location):
    global playerMoney, totalSum
    if location == 15:
        displayCart()
        
        userInput = input("Press a to buy cart\nPress x to review cart")
        
        if userInput == 'a':
            playerMoney = playerMoney - totalSum
            
        print(f"You have ${playerMoney} left")
    

def movement():
    global location
    
    print("\n" + "=" * 60)
    print(f"  📍 CURRENT LOCATION: {returnLocationName(location).upper()}")
    print("=" * 60)
    
    buyProducts(location)
    movementNames(location)
    checkoutCart(location)
    
    userInput = input("\n  ➤ Enter direction to move: ").lower()

    if userInput in world[location]:
        location = world[location][userInput]
    else:
        print("\n    ⚠️  You are at a wall! Please choose a valid direction.\n")
        
while True:
    movement()