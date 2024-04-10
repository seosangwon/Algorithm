import heapq

n,t=map(int,input().split())
data=[[] for _ in range(n+1)]

for _ in range(t):
    start,end,cost=map(int,input().split())
    data[start].append((end,cost))
    data[end].append((start,cost))

s,e=map(int,input().split())

INF=1e9
distance=[INF for _ in range(n+1)]
# print(data)

def dijkstra(start):
    q=[]
    distance[start]=0
    for end,cost in data[start]:
        heapq.heappush(q,(cost,end))

    while q:
        dist,node=heapq.heappop(q)
        # print(dist,node)
        if distance[node] < dist:
            continue

        distance[node]=dist

        for next_node, c in data[node]:
            cost=dist + c
            if distance[next_node] > cost:
                heapq.heappush(q,(cost,next_node))
                distance[next_node]=cost

    return

dijkstra(s)


print(distance[e])