# 동일한 보석 여러개 가지는 것이 가능하다
N,M=map(int,input().split())
w,v=[],[]

for _ in range(N):
    weight,value=map(int,input().split())
    w.append(weight)
    v.append(value)


dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(1,M+1):
        if j >= w[i] : # 보석을 담을 수 있다면은 
            dp[i][j]=max(dp[i-1][j] , dp[i-1][j-w[i]]+v[i] , dp[i][j-w[i]]+v[i])
        else:
            dp[i][j]=dp[i-1][j]
        
        

# for i in range(N+1):
#     for j in range(M+1):
#         print(dp[i][j],end=' ')
#     print()

print(max(dp[N-1]))