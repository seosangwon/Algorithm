# A도둑의 흔적을 가장 적게 만들어 return
# A도둑이 훔치느냐 B도둑이 훔치느냐 : 최대 물건의 개수는 40개이므로 완탐시 2**40으로 시간초과
# memoization이 필요함 -> dp
# A와 훔쳤을 경우와 B 훔쳤을 경우를 나눈다
# 행은 idx, 열은 m
def solution(info, n, m):

    INF=int(1e9)
    len_=len(info)
    dp=[[INF]*m for _ in range(len_+1)]
    dp[0][0]=0
    for i in range(len_):
        a=info[i][0]
        b=info[i][1]
        for j in range(m):
            if dp[i][j]==INF: # 도달하지 않은 값이면 경우의 수가 없는 것, 패스한다
                continue
            
            #A가 가져갔을 경우
            if dp[i][j]+a<n: # n보다 작아야함 
                dp[i+1][j]=min(dp[i][j]+a,dp[i+1][j])
            
            #B가 가져갔을 경우
            if j+b<m:
                dp[i+1][j+b]=min(dp[i][j],dp[i+1][j+b])
    
    
    for i in range(len_+1):
        for j in range(m):
            print(dp[i][j],end=' ')
        print()
    
    
    answer = min(dp[len_]) 
    
    
    if answer==INF:
        answer=-1
    
                
    
    return answer