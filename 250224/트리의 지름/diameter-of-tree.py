# 트리의 지름 : 임의의 노드 2개 선택시 , 거리가 가장 멀면 지름
# 1. 아무 노드에서 dfs를 실행하여 가장 거리가 먼 노드를 구한다 
# 2. 가장 거리가 먼 노드에서 dfs를 실행하여 가장 먼 거리를 구한다 
import sys
sys.setrecursionlimit(int(1e6))

n=int(input())
edges=[[] for _ in range(n+1)]
for _ in range(n-1):
    s,e,c=map(int,input().split())
    edges[s].append((e,c))
    edges[e].append((s,c))

visited=[False]*(n+1)
distance=[0]*(n+1)

def dfs(node,cost):
    visited[node]=True

    for edge in edges[node]: # 방문을 안했던 노드라면은 
        if not visited[edge[0]]: 
            distance[edge[0]]=(cost+edge[1])
            dfs(edge[0],cost+edge[1])


dfs(1,0)

# 초기화 밑 가장 먼 노드 찾기 
max_dis=-1
max_node=-1

for i in range(1,n+1):
    if max_dis <= distance[i]:
        max_dis=distance[i]
        max_node=i


#초기화 
visited=[False]*(n+1)
distance=[0]*(n+1)

dfs(max_node,0)

max_dis=-1
max_node=-1

for i in range(1,n+1):
    if max_dis <= distance[i]:
        max_dis=distance[i]
        max_node=i

print(max_dis)






    

    
        


