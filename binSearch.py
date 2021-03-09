def binSearch(arr, key):
    start = 0
    end = len(arr) - 1

    while (start <= end): # greater than or equal to 1 element
        mid = (start + end)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
        
    return -1

arr = [1,2,3,4,5,6]
key = int(input())
print(binSearch(arr, key))