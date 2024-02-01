import sys
input = sys.stdin.readline

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


n=int(input())
data=[]
parents=[i for i in range(n+1)]
edges=[]
result=0
count_edge=0

for i in range(1,n+1):
    x,y,z=map(int,input().split())
    data.append((x,y,z,i))




#x,y,z로 각각 정렬
for k in range(3):
    data=sorted(data,key=lambda x:x[k])
    count=0
    for i in range(n-1):
        if count==n+1:
            break
        cost=min( (abs(data[i][0]-data[i+1][0])) , (abs(data[i][1]-data[i+1][1])) , (abs(data[i][2]-data[i+1][2]))  )
        edges.append((cost,data[i][3], data[i+1][3]))



edges.sort()


for edge in edges:
    if count_edge==n-1:
        print(result)
        break

    cost,node1,node2=edge
    if find(node1) != find(node2):
        union(node1,node2)
        result+=cost
        count_edge+=1

