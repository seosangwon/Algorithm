# A가 물건을 훔쳤을 경우
# B가 물건을 훔쳤을 경우 

def solution(info, n, m):
    answer = 0
    INF=int(1e9)
    length=len(info)
    dp=[[INF]*m for _ in range(length+1)]
    dp[0][0]=0
    
    for i in range(length):
        A_cost=info[i][0]
        B_cost=info[i][1]
        for j in range(m):
            if dp[i][j]==INF:
                continue 
            
            # A가 훔치는 경우 
            new_cost_A=A_cost+dp[i][j]
            if dp[i+1][j] > new_cost_A:
                dp[i+1][j]=new_cost_A
            
            # B가 훔치는 경우 
            new_cost_B=B_cost + j
            
            if new_cost_B < m:
                if dp[i+1][new_cost_B] > dp[i][j]:
                    dp[i+1][new_cost_B]=dp[i][j]
                    
    # for i in range(length+1):
    #     for j in range(m):
    #         print(dp[i][j],end=' ')
    #     print()
    
    answer=min(dp[length])
    
    if answer>=n:
        return -1

    
    return answer