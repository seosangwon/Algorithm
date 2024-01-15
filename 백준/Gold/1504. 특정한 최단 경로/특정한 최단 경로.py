import heapq
#노드의 개수 , 간선의 개수
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
INF=1e12
for _ in range(m):
    start,end,cost=map(int,input().split())
    graph[start].append((end,cost))
    graph[end].append((start, cost))



def dijkstra(start):
    distance=[INF]*(n+1)
    q=[]
    #cost,node
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if distance[i[0]] > cost:
                distance[i[0]]= cost
                heapq.heappush(q,(cost,i[0]))
    return distance

u,v=map(int,input().split())
original_dijkstra=dijkstra(1)
u_dijkstra=dijkstra(u)
v_dijkstra=dijkstra(v)
result1=original_dijkstra[u]+u_dijkstra[v]+v_dijkstra[n]
result2=original_dijkstra[v]+v_dijkstra[u]+u_dijkstra[n]
fin_result=(min(result1,result2))
if fin_result>=1e10:
    print(-1)
else:
    print(fin_result)
