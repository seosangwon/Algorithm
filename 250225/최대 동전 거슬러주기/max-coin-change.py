import sys
INT_MIN=-sys.maxsize
N, M = map(int, input().split())
coin = list(map(int, input().split()))


# 최대 동저의 개수로 거스름돈 거슬러주기 

dp=[INT_MIN]*(M+1)
dp[0]=0


for i in range(1,M+1):
    for j in range(N):
        if i>=coin[j]:
            if dp[i-coin[j]]==INT_MIN:
                continue
            
            dp[i]=max(dp[i],dp[i-coin[j]]+1)


if dp[M]==INT_MIN:
    print(-1)
else:
    print(dp[M])