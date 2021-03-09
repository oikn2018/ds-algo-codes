import math
def check(num):
    return num>0

def prime(num):
    if num<2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        flag = 0
        for i in range(3, int(math.sqrt(num))):
            if num % i == 0:
                flag = 1
                break
        if flag:
            return False
        return True

n = int(input())
while not check(n):
    print("Please enter positive number:")
    n = int(input())

if prime(n):
    print("Positive number is prime")
else:
    print("Positive number is not prime")