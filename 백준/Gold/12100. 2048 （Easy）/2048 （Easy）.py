import copy
from collections import deque

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

#상 하 좌 우
dx=[-1,1,0,0,]
dy=[0,0,-1,1]
def move(dir,data):
    #상 좌는 (0,0)부터 순차적으로 탐색
    changed=[]
    if dir==0 or dir==2:
        for i in range(n):
            for j in range(n):
                if data[i][j]!=0:
                    bfs_move(dir,i,j,data,changed) # 방향 , 좌표

    else: #하 우는 (n-1,n-1)부터 역순을 퇌색
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if data[i][j]!=0:
                    bfs_move(dir, i, j, data , changed)  # 방향 , 좌표

    return data



def bfs_move(dir,x,y,data,changed):
    
    q=deque([(dir,x,y)])
    while q:
        dir,x,y=q.popleft()


        nx=x+dx[dir]
        ny=y+dy[dir]

        if 0<=nx<n and 0<=ny<n and data[nx][ny]==data[x][y] and (nx,ny) not in changed:
            data[nx][ny]=data[x][y]*2 # 값 합치기
            data[x][y] = 0  # 원래 좌표는 0
            changed.append((nx,ny))

        elif  0<=nx<n and 0<= ny < n and data[nx][ny]==0:
            data[nx][ny]=data[x][y]
            data[x][y]=0
            q.append((dir,nx,ny))








max_value=0
def dfs(idx,data):
    global max_value
    if idx==5:
        for i in range(n):
            for j in range(n):
                max_value=max(max_value,data[i][j])
        return

    for i in range(4):
        moved_data=move(i,copy.deepcopy(data))
        dfs(idx+1,moved_data)


dfs(0,graph)
print(max_value)
