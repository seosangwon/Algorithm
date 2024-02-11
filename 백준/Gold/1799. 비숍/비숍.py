n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 대각선 방향 점유 여부 확인을 위한 배열
diagonal1 = [False] * (2 * n - 1)  # / 방향
diagonal2 = [False] * (2 * n - 1)  # \ 방향

result = [0, 0]  # 각 색깔별로 최대 비숍 개수 저장

def backtrack(x, y, count, color):
    global n, result, board, diagonal1, diagonal2
    if y >= n:
        x += 1
        y = (y + 1) % 2  # 다음 행의 시작 칸 색깔 조정
    if x == n:
        result[color] = max(result[color], count)
        return
    if board[x][y] == 1 and not diagonal1[x+y] and not diagonal2[x-y+n-1]:
        diagonal1[x+y] = diagonal2[x-y+n-1] = True
        backtrack(x, y+2, count+1, color)  # 비숍을 놓는 경우
        diagonal1[x+y] = diagonal2[x-y+n-1] = False
    backtrack(x, y+2, count, color)  # 비숍을 놓지 않는 경우

# 흰 칸과 검은 칸 각각에 대해 백트래킹 수행
backtrack(0, 0, 0, 0)  # 흰 칸 시작
backtrack(0, 1, 0, 1)  # 검은 칸 시작

print(sum(result))  # 흰 칸과 검은 칸에서의 최대 비숍 개수 합
