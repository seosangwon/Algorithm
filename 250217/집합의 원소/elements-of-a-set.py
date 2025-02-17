n, m = map(int, input().split())


# 0 이면 두 노드 합치기 
# 1 이면 find 해서 같은 집합이면 1 출력 , 아니면 0 출력 

parent_node=[i for i in range(n+1)]


def find(n):
    if parent_node[n]==n:
        return n 
    root_node=find(parent_node[n])
    parent_node[n]=root_node
    return root_node

def union(n1,n2):
    r_n1= find(n1)
    r_n2= find(n2)
    if r_n1 < r_n2:
        parent_node[n2]=r_n1
        


for _ in range(m):
    command,n1,n2=map(int,input().split())
    if command==0:
        union(n1,n2)
    if command==1:
        if find(n1) == find(n2):
            print(1)
        else:
            print(0)