# +을 넣냐  , -을 넣냐
# 왼쪽부터 계산 중 나오는 수는 모두 0이상 20이하여야 한다
# N은 최대 100개
# 백트래킹 하기에는 시간 초과

N=int(input())
data=list(map(int,input().split()))

# 0 이상 20을 넘지 않는다
dp=[[0]*(21) for _ in range(N)]
dp[0][data[0]]=1

for i in range(1,N-1): # 순서
    for j in range(21): # 경우의 수 dp
        if j-data[i]>=0:
            dp[i][j-data[i]]+=dp[i-1][j]
        if j+data[i]<=20:
            dp[i][j+data[i]]+=dp[i-1][j]

print(dp[-2][data[-1]])







