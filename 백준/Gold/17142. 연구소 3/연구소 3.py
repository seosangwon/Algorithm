from itertools import combinations
from collections import deque
import copy

#N은 칸수 , M은 놓을 수 있는 바이러스 개수
N,M=map(int,input().split())

data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))

virus=[]
for i in range(N):
    for j in range(N):
        if data[i][j]==2:
            data[i][j]='*'
            virus.append((i,j))
        elif data[i][j]==1:
            data[i][j]='-'

comb_virus=list(combinations(virus,M))



dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(vi,c_data):
    visited=[[False for _ in range(N)] for _ in range(N)]
    q=deque([])
    for x,y in vi:
        visited[x][y]=True
        c_data[x][y]='!'
        q.append((x,y,0))

    while q:
        x,y,t=q.popleft() # 좌표 , 시간
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False and c_data[nx][ny]==0 :
                visited[nx][ny]=True
                c_data[nx][ny]=t+1
                q.append((nx,ny,t+1))

            elif 0<=nx<N and 0<=ny<N and visited[nx][ny]==False and c_data[nx][ny] == '*':
                visited[nx][ny]=True
                q.append((nx,ny,t+1))


    max_value=0
    for i in range(N):
        for j in range(N):
            if isinstance(c_data[i][j], int):
                if c_data[i][j]==0:
                    return 1e9
                max_value=max(max_value,c_data[i][j])


    # for i in range(N):
    #     for j in range(N):
    #         print(c_data[i][j],end=' ')
    #     print()
    # print()

    return max_value




min_value=1e9
for v in comb_virus:
    value=bfs(v,copy.deepcopy(data))
    min_value=min(value,min_value)


if min_value==1e9:
    print(-1)
else:
    print(min_value)
