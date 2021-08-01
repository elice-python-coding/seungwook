my_list = list(input())

while len(my_list) > 1:
    mul = int(my_list[0]) * int(my_list[1])
    sum = int(my_list[0]) + int(my_list[1])
    if mul >= sum:
        del my_list[0:2]
        my_list.insert(0, mul)
    else:
        del my_list[0:2]
        my_list.insert(0, sum)

print(my_list[0])