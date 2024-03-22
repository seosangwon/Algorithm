from collections import deque
import copy

r,c,t=map(int,input().split())
data=[]
ac=[]

for _ in range(r):
    data.append(list(map(int,input().split())))

dust=[]

for i in range(r):
    for j in range(c):
        if data[i][j] > 0 :
            dust.append((i,j,data[i][j]))
        elif data[i][j]==-1:
            ac.append((i,j))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

#파라미터로 받은 copy_data에 대해 값을 저장한다
def bfs(copy_data):
    q=deque(dust)
    while q:
        x,y,m=q.popleft()
        a=copy_data[x][y]//5  # 원본 값에서 체크
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and copy_data[nx][ny]!=-1:
               data[nx][ny]+=a # 가능한 4방향으로 확산
               data[x][y]-=a





#이게 어려움
r_d1=[(-1,0),(0,1),(1,0),(0,-1)]
r_d2=[(1,0),(0,1),(-1,0),(0,-1)]

def air_condition1(x,y): # x,y는 공기청정기 윗 좌표
    origin_x=x
    origin_y=y
    nx,ny=x,y

    for i in range(4):
        nx += r_d1[i][0]
        ny += r_d1[i][1]
        while 0<= nx <= origin_x and 0<=ny< c:
            if nx==origin_x and ny==origin_y:
                data[origin_x][origin_y+1]=0
                break
            data[nx-r_d1[i][0]][ny-r_d1[i][1]]=data[nx][ny]
            nx+=r_d1[i][0]
            ny+=r_d1[i][1]
        nx-=r_d1[i][0]
        ny-=r_d1[i][1]

    data[x][y]=-1

def air_condition2(x,y): # x,y는 공기청정기 윗 좌표
    origin_x=x
    origin_y=y
    nx,ny=x,y

    for i in range(4):
        nx += r_d2[i][0]
        ny += r_d2[i][1]
        while origin_x<= nx < r and 0<=ny< c:
            if nx==origin_x and ny== origin_y:
                data[origin_x][origin_y + 1] = 0
                break
            data[nx-r_d2[i][0]][ny-r_d2[i][1]]=data[nx][ny]
            nx+=r_d2[i][0]
            ny+=r_d2[i][1]
        nx-=r_d2[i][0]
        ny-=r_d2[i][1]

    data[x][y]=-1







for _ in range(t):
    bfs(copy.deepcopy(data)) # 원본 값 업데이트
    air_condition1(ac[0][0],ac[0][1])
    air_condition2(ac[1][0],ac[1][1])
    dust=[]
    for i in range(r):
        for j in range(c):
            if data[i][j]>0:
                dust.append((i,j,data[i][j]))






result=0
for i in range(r):
    for j in range(c):
        if data[i][j]>0:
            result+=data[i][j]

print(result)
