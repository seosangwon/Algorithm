#금액 M을 맞추는 최소 동전의 개수를 출력해라
#i는 금액 
#dp[i]는 금액i를 거슬러 줄 수 있는 최소 동전의 수 
n,m=map(int,input().split())
coins=list(map(int,input().split()))
coins.sort()
INF=int(1e9)
dp=[INF]*(m+1)

for coin in coins:
    if coin <= m:
        dp[coin]=1


for i in range(1,m+1): # 현재 금액 
    for j in range(n):   
        if i>coins[j]:
            dp[i]=min(dp[i],dp[i-coins[j]]+1)


if dp[-1]==INF:
    print(-1)
else:
    print(dp[-1])