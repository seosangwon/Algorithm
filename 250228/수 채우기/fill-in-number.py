import sys
n = int(input())

# Please write your code here.
INT_MAX=sys.maxsize
dp=[INT_MAX]*(n+1)
coins=[2,5]
dp[0]=0

for i in range(n+1):
    for j in range(len(coins)):
        if i>=coins[j]: 
            if dp[i-coins[j]]!=INT_MAX:
                dp[i]=min(dp[i],dp[i-coins[j]]+1)


if dp[n] == INT_MAX:
    print(-1)
else:
    print(dp[n])

