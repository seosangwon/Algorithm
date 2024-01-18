import sys
sys.setrecursionlimit(100000)

n=int(input())
graph=[[]for _ in range(n+1)]

for _ in range(n-1):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))


#DFS
def dfs(node,dist):
    for next_node,cost in graph[node]:
        if visited[next_node] ==-1:
            visited[next_node]=dist+cost
            dfs(next_node,dist+cost)


#1번 노드부터 시작
visited=[-1 for _ in range(n+1)]
visited[1]=0
dfs(1,0)
max_value=max(visited)
max_node=visited.index(max_value)

#max_node에서 DFS
visited=[-1 for _ in range(n+1)]
visited[max_node]=0
dfs(max_node,0)

print(max(visited))


