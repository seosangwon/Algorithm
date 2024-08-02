# 입력 받기
N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
answer = input()

# 초기 설정
len_answer = len(answer)
dp = [[[-1] * len_answer for _ in range(M)] for _ in range(N)]

# 방향 이동 설정 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# DFS 함수 정의
def dfs(x, y, idx):
    # 이미 계산된 경로 수가 있으면 그 값을 반환
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]

    # 만약 마지막 글자를 찾았다면 경로를 하나 찾았으므로 1을 반환
    if idx == len_answer - 1:
        return 1

    # 경로의 수 초기화
    count = 0

    # K만큼 상하좌우로 이동할 수 있는 모든 경우 탐색
    for direction in range(4):
        for step in range(1, K + 1):
            nx, ny = x + dx[direction] * step, y + dy[direction] * step

            # 경계를 넘지 않으며, 다음 글자가 맞으면 DFS 호출
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == answer[idx + 1]:
                count += dfs(nx, ny, idx + 1)

    # 현재 위치와 idx에 대한 경로의 수 저장
    dp[x][y][idx] = count
    return count

# 초기 시작점에서 DFS 호출
result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == answer[0]:  # 첫 글자가 맞으면 시작
            result += dfs(i, j, 0)

# 결과 출력
print(result)
