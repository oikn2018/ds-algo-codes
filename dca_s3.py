from queue import PriorityQueue

#kth min
q = PriorityQueue()


ip = list(map(int, input().split()))
size = ip.pop(0)
k = ip.pop()
arr = ip

for num in arr:
    q.put(num)

val = 0

for i in range(k):
    val = q.get()

print(val)