import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(start, depth):
    if depth == 5:
        return 1
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            if dfs(i, depth + 1):
                return 1
    visited[start] = False
    return 0

for i in range(n):
    visited = [False] * n  # 방문 배열 초기화
    if dfs(i, 1):
        print(1)
        break
else:
    print(0)
