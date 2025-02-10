n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
visited=[[False]*n for _ in range(n)]
cnt_block=0
max_broken=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y,value,cnt_broken):
    v=1
    

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]==value:
            visited[nx][ny]=True
            v +=dfs(nx,ny,value,cnt_broken+1)
            
    
    return v
    
    
    

     
    


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j]=True # 방문 처리 
            broken=dfs(i,j,grid[i][j],1) # 방문을 안했다면은 dfs 실행
            if broken >=4:
                cnt_block+=1
            max_broken=max(max_broken , broken)






print(cnt_block,max_broken)
    

    


