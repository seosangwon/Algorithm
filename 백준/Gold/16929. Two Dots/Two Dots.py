N,M=map(int,input().split()) # 행 , 열
data=[]
for _ in range(N):
    data.append(list(input()))




visited=[[False for _ in range(M)] for _ in range(N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(s_x,s_y,x,y,depth,alpha): # x,y,depth
    if s_x==x and s_y == y and depth>=4:
        return True

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and data[nx][ny]==alpha:
            visited[nx][ny]=True
            if (dfs(s_x,s_y,nx,ny,depth+1,alpha)):
                return True
            visited[nx][ny]=False

    return False # 종료,정답 조건이 실행되면은 이 코드는 실행 안됨





for i in range(N):
    for j in range(M):
        if dfs(i,j,i,j,1,data[i][j]):
            print("Yes")
            exit()

print("No")