char = input()[0]
if char.isupper():
    print("Upper")
elif char.islower():
    print("Lower")
elif char.isdigit():
    print("Number")
else:
    print("Symbol")