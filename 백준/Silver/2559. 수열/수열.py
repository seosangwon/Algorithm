N,M=map(int,input().split())
data=list(map(int,input().split()))
dp=[0 for _ in range(N-M+1)]

for i in range(M):
    dp[0]+=data[i]

for i in range(1,N-M+1):
    dp[i]=dp[i-1]+data[i+M-1]-data[i-1]

print(max(dp))

