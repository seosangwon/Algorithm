
import heapq
#n은 행 , m은 열
m,n=map(int,input().split())
data=[[] for _ in range(n)]
for i in range(n):
    value=list(input())
    for j in value:
        j=int(j)
        data[i].append(j)

INF=1e10
wall_count=[[INF for _ in range(m)] for _ in range(n) ]

dx=[1,-1,0,0]
dy=[0,0,1,-1]




def dijkstra(start_x,start_y):
    q=[]
    wall_count[start_x][start_y]=0
    heapq.heappush(q,(0,start_x,start_y))
    while q:
        now_wall,now_x,now_y=heapq.heappop(q)

        #갱신되서 온 정보가 , wall_count에 저장된 벽읙 개수보다 많다면 필요없으니 버린다
        if wall_count[now_x][now_y] < now_wall:
            continue

        for i in range(4):
            nx=now_x+dx[i]
            ny=now_y+dy[i]
            if  0<=nx<n and 0<=ny<m:
                next_wall=now_wall+data[nx][ny]
            else:
                continue

            if wall_count[nx][ny] > next_wall:
                wall_count[nx][ny]=next_wall
                heapq.heappush(q,(next_wall,nx,ny))
    

    return wall_count[n-1][m-1]

print(dijkstra(0,0))