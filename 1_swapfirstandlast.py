input_arr = input()
output_arr = ""
for i in input_arr:
    if i == "[":
        pass
    elif i == "]":
        pass
    else:
        output_arr += i

output_arr = list(map(int, output_arr.split(",")))
output_arr[0], output_arr[-1] = output_arr[-1], output_arr[0]
print(output_arr)

