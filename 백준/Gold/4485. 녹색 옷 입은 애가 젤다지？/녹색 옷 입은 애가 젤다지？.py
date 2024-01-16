import heapq


# return은 distance[n-1][n-1]
def dijkstra(start_x, start_y):
    q = []
    distance[start_x][start_y] = data[start_x][start_y]
    heapq.heappush(q, (distance[start_x][start_y], start_y, start_y))
    while q:
        dist, now_x, now_y = heapq.heappop(q)
        if distance[now_x][now_y] < dist:
            continue
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            cost = 0
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + data[nx][ny]
            else:
                continue
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    return distance[n - 1][n - 1]


i=0

while(True):
    n=int(input())
    if n==0:
        break
    i+=1
    data=[]
    INF=1e15
    distance=[[INF for _ in range(n)] for _ in range(n)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for _ in range(n):
        data.append(list(map(int,input().split())))

    print("Problem "+str(i)+': '+str(dijkstra(0,0)))
