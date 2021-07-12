n, k = map(int, input().split())
count = 0

def divide():
    global n, k
    if n % k == 0:
        n /= k
    else:
        n -= 1

def minus():
    global n
    n -= 1

while n != 1:
    if n > k:
        divide()
    else:
        minus()
    count += 1

print(count)