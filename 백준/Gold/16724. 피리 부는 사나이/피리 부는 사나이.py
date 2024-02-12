n,m=map(int,input().split())
data=[]
nodes=[]
INF=int(1e9)
parents=[i for i in range(n*m)]

for _ in range(n):
    data.append(list(input()))



for i in range(n):
    for j in range(m):
        if data[i][j]=='D':
            nodes.append((m*i+j , m*(i+1)+j))
        elif data[i][j]=='U':
            nodes.append((m*i+j , m*(i-1)+j))
        elif data[i][j] == 'L':
            nodes.append((m*i+j , m*i+(j-1)))
        else:
            nodes.append((m * i + j, m * i + (j + 1)))



def find(x):
    if x!=parents[x]:
        x=find(parents[x])
    return x


def union(a,b):
    a=find(a)
    b=find(b)

    if a < b :
        parents[b]=a
    else:
        parents[a]=b


for start,end in nodes:
    if find(start) != find(end):
        union(start,end)

result = len(set(map(find, range(n*m))))
print(result)
