import copy
from collections import  deque
n,m=map(int,input().split())
data=[]

for i in range(n):
    data.append(list(input()))


dx=[1,-1,0,0]
dy=[0,0,1,-1]


def bfs(dist,x,y,data1):
    q = deque()
    q.append((0,x,y))
    max_dist=0
    if data1[x][y] == 'W':
        return 0
    while q :
        dist,x,y=q.popleft()
        max_dist=max(max_dist,dist)
        data1[x][y]='W'

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <=ny < m and data1[nx][ny] == 'L':
                data1[nx][ny]='W'
                q.append((dist+1,nx,ny))

    return max_dist


max_value=0
for i in range(n):
    for j in range(m):
        copy_data=copy.deepcopy(data)
        value=bfs(0,i,j,copy_data)
        max_value=max(max_value,value)


print(max_value)


