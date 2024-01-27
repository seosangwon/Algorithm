n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))


dp=[[0 for _ in range(m)] for _ in range(n) ]
dp[0][0]=data[0][0]




for j in range(1,m):
    dp[0][j]=dp[0][j-1] +data[0][j]

for i in range(1,n):
    dp[i][0]=dp[i-1][0] +data[i][0]

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = max(dp[i][j - 1] + data[i][j], dp[i - 1][j - 1] + data[i][j], dp[i - 1][j] + data[i][j])

print(dp[n-1][m-1])

