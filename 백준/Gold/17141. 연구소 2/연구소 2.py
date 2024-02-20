import copy
from itertools import combinations
from collections import deque

n,m=map(int,input().split())
data=[]
virus=[]

for _ in range(n):
    data.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j]==1:
            data[i][j]=-1
        elif data[i][j]==2:
            virus.append((i,j))

comb_virus=list(combinations(virus,m))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(li):
    copy_data=copy.deepcopy(data)
    for i in range(n):
        for j in range(n):
            if (i,j) in li:
                copy_data[i][j]=-2
                continue
            if copy_data[i][j]==2:
                copy_data[i][j]=0

    visited=[[False for _ in range(n)] for _ in range(n)]

    q=deque([])
    for x,y in li:
        q.append((x,y,0))
        visited[x][y]=True

    while q:
        x,y,cost=q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny= y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and copy_data[nx][ny] == 0:
                copy_data[nx][ny]=cost+1
                visited[nx][ny]=True
                q.append((nx,ny,cost+1))

    # for i in range(n):
    #     for j in range(n):
    #         print(copy_data[i][j],end=' ')
    #     print()

    v=0
    for i in range(n):
        for j in range(n):
            if copy_data[i][j]==0:
                return int(1e9)
            if 1<= copy_data[i][j] <=int(1e9):
                v=max(v,copy_data[i][j])

    return v













min_value=int(1e9)
for i in range(len(comb_virus)):
    value=bfs(comb_virus[i])
  # print()
    min_value=min(min_value,value)



if min_value == int(1e9):
    print(-1)
else:
    print(min_value)

