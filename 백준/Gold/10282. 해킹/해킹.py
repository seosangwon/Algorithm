import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) # dis , node
    distance[start]=0
    while q:
        dis,now = heapq.heappop(q)
        if distance[now] < dis:
            continue

        for next,value in graph[now]:
            cost = distance[now] + value
            if distance[next] > cost:
                distance[next]=cost
                heapq.heappush(q,(cost,next))








t=int(input())
INF=int(1e9)
for _ in range(t):
    n,m,start=map(int,input().split())
    distance=[INF for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        e,s,c = map(int,input().split())
        graph[s].append((e,c))

    dijkstra(start)

    count,result=1,0
    for i in range(1,n+1):
        if i == start:
            continue
        if distance[i] != INF:
            count+=1
            if distance[i] > result:
                result=distance[i]

    print(count,result)



