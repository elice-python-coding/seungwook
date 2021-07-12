n,m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    num = min(arr)
    result = max(num, result)

print(result)