#간선이 많은 경로를 찾는다. 만약 간선의 개수가 같을 경우 거리가 더 짧은 경로를 찾는다 
import sys
sys.setrecursionlimit(int(1e6))

N,D = map(int, input().split()) #N은 노드 개수 , D는 하루에 갈 수 있는 값
edges=[[] for _ in range(N+1)]
for _ in range(N-1):
    s,e,d=map(int,input().split())
    edges[s].append((e,d))
    edges[e].append((s,d))

dist_cnt=[0]*(N+1) # 시작 노드와 각 노드간의 간선 개수 
distance=[0]*(N+1) # 시작 노드와 각 노드간의 거리 
visited=[False]*(N+1)


max_dist=(0,0)
last_node=0

def dfs(node):
    global max_dist, last_node

    for n_node , n_dist in edges[node]:
        if not visited[n_node]:
            visited[n_node]=True 
            dist_cnt[n_node]=dist_cnt[node]+1
            distance[n_node]=distance[node]+n_dist 

            cur_dist=(dist_cnt[n_node],-distance[n_node])

            if cur_dist > max_dist:
                max_dist=cur_dist
                last_node=n_node 
            
            dfs(n_node)


visited[1]=True 
dfs(1)

for i in range(N+1):
    visited[i]=False
    dist_cnt[i]=0
    distance[i]=0

visited[last_node]=True 
dfs(last_node)

print(1+(-max_dist[1]-1)//D)





