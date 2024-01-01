n, m, k = map(int, input().split())
data = []
hash_map = {}
length=0
for _ in range(n):
    data.append(list(input()))

for _ in range(k):
    god_str = input()
    length=len(god_str)
    hash_map[god_str] = 0

# 행, 열, 대각선 이동
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y, cost, value):
    global length
    if cost == length:
        if value in hash_map:
            hash_map[value] += 1
        return

    for i in range(8):
        nx = (x + dx[i]) % n
        ny = (y + dy[i]) % m
        dfs(nx, ny, cost + 1, value + data[nx][ny])

for i in range(n):
    for j in range(m):
        dfs(i, j, 1, data[i][j])

for key in hash_map:
    print(hash_map[key])
