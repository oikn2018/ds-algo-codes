import math
n = int(input())
n0 = 1
rodd = 2
n1 = 1
reven = 3

if n % 2 == 0:
    # even series
    val = n0*(reven**(math.ceil(n/2)-1))
else:
    # odd series
    val = n1 * (rodd**(math.ceil(n/2)-1))

print(val)