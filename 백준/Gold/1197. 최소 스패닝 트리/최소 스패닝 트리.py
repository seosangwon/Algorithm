n,m=map(int,input().split())
parents=[i for i in range(n+1)]
data=[]
for _ in range(m):
    start,end,cost=map(int,input().split())
    data.append((start,end,cost))

data=sorted(data,key=lambda x:x[2])


def find(parents,a):
    if parents[a]!=a:
        parents[a]=find(parents,parents[a])
    return parents[a]


def union(a,b):
    a=find(parents,a)
    b=find(parents,b)


    if a<b:
        parents[b]=a
    else:
        parents[a]=b

result=0

for i in range(m):
    n1,n2,cost=data[i][0],data[i][1],data[i][2]
    if find(parents,n1) != find(parents,n2):
        union(n1,n2)
        result+=cost

print(result)
