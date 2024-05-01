
N,M=map(int,input().split())
data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))


dx=[1,-1,0,0]
dy=[0,0,1,-1]
count=0
visited=[[False for _ in range(M)] for _ in range(N)]
visited[0][0]=True
dp=[[-1 for _ in range(M)] for _ in range(N)]




def dfs(x,y):
    global count
    if x==N-1 and y==M-1:
        count+=1
        return 1

    if dp[x][y]!=-1: # 이미 방문했다면
        return dp[x][y]

    path_count=0



    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and data[x][y]>data[nx][ny]:
            visited[nx][ny]=True
            path_count+=dfs(nx,ny)
            visited[nx][ny]=False
        dp[x][y]=path_count

    return path_count






result=dfs(0,0)
#print(count)
print(result)
