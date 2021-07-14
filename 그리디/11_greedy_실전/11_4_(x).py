import itertools

n = int(input())
m = list(map(str, input().split()))

combine_m = "".join(m)
arr1 = []
i = len(m)
while i > 0:
    arr1.append(m[i-1])
    i -= 1

iter = itertools.product(combine_m, repeat=2)
for data in iter:
    arr2 = []
    x , y = data
    arr2.append(int(x)+int(y))
    
for i in range(100000000):
    if (i in arr1) or (i in arr2):
        pass
    else:
        print(i)
        break 
