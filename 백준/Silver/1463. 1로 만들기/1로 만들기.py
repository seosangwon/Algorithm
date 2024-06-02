N=int(input())
INF=int(1e9)
dp=[0 for _ in range(N+1)]
dp[1]=0

for i in range(2,N+1):
    if i %3==0 and i%2!=0:
        dp[i]=min(dp[i//3]+1, dp[i-1]+1)

    if i%2==0 and i%3!=0:
        dp[i]=min(dp[i//2]+1,dp[i-1]+1)

    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i//3]+1 ,dp[i // 2] + 1, dp[i - 1] + 1)

    if i%3 !=0 and i%2!=0:
        dp[i]=dp[i-1]+1


print(dp[-1])

