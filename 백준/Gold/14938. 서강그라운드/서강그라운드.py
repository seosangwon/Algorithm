#지역의 개수 , 수색범위 , 길의 개수
n,m,r=map(int,input().split())
items=list(map(int,input().split()))
items.insert(0,0)
INF=1e10
data=[[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(r):
    start,end,cost=map(int,input().split())
    data[start][end]=cost
    data[end][start]=cost


for i in range(1,n):
    for j in range(1,m):
        if i==j:
            data[i][j]=0


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            data[i][j]=min(data[i][j],data[i][k]+data[k][j])


results=[]
for i in range(1,n+1):
    sum_item=items[i]
    for j in range(1,n+1):
        if  data[i][j]<=m and i!=j:
            sum_item+=items[j]
    results.append(sum_item)

print(max(results))

