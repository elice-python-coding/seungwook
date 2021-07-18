from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

## 오른, 아래, 위, 왼 배치를 위해
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    ## 큐가 빌때까지
    while queue:
        x, y = queue.popleft()
        ## 오른쪽, 아래, 위, 왼쪽 순서
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 밖 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 0 만나면 무시
            if arr[nx][ny] == 0:
                continue
            # 1인곳으로 위치 이동하면서 카운트 + 1 & 반복위해 큐에 채워줌
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))

    return arr[n-1][m-1]  # 오른아래끝에서 카운트 반환

print(bfs(0, 0))