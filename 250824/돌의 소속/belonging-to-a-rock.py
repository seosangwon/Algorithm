# N,Q는 최대 10만 


N,Q=map(int,input().split())
data=[0]

for i in range(N):
    data.append(int(input()))


dp=[[0,0,0] for _ in range(N+1)]

#prefix
for i in range(1,N+1):
    if data[i]==1:
        dp[i][0]=dp[i-1][0]+1
        dp[i][1]=dp[i-1][1]
        dp[i][2]=dp[i-1][2]
    if data[i]==2:
        dp[i][0]=dp[i-1][0]
        dp[i][1]=dp[i-1][1]+1
        dp[i][2]=dp[i-1][2]
    if data[i]==3:
        dp[i][0]=dp[i-1][0]
        dp[i][1]=dp[i-1][1]
        dp[i][2]=dp[i-1][2]+1
        


for _ in range(Q):
    a,b=map(int,input().split())
    for k in range(3):
        print(dp[b][k]-dp[a-1][k],end=' ')
    print()


