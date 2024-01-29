n,m=map(int,input().split())

dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
data=[]

for i in range(1,n+1):
    w,v=map(int,input().split())
    for j in range(1,m+1):
        if j>=w:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][m])