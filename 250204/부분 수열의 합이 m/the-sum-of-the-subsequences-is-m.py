n, m = map(int, input().split())
A = list(map(int, input().split()))
INF=int(1e9)
dp=[INF]*(m+1)
dp[0]=0

try:
    for i in range(n): # 코인은 순차적으로 
        for j in range(m,-1,-1): # 목표 값에서 부터 -1씩 감소
            if j<A[i] or dp[j-A[i]]==INF: # 지금 코인으로 만들 수 없는 값이라면은 pass
                continue
            
            dp[j]=min(dp[j],dp[j-A[i]]+1)
except:
    print(i,j,A[i])


print(dp[-1])
        

            
        



