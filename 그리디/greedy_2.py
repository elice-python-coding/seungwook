import random

n, m, k = input().split()
n, m, k = int(n), int(m), int(k)
if n < 2 or n > 1000 or m < 1 or m > 10000 or k < 1 or k > 10000:
    print("잘못된 수를 입력하였습니다")

data = list(map(int, input().split()))
data.sort()
data.reverse()

first = data[0]
second = data[1]

second_num = m / (k+1)
first_num = m - second_num
result = (first*first_num)+(second*second_num)

print(int(result))