import sys 
N = int(input())
profit = [0] + list(map(int, input().split()))

INT_MIN=-sys.maxsize
dp=[[INT_MIN] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    dp[1][i]=profit[1]*i

for i in range(2,N+1):
    for j in range(N+1):
        if j>=i:
            dp[i][j]=max(dp[i-1][j] , dp[i][j-i]+profit[i])
        else:
            dp[i][j]=dp[i-1][j]


# for i in range(N+1):
#     for j in range(N+1):
#         print(dp[i][j],end=' ')
#     print()


print(dp[N][N])