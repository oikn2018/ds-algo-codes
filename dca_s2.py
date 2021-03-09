import math

num = int(input())

if num<0:
    print("Wrong input")
else:
    d = math.floor(math.log10(num)) + 1

    if int(str(num**2)[-d:]) == num:
        print("Correct number")
    else:
        print("Incorrect number")