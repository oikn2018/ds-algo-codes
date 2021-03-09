n = 4
k = int(input())

arr = [80, -50, 90, 100]

def slidingWindow_optimized(arr, n, k):
    if k < n:
        slidingWindowSum = sum([arr[i] for i in range(k)])
        maxSum = slidingWindowSum
    if k >= n:
        return sum(arr)
    temp = slidingWindowSum
    for i in range(n - k):
        temp = temp + arr[i+k] - arr[i]
        # print(temp)
        if temp > maxSum:
            maxSum = temp
    return maxSum

print(slidingWindow_optimized(arr, n, k))