import heapq
n=int(input())
data=[]
INF=int(1e9)
distance=[[INF for _ in range(n)] for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(n):
    data.append(list(map(int,input())))



def dijkstra():
    q=[]
    heapq.heappush(q,(0,0,0))
    distance[0][0]=0
    while q:
        cost,x,y=heapq.heappop(q)
        if distance[x][y] < cost:
            continue

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n :
                if data[nx][ny]==0: # 다음 노드가 검은색 노드라면
                    next_cost=cost+1
                    if  next_cost < distance[nx][ny]:
                        distance[nx][ny]=next_cost
                        heapq.heappush(q,(next_cost,nx,ny))
                else: #다음 노드가 흰색 노드라면
                    if cost < distance[nx][ny]:
                        distance[nx][ny]=cost
                        heapq.heappush(q,(cost,nx,ny))

dijkstra()
print(distance[-1][-1])


