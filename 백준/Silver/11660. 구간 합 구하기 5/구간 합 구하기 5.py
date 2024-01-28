n,m=map(int,input().split())
data=[]
points=[]

for _ in range(n):
    data.append(list(map(int,input().split())))

for _ in range(m):
    points.append(list(map(int,input().split())))

dp_sum=[[0 for _ in range(n+1)] for _ in range(n+1)]



for i in range(1,n+1):
    for j in range(1,n+1):
        dp_sum[i][j]=dp_sum[i][j-1]+dp_sum[i-1][j] - dp_sum[i-1][j-1] + data[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2=points[i]
    result=dp_sum[x2][y2]-dp_sum[x2][y1-1]-dp_sum[x1-1][y2]+dp_sum[x1-1][y1-1]
    print(result)