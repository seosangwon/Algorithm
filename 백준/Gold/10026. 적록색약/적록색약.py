from collections import deque
n=int(input())
data=[list(input()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

#R,G,B BFS

dx=[-1,1,0,0]
dy=[0,0,1,-1]


def bfs_RGB(x,y,visited,data):
  if visited[x][y]==True:
      return 0
  q=deque([(x,y)])
  while(q):
    x,y = q.popleft()
    visited[x][y]=True
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n :
        continue
      if  data[nx][ny]!=data[x][y] or visited[nx][ny] == True:
        continue
      visited[nx][ny]=True
      q.append((nx,ny))
  return 1

result1=0
result2=0

for i in range(n):
  for j in range(n):
    result1+= bfs_RGB(i,j,visited,data)

visited=[[False]*n for _ in range(n)]


for i in range(n):
  for j in range(n):
    if data[i][j]=='G':
      data[i][j]='R'

for i in range(n):
  for j in range(n):
    result2+=bfs_RGB(i,j,visited,data)


print(result1,result2)
  