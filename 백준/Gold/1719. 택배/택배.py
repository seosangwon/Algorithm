n,m=map(int,input().split())
INF=int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    i,j,cost=map(int,input().split())
    graph[i][j]=cost
    graph[j][i]=cost

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

result = [[i for i in range(n+1)] for _ in range(n+1)]



for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]
                result[i][j]=result[i][k]



for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('-',end=' ')
        else:
            print(result[i][j],end=' ')
    print()


