N, M = map(int, input().split())

edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    s,e,r=map(int,input().split())
    edges[s].append((e,r))
    edges[e].append((s,r))

querys=[]
for _ in range(M):
    s,e=map(int,input().split())
    querys.append((s,e))




def dfs(node , end , visited , r):
    global answer 
    if node==end:
        answer=r 
        exit  
    
    for next_node , dist in edges[node]:
        if not visited[next_node]:
            visited[next_node]=True 
            dfs(next_node,end,visited,r+dist)




for s,e in querys:
    answer=0
    visited=[False]*(N+1)
    visited[s]=True
    dfs(s,e,visited,0)
    print(answer)
    
    




