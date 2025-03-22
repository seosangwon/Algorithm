# 각 물건에 대해 A도둑과 B 도둑이 남기는 흔적의 개수는 1 이상 3 이하이다 
# A 도둑이 남긴 흔적의 누적 개수가 최솟값을 return
# 만약 두 도둑 모두 경찰에 붙잡히지 않게 할 수 없다면 -1을 return 
def solution(info, n, m):
    length=len(info)
    INF=int(1e9)
    dp=[[INF]*(m) for _ in range(length+1)]
    dp[0][0]=0
    
    for i in range(length):
        a_cost=info[i][0]   
        b_cost=info[i][1]
        for j in range(m):
            if dp[i][j]==INF:
                continue 
            
            # A가 훔치는 경우 
            new_a=dp[i][j]+a_cost 
            
            if new_a < dp[i+1][j]:
                dp[i+1][j]=new_a
            
            #B가 훔치는 경우 
            new_b=j+b_cost 
            if new_b<m:
                if dp[i][j] < dp[i+1][new_b]:
                    dp[i+1][new_b]=dp[i][j]
    
    answer=min(dp[length])
    
    return answer if answer<n else -1