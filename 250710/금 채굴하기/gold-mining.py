from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_area(k):
    return k * k + (k + 1) * (k + 1)

def bfs(x, y, k):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x, y, 0))  # (x좌표, y좌표, 현재 거리)
    visited[x][y] = True

    gold = grid[x][y]  # 시작점의 금

    while q:
        cx, cy, dist = q.popleft()

        if dist == k:
            continue  # k 초과 금지

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if abs(nx - x) + abs(ny - y) <= k:  # 혹시라도 우회한 경로로 k 초과했을 경우 방지
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
                    gold += grid[nx][ny]

    return gold

max_gold = 0

# 각 위치를 중심으로 k 범위 탐색
for x in range(n):
    for y in range(n):
        for k in range(2 * n):  # 넉넉하게 잡기
            gold_count = bfs(x, y, k)
            cost = get_area(k)
            if gold_count * m >= cost:
                max_gold = max(max_gold, gold_count)

print(max_gold)
