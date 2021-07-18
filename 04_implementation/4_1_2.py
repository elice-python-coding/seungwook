N = int(input())
cnt_3 = (15 * 45) + (60 * 15) # 시간당 3이 나오는 횟수 

cnt = 0
if N < 3:
    cnt = cnt_3 * (N+1)
elif N >= 3 and N < 13:
    cnt = (cnt_3 * N) + 3600
elif N >= 13 and N < 23:
    cnt = (cnt_3 * (N-1)) + 3600 * 2
else:
    cnt = (cnt_3 * (N-2)) + 3600 * 3

print(cnt)