# 1. 다른 모든 정점과의 거리의 최대값이 , 최소가 되는 노드를 찾는다 
    # 각 노드 별로 가장 먼 거리의 값을 찾는다 
# 2. 그 노드로부터 가장 먼 거리 값을 찾는다 

# 각 노드별로 1번씩 실행 (1e5) X dfs 로직 내에서 각 노드별로의 거리를 구해야함 (1e5)

n = int(input())
visited=[False]*(n+1)
dist=[0]*(n+1)
edges=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(node):
    
    for next_node in edges[node]:
        if not visited[next_node]:
            visited[next_node]=True 
            dist[next_node]=dist[node]+1
            dfs(next_node)





visited[1]=True
dfs(1) # 아무 노드로 dfs 실행 해서 가장 먼 노드 찾기 
so_far_node=0
max_distance=0
for node in range(1,n+1):
    if max_distance < dist[node]:
        max_distance=dist[node]
        so_far_node=node 


# reset
visited=[False]*(n+1)
dist=[0]*(n+1)

visited[so_far_node]=True
dfs(so_far_node)
max_distance=max(dist)
answer=(max_distance+1)//2

print(answer)





