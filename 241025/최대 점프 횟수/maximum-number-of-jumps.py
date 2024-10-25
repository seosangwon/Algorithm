n=int(input())
data=list(map(int,input().split()))

MIN_INF=-int(1e9)
dp=[MIN_INF] * n 
dp[0]=0

for i in range(1,n):
    for j in range(i):
        if dp[j]==MIN_INF:
            continue
        
        if i <= j+data[j]:
            dp[i]=max(dp[i],dp[j]+1)


print(max(dp))