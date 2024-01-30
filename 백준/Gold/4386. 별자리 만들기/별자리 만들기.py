import math
def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a<b:
        parents[b]=a
    else:
        parents[a]=b


n=int(input())
star=[0]
parents=[i for i in range(n+1)]


for i in range(n):
    start,end=map(float,input().split())
    star.append((start,end))



edges=[]

for i in range(1,n+1):
    for j in range(i+1,n+1):
        cost=math.sqrt( (star[i][0]-star[j][0])**2 + (star[i][1]-star[j][1])**2 )
        cost=round(cost,2)
        edges.append((cost,i,j))



edges.sort()
edge_count=0
result=0

for edge in edges :
    if edge_count== n-1:
        print(result)
        break

    cost , node1, node2 = edge
    if find(node1) != find(node2):
        union(node1, node2)
        result+=cost
        edge_count+=1


