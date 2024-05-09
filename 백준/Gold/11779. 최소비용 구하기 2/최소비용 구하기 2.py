import heapq

N=int(input()) # 노드의 개수
M=int(input()) # 간선의 개수
INF=int(1e9)
distance=[INF for _ in range(N+1)]
graph=[ [] for _ in range(N+1)]

for _ in range(M):
    s,e,cost=map(int,input().split())
    graph[s].append((e,cost))
    #graph[e].append((s,cost)) # 간선은 단방향성 정보이다

start,end=map(int,input().split())


prev_node=[0 for _ in range(N+1)]

def dijkstra(start,end):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start)) # cost , node


    while q:
        cost,node=heapq.heappop(q)

        if distance[node] < cost: # 지금 node까지 오기 필요한 거리 값 cost가 distance 리스트에 저장되어 있는 값 보다 높다면은 필요가 없는 정보이므로 continue
            continue

        for next_node,c in graph[node]: # 간선 정보 하나씩 추출
            if cost+c < distance[next_node]: # 현재 node를 거치고 next_node로 가는 값이 현재 저장되어 있는 distance[next_node]값 보다 작다면 갱신
                distance[next_node]=(cost+c)
                heapq.heappush(q,(cost+c,next_node))
                prev_node[next_node]=node




    return


dijkstra(start,end)
path=[end]
now=end

while now!=start:
    now=prev_node[now]
    path.append(now)

path.reverse()
print(distance[end])
print(len(path))
print(' '.join(map(str,path)))
