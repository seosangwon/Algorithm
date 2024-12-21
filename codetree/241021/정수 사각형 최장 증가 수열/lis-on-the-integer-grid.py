n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

dp=[[1 for _ in range(n)] for _ in range(n)] # 시작 값은 전부 1

cells=[]

for i in range(n):
    for j in range(n):
        cells.append((data[i][j],i,j))

cells.sort()

dx=[1,-1,0,0]
dy=[0,0,1,-1]
answer=1
for v,x,y in cells:
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and data[nx][ny] > data[x][y]:
            dp[nx][ny]=max(dp[nx][ny],dp[x][y]+1)
            answer=max(answer,dp[nx][ny])

print(answer)