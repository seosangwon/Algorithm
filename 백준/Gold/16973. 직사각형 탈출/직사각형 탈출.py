from collections import deque
N,M=map(int,input().split())
data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))

H,W,sr,sc,fr,fc=map(int,input().split())

prefix_sum=[[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        prefix_sum[i][j]=prefix_sum[i][j-1]+prefix_sum[i-1][j]-prefix_sum[i-1][j-1]+data[i-1][j-1]

visited=[[False for _ in range(M+1)] for _ in range(N+1)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

#data접근 할 때는 1씩 빼야 하는거 인지
def bfs(x,y):
    q=deque([(x,y,0)])
    visited[x][y]=True

    while q:
        x,y,count=q.popleft()


        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            x1=nx+1
            y1=ny+1

            x2=x1+H-1
            y2=y1+W-1


            if (0 <= nx and 0 <= ny) and (nx+H <= N and ny+W <= M) and visited[nx][ny]==False and (prefix_sum[x2][y2] - prefix_sum[x2][y1-1]-prefix_sum[x1-1][y2]+prefix_sum[x1-1][y1-1]) <1:
                visited[nx][ny]=True
                q.append((nx,ny,count+1))

                if nx==fr-1 and ny==fc-1:
                    return count+1
    return


v=bfs(sr-1,sc-1)
if not v:
    print(-1)
else:
    print(v)
