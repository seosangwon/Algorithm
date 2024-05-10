import heapq

N,M=map(int,input().split())
data=[]
for _ in range(N):
    data.append(list(input()))


start=[]
end=[]
trash_list=[]

for i in range(N):
    for j in range(M):
        if data[i][j]=='F':
            end.append((i,j))
        elif data[i][j]=='S':
            start.append((i,j))
        elif data[i][j]=='g':
            trash_list.append((i,j))



dx=[1,-1,0,0]
dy=[0,0,1,-1]

def check_adj_trash(x,y): # adj_trash는 1로 표시
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and data[nx][ny]=='.':
            data[nx][ny]=1
    return



def dijkstra(x,y):
    visited=[[False for _ in range(M)] for _ in range(N)]
    visited[x][y]=True
    q=[]
    heapq.heappush(q,(0,0,x,y)) # 쓰레기를 지나치는 수 , 쓰레기를 옆에 지나치는 수 , 좌표
    while q:
        trash,adj_trash,x,y=heapq.heappop(q)
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == False :
                visited[nx][ny]=True
                if data[nx][ny]=='g':
                    heapq.heappush(q,(trash+1,adj_trash,nx,ny))
                elif data[nx][ny]=='.':
                    heapq.heappush(q,(trash,adj_trash,nx,ny))
                elif data[nx][ny]==1:
                    heapq.heappush(q,(trash,adj_trash+1,nx,ny))
                elif data[nx][ny]=='F':
                    return (trash,adj_trash)










for x,y in trash_list: # 쓰레기 옆 주위 먼저 표시
    check_adj_trash(x,y)

t,adj_t=dijkstra(start[0][0],start[0][1])

print(t,adj_t)
