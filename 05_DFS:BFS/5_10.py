N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input())))

## 행과 열이 -1 인덱스까지 인접한 0이 있으면 전부 1로 변환
for x in range(N-1):
    for y in range(M-1):
        if arr[x][y] == 0 and arr[x][y+1] == 0 and arr[x+1][y] == 0:
            ## x행 전부다 1
            for i in range(M-1):
                arr[x][i] = 1
        elif arr[x][y] == 0 and arr[x+1][y] == 0:
            arr[x][y] = 1
        elif arr[x][y] == 0 and arr[x][y+1] == 0:
            arr[x][y] = 1

## 열은 마지막 인덱스로 고정하고 행을 -1번째까지 인접한 0 이 있으면 1로 변환
for x in range(N-1):
    if arr[x][M-1] == 0 and arr[x+1][M-1] == 0:
        arr[x][M-1] = 1

## 행은 마지막 인덱스로 픽스하고 열을 -1번째 인덱스까지 인접한 0이 있으면 1로 변환
for y in range(M-1):
    if arr[N-1][y] == 0 and arr[N-1][y+1] == 0:
        arr[N-1][y] = 1

## 남은 총 0의 갯수를 세어줌
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt += 1

print(cnt)