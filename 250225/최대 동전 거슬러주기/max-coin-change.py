N, M = map(int, input().split())
coin = list(map(int, input().split()))


# 최대 동저의 개수로 거스름돈 거슬러주기 

dp=[0]*(M+1)

for c in coin: # 각 동전 초기화 
    dp[c]=1

coin_max=max(coin)

for i in range(coin_max+1,M+1):
    for j in range(N):
        
        dp[i]=max(dp[i],(dp[i-coin[j]]+1))

if dp[M]==0:
    print(-1)
else:
    print(dp[M])