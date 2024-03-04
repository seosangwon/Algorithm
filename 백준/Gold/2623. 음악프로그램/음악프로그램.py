from collections import deque
#가수의 정보 , 보조pd의 수
n,m=map(int,input().split())
in_degree=[0 for _ in range(n+1)]
data=[]
graph=[[] for _ in range(n+1)]

for _ in range(m):
    data.append(list(map(int,input().split())))

for li in data:
    for i in range(2,li[0]+1):
        in_degree[li[i]]+=1
    for i in range(1,li[0]):
        graph[li[i]].append(li[i+1])




result=[]
def topology_sort():
    q=deque([])
    for i in range(1,n+1):
        if in_degree[i]==0:
            q.append(i)

    while q:
        node=q.popleft()
        result.append(node)
        for i in graph[node]:
            in_degree[i]-=1
            if in_degree[i]==0:
                q.append(i)





topology_sort()

if len(result) == n :
    for i in range(n):
        print(result[i])
else:
    print(0)

