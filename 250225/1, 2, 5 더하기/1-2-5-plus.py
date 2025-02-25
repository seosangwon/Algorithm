# 1,2,5의 합으로 나타내는 방법의 수 
N=int(input())
dp=[0]*(10001)
dp[1]=1
dp[2]=2
dp[3]=3
dp[4]=5
dp[5]=9

if N>5:
    for i in range(6,N+1):
        dp[i]=max(dp[i],(dp[i-1]+dp[i-2]+dp[i-5])%10007)

print(dp[N])
        
