# 0번부터 N-1번 까지 노드가 있다 
# 각 노드의 부모 노드 리스트를 주어진다 
# 노드를 제거한다 - 노드의 자식 노드까지 제거한다 
# 남아있는 리프노드 개수를 구한다 
# N<=50

n=int(input())
parents=list(map(int,input().split()))
del_node=int(input())
root_node=-1

edges=[[] for _ in range(n)]

for i in range(n):
    x,y=i,parents[i]
    if y==-1:
        root_node=x
        continue
    
    edges[y].append(x)



is_deleted=[False] * n
is_deleted[del_node]=True

answer=0

def dfs(node):
    global answer 

    if is_deleted[node]:
        return 
    
    is_leaf=True

    for edge in edges[node]:
        if is_deleted[edge]:
            continue
        
        is_leaf=False
        dfs(edge)
    
    if is_leaf:
        answer+=1
    

dfs(root_node)
print(answer)










