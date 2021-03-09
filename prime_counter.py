import math

def prime(num):
    if num<2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        flag = 0
        for i in range(3, math.ceil(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = 1
                break
        if flag:
            return False
        return True

def prime_count(n):
    count = 0
    for i in range(2, n+1):
        if prime(i):
            count += 1
    return count

prime_dict = {}
count_pc = 0
low, high = list(map(int, input().split(" ")))
# making the prime list
for i in range(low, high + 1):
    prime_dict[i] = prime_count(i)
    if prime(prime_dict[i]):
        count_pc +=1
print(prime_dict)

print(count_pc)

