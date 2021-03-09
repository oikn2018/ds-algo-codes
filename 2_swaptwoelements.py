input_arr = list(map(int, input().split(",")))
pos1, pos2 = list(map(int, input().split(",")))

input_arr[pos1-1], input_arr[pos2-1] = input_arr[pos2-1], input_arr[pos1-1]

print(input_arr)
