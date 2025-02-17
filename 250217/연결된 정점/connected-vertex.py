# 간선을 연결 할 때 마다 집합의 노드 개수를 count 해줘야 할 것 같다 
N,M=map(int,input().split()) # 노드 , 간선 개수
counts=[1]*(N+1)
parent_node=[i for i in range(N+1)]


def find(node):
    if parent_node[node]==node:
        return node
    root_node = find(parent_node[node])
    parent_node[node]=root_node
    return root_node

def union(n1,n2):
    r_n1= find(n1)
    r_n2 = find(n2)

    if r_n1 < r_n2:
        parent_node[r_n2]=r_n1 
        counts[r_n1]+=counts[r_n2]
        counts[r_n2]=0
    
    else:
        parent_node[r_n1]=r_n2
        counts[r_n2]+=counts[r_n1]
        counts[r_n1]=0
    

for _ in range(M):
    l=list(input().split())
    if l[0]=='x':
        n1,n2=map(int,l[1:])
        union(n1,n2)
    if l[0]=='y':
        r_n = find(int(l[1]))
        print(counts[r_n])
        
