import sys
INT_MIN=-sys.maxsize
N, M = map(int, input().split())
j=[(0,0)]
weight=[0]*(M+1)
value=[0]*(M+1)

for i in range(1,N+1):
    w,v=map(int,input().split())
    weight[i]=w 
    value[i]=v


#보석을 넣냐 마느냐 
dp=[[INT_MIN] * (M+1) for _ in range(N+1)]
dp[0][0]=0


for i in range(1,N+1):
    for j in range(M+1):
        if j>=weight[i]: # 보석을 넣는경우 
            dp[i][j]=max(dp[i-1][j-weight[i]]+value[i] , dp[i-1][j])
        
        else: # 보석을 못넣는 경우 
            dp[i][j]=dp[i-1][j]



print(max(dp[N]))




