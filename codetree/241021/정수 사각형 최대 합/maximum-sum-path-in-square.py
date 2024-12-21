n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=data[0][0]
for i in range(1,n):
    dp[0][i]=data[0][i] + dp[0][i-1]
    dp[i][0]=data[i][0] + dp[i-1][0]



# for i in range(n):
#     for j in range(n):
#         print(dp[i][j],end=' ')
#     print()

for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=max(dp[i-1][j]+data[i][j],dp[i][j-1]+data[i][j])

print(dp[n-1][n-1])