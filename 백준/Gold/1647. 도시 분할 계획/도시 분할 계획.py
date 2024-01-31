
def find(x):
    if parents[x]!=x:
        x=find(parents[x])
    return x


def union(a,b):
    a=find(a)
    b=find(b)

    if a<b:
        parents[b]=a
    else:
        parents[a]=b





n,m=map(int,input().split())
data=[]
parents=[i for i in range(n+1)]

for _ in range(m):
    start,end,cost=map(int,input().split())
    data.append((start,end,cost))

data=sorted(data,key=lambda x : x[2])

count_edge=0
result=0

for value in data:

    if count_edge==n-2:
        print(result)
        break

    node1,node2,cost=value
    if find(node1)!= find(node2):
        union(node1,node2)
        count_edge+=1
        result+=cost

