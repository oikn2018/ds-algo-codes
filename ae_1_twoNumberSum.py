# Naive solution TC: O(N^2)
def twoNumberSum(iarr, targetSum):
    flag = 0
    for i in range(len(iarr)):
        for j in range(i+1, len(iarr)):
            if iarr[i] + iarr[j] == targetSum:
                flag = 1
                return sorted([iarr[i], iarr[j]])

    if flag == 0:
        return []

# Better solution (w/o hash table) TC: O(NlogN) SC: O(1)
def twoNumberSum2(iarr, targetSum):
    iarr.sort()
    L = 0
    R = len(arr) - 1
    while (L < R):
        if iarr[L] + iarr[R] < targetSum:
            L += 1
        elif iarr[L] + iarr[R] > targetSum:
            R -= 1
        else:
            return [iarr[L], iarr[R]]
    return []

# Best solution (w hash table) TC: O(N) SC: O(N)
def twoNumberSum3(iarr, targetSum):
    hashT = {}
    flag = 0
    for num in iarr:
        diff = targetSum - num
        if diff not in hashT:
            hashT[num] = True
        else:
            flag = 1
            return sorted([num, diff])
    if flag == 0:
        return []

# Main Code
arr = [3, 5, -4, 8, 11, 1, -1, 6]
ts = 10
print(twoNumberSum3(arr, ts))