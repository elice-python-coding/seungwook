N = int(input())
M = input().split()

arr = [1, 1]
i = 0
while i < len(M):
    if M[i] == 'R' and arr[1] != N:
        arr[1] += 1
    elif M[i] == 'L' and arr[1] != 1:
        arr[1] -= 1
    elif M[i] == 'U' and arr[0] != 1:
        arr[0] -= 1
    elif M[i] == 'D' and arr[0] != N:
        arr[0] += 1
    i += 1

print(arr[0], arr[1])