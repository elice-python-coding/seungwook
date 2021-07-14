my_str = list(input())

cnt = 0
for i in range(1, len(my_str)):
    if my_str[i] != my_str[i-1]:
       cnt += 1
    else:
        pass
    
print(ceil(int(cnt/2)))
