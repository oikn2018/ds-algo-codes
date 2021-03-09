array = list(map(int, input().split(",")))
if len(array) < 4:
    print("invalid size")
array.sort()
sum = array[-3] + array[-2] + array[-1]
print(sum)
