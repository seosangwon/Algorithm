# 최솟값 중 최대를 출력해라 
n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

dp=[[0]* n for _ in range(n)]
dp[0][0]=data[0][0]

for i in range(1,n):
    dp[0][i]=min(dp[0][i-1],data[0][i])
    dp[i][0]=min(dp[i-1][0],data[i][0])




for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=min(max(dp[i-1][j],dp[i][j-1]),data[i][j])

print(dp[-1][-1])