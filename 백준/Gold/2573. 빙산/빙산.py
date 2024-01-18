from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def year():
    minus = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0:
                count = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                        count += 1
                minus[i][j] = count
    for i in range(n):
        for j in range(m):
            data[i][j] -= minus[i][j]
            if data[i][j] < 0:
                data[i][j] = 0

def bfs(x, y):
    if data[x][y] == 0 or visited[x][y]:
        return 0
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    return 1  # 연결된 얼음 덩어리를 찾을 때마다 1 반환

result = 0
while True:
    year()  # 얼음이 녹는 과정
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and not visited[i][j]:
                count += bfs(i, j)  # 연결된 얼음 덩어리 수 세기
    result += 1
    if count >= 2:
        print(result)
        break
    if all(data[i][j] == 0 for i in range(n) for j in range(m)):
        print(0)
        break
