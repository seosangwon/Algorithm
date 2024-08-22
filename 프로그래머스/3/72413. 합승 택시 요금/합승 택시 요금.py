def solution(n, s, a, b, fares):
    answer = 0
    INF=int(1e9)
    dp=[[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                dp[i][j]=0
    
    for start,end,cost in fares:
        dp[start][end]=cost
        dp[end][start]=cost
    

    
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i][k]==INF or dp[k][j]==INF:
                    continue
                dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j])
        
    result=dp[s][a]+dp[s][b] # 경유하지 않고 직선거리 값들 
        
    for k in range(1,n+1):
        result=min(result,dp[s][k]+dp[k][b]+dp[k][a])

    answer=result

    
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print(dp[i][j],end=' ')
#         print()
        
        
    
    
    
    return answer