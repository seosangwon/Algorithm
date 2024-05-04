from collections import deque
#세로 ,가로, ,음식물 개수
n,m,k=map(int,input().split())

#0은 음식물이 없는 공간
graph=[[0]*m for _ in range(n)]

for _ in range(k):
  #음식물이 있는 공간 입력받기
  x,y=map(int,input().split())
  graph[x-1][y-1]=1

#bfs 준비물
dx=[-1,1,0,0]
dy=[0,0,1,-1]

#bfs
def bfs(graph,x,y):
  if graph[x][y]==0:
    return 0
    
  q=deque()
  q.append((x,y))
  count=0
  while q:
    a,b=q.popleft()
    if graph[a][b]==1:
      count+=1
      graph[a][b]=2
      for k in range(4):
        nx=a+dx[k]
        ny=b+dy[k]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1 :
          q.append((nx,ny))
  #print(count)
  return count


result=[]
for i in range(n):
  for j in range(m):
    result.append(bfs(graph,i,j))



print(max(result))