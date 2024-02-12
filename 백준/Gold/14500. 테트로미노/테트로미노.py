n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
visited=[[False for _ in range (m)] for _ in range(n)]
max_value=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

#첫 실행시 depth=1 , value=data[x][y], visited[x][y]=True로 보내준다
def dfs(depth,x,y,value):
    global max_value
    global init_x,init_y
    if depth==5:
        #print(value)
        max_value=max(max_value,value)
        return

    for i in range(4):
        nx= x + dx[i]
        ny= y + dy[i]
        if 0<=nx<n and 0<=ny <m and visited[nx][ny]==False:
            visited[nx][ny]=True
            dfs(depth+1,nx,ny,value+data[nx][ny])
            visited[nx][ny]=False
        elif 0<=nx<n and 0<=ny <m and nx==init_x and ny==init_y:
            dfs(depth,nx,ny,value)




for i in range(n):
    for j in range(m):
        init_x,init_y=i,j
        dfs(1,i,j,0)



print(max_value)
