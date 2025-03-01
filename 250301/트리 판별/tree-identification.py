m = int(input())
edges=[]
# 트리 판별 요건 : 사이클이 없는지 확인 , 루트 노드에서 모든 노드로 이동 할 수 있는지 확인 

# 1. 루트 노드 찾기 
# 2. dfs로 전체 순회 
# 3. 사이클이 발생하면은 return 0 
# 4. dfs 종료 후 , 모든 노드가 방문 처리 되어 있다면은 return 1 

# 루트 노드 찾기 
max_node=-1

for _ in range(m):
    s,e=map(int,input().split())
    edges.append([s,e])
    max_node=max(max_node , s, e )

in_edges=[[] for _ in range(max_node+1)]
out_edges=[[] for _ in range(max_node+1)]
for s,e in edges:
    in_edges[e].append(s)
    out_edges[s].append(e)

def find_root(in_edges):
    root_node=-1
    cnt=0
    for i in range(1,max_node+1):
        if len(in_edges[i])==0:
            root_node=i 
            cnt+=1
        if cnt>=2:
            break 
    
    if cnt>=2:
        return -1 
    
    return root_node


visited=[False]*(max_node+1)
flag=True

def dfs(node):
    global flag
    visited[node]=True  # 노드 방문 처리 

    for next_node in out_edges[node]:
        if visited[next_node]: # 만약 방문이 이미 되어있다면 경로가 유일하지 않은 것 
            flag=False 

        
        if not visited[next_node]:
            dfs(next_node)
    
    return flag
        
        

            



def is_root():
    root_node = find_root(in_edges)
    if root_node== -1: # 루트 노드가 여러개 
        # print("루트 노드 여러개 ")
        # print(in_edges)
        return 0
    
    if not dfs(root_node): # 사이클 존재 
        print("사이클 존재")
        return 0 

    
    if False in visited[1:] : # 모든 노드 존재 방문 
        print("모든 노드 방문 x ")
        return 0 
    
    
    return 1 


print(is_root())


    











    
    

