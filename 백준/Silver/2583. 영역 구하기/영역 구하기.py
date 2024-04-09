from collections import deque
#M이 열 , N이 행
M,N,K=map(int,input().split())
data=[[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            data[i][j]=1

# for i in range(N):
#     for j in range(M):
#         print(data[i][j],end=' ')
#     print()



visited=[[False for _ in range(M)] for _ in range(N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs (x,y):
    visited[x][y]=True
    q=deque([(x,y)])
    c=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and data[nx][ny]==0:
                # print(nx,ny)
                c+=1
                visited[nx][ny]=True
                q.append((nx,ny))

    return c







result=[]
for i in range(N):
    for j in range(M-1,-1,-1):
        if data[i][j]==0 and visited[i][j]==False:
            value=bfs(i,j)
            result.append(value)



result.sort()
print(len(result))
for v in result:
    print(v,end=' ')

