n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

dp=[[0 for _ in range(n)] for _ in range(n)]

dp[0][n-1]=data[0][n-1]

for i in range(n-2,-1,-1):
    dp[0][i]=dp[0][i+1]+data[0][i]

for i in range(1,n):
    dp[i][n-1]=dp[i-1][n-1]+data[i][n-1]



for i in range(1,n):
    for j in range(n-2,-1,-1):
        dp[i][j]=min((dp[i-1][j]+data[i][j]) , dp[i][j+1]+data[i][j])

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j],end=' ')
#     print()

print(dp[n-1][0])