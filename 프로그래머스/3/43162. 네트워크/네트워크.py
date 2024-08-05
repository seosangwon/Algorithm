def solution(n, computers):
    answer = 0
    visited=[False for _ in range(n)]
    edge=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]==1:
                edge[i].append(j)
    
    
                
    
    def dfs(n):
        visited[n]=True
        
        for next in edge[n]:
            if visited[next]==False:
                dfs(next)
        
        return
    
    
    for node in range(n):
        if visited[node]==False:
            dfs(node)
            answer+=1
            

    
    return answer