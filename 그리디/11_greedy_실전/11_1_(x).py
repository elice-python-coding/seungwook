n = int(input())
m = list(map(int, input().split()))

m.sort()
cnt = 0
m_length = len(m)
while m_length > 0:
    m_length -= max(m)
    for i in range(m_length-1):
        del m[i]
    cnt += 1

print(cnt)
