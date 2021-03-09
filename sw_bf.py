n = 4
k = int(input())

arr = [80, -50, 90, 100]

def slidingWindow_bf(arr, n, k):
    res = 0
    if k > len(arr):
        res = sum(arr)
        return res
    for i in range(len(arr)-(k-1)):
        temp = 0
        for j in range(k):
            temp += arr[i+j]
        if temp > res:
            res = temp
    return res

print(slidingWindow_bf(arr, n, k))