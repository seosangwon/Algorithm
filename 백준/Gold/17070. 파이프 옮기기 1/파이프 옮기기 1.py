#N의 최대 크기는 16
#가로 -> 가로 , 대각
#세로 -> 세로 , 대각
#대각 -> 가로 , 세로 , 대각
N=int(input())
data=[]
shape=1 #가로 1, 세로 2 , 대각 3
x,y=0,1
for _ in range(N):
    data.append(list(map(int,input().split())))

dp=[[[0] * 3 for _ in range(N)] for _ in range(N)]

#0,1,2 가로,세로,대각선

dp[0][1][0]=1
for i in range(2,N):
    if data[0][i]==0:
        dp[0][i][0]=1
    else:
        break

for i in range(1,N):
    for j in range(2,N):
        if data[i][j]==0 and data[i-1][j]==0 and data[i][j-1]==0: # 대각
            dp[i][j][2]=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]

        if data[i][j]==0:
            dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][2]
            dp[i][j][1]=dp[i-1][j][1]+dp[i-1][j][2]

result=sum(dp[N-1][N-1])
print(result)
















