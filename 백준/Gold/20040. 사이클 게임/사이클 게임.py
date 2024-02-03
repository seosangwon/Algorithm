import sys
input=sys.stdin.readline

def find(a):
    if parents[a]!=a:
       a=find(parents[a])
    return a

def union (a , b):
    a = find(a)
    b= find(b)

    if a < b:
        parents[b]=a
    else:
        parents[a]=b


n ,m = map(int,input().split())
data=[]
parents=[i for i in range(n)]
count=1

for _ in range(m):
    start,end=map(int,input().split())
    data.append((start,end))



for node1 , node2 in data:
    if find(node1) != find(node2):
        union(node1 , node2)
        count+=1
    else:
        print(count)
        break

if count==m+1:
    print(0)


