def solution(triangle):
    answer = 0
    N=len(triangle)
    dp=[[0 for _ in range(N)] for _ in range(N)]
    dp[0][0]=triangle[0][0]
    #옆에 사이드는 미리 다 더하기 
    for i in range(1,N):
        dp[i][0]=dp[i-1][0]+triangle[i][0]
        dp[i][i]=dp[i-1][i-1]+triangle[i][i]
    
    for i in range(2,N):
        for j in range(1,i):
            dp[i][j]=max(dp[i-1][j-1]+triangle[i][j] , dp[i-1][j]+triangle[i][j])
    
    answer = max(dp[-1])
    
    
    
            
    
    
    
    return answer