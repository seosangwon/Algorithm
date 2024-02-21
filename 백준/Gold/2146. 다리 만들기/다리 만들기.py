from collections import deque
n=int(input())
data=[]

for _ in range(n):
    data.append(list(map(int,input().split())))

visited=[[False for _ in range(n)] for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs_district(x,y,c):
    if visited[x][y]==True:
        return
    visited[x][y]=True
    data[x][y]=c
    q=deque([(x,y,c)])
    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and data[nx][ny]!=0:
                visited[nx][ny]=True
                data[nx][ny]=c
                q.append((nx,ny,c))
    return True

c=2
for i in range(n):
    for j in range(n):
        if data[i][j]!=0:
            if (bfs_district(i,j,c)):
                c+=1





def bfs(x,y,c,cost):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y]=True
    q=deque([(x,y,c,cost)])
    while q:
        x,y,c,cost=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and data[nx][ny]!=c:
                if data[nx][ny] !=0 :
                    return cost
                visited[nx][ny]=True
                q.append((nx,ny,c,cost+1))
    return False



# for i in range(n):
#     for j in range(n):
#         print(data[i][j],end=' ')
#     print()


min_value=int(1e9)
for i in range(n):
    for j in range(n):
        if data[i][j]!=0:
            value = bfs(i,j,data[i][j],0)
            if value:
                min_value=min(min_value,value)

print(min_value)


