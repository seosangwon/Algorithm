# 0번부터 N-1번 까지 노드가 있다 
# 각 노드의 부모 노드 리스트를 주어진다 
# 노드를 제거한다 - 노드의 자식 노드까지 제거한다 
# 남아있는 리프노드 개수를 구한다 
# N<=50

n=int(input())
parents=list(map(int,input().split()))
del_node=int(input())

# 리프 노드 후보 구하기 
set_parents=set(parents)
leaf_can=[]

for i in range(n):
    if i not in set_parents:
        leaf_can.append(i)


def dfs(node):
    
    if parents[node]==del_node:
        return True
    
    if parents[node]==-1:
        return False

    return dfs(parents[node])


for node in leaf_can[:]:
    #print(node)
    if dfs(node):
        leaf_can.remove(node)

print(len(leaf_can))




