#CCD

category = input().upper()
flavor = input()
type = ""

if category == "C":
    if flavor == "1":
        type = "Expresso Coffee"
    elif flavor == "2":
        type = "Cappuccino Coffee"
    elif flavor == "3":
        type = "Latte Coffee"
    else:
        type = "#"
elif category == "T":
    if flavor == "1":
        type = "Plain Tea"
    elif flavor == "2":
        type = "Assam Tea"
    elif flavor == "3":
        type = "Ginger Tea"
    else:
        type = "#"
elif category == "S":
    if flavor == "1":
        type = "Hot and Sour Soup"
    elif flavor == "2":
        type = "Veg Corn Soup"
    elif flavor == "3":
        type = "Tomato Soup"
    else:
        type = "#"
elif category == "B":
    if flavor == "1":
        type = "Hot Chocolate Drink"
    elif flavor == "2":
        type = "Badam Drink"
    elif flavor == "3":
        type = "Badam Pista Drink"
    else:
        type = "#"
if type == "#":
    print("Invalid OUTPUT!")
else:
    print("Welcome to CCD")
    print("Enjoy your " + type + "!")