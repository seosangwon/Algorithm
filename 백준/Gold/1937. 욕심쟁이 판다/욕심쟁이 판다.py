import sys
input = sys.stdin.read

# 입력 처리
data = input().split()
N = int(data[0])
forest = []
index = 1
for i in range(N):
    forest.append([int(data[index + j]) for j in range(N)])
    index += N

# DP 테이블 초기화
dp = [[0] * N for _ in range(N)]

# 이동 방향 정의 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# DFS 함수 정의
def dfs(x, y):
    if dp[x][y] != 0:  # 이미 계산된 경우
        return dp[x][y]

    dp[x][y] = 1  # 기본적으로 자신을 포함하여 최소 1칸 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and forest[nx][ny] > forest[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]

# 전체 셀에 대해 DFS 수행
max_value = 0
for i in range(N):
    for j in range(N):
        max_value = max(max_value, dfs(i, j))

print(max_value)