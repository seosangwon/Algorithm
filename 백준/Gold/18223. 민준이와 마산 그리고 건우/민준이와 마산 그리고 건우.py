import heapq

n,m,p=map(int,input().split())

graph=[[]for _ in range(n+1)]
for _ in range(m):
    s,e,c=map(int,input().split())
    graph[s].append((e,c))
    graph[e].append((s,c))

INF=int(1e9)



def dijkstra(start):
    distance = [INF for _ in range(n + 1)]
    distance[start]=0
    q=[]

    heapq.heappush(q,(0,start))

    while q:
        dist,cur_node=heapq.heappop(q)
        if distance[cur_node] < dist:
            continue

        for next_node , c in graph[cur_node]:
            cost=dist+c
            if distance[next_node] > cost:
                distance[next_node]=cost
                heapq.heappush(q,(cost,next_node))
    return distance


dis_s=dijkstra(1)
dis_p=dijkstra(p)

if dis_s[n] == dis_s[p]+dis_p[n]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
