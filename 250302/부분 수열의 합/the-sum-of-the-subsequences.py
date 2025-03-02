N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))

# 부분 수열의 합으로 m을 만들 수 있는지 없는지 확인 
# N은 최대 100개 
# 포함하냐 마냐 , 2의 거든제곱 


dp=[[False] * (M+1)for _ in range(N+1)]
dp[0][0]=True

for i in range(1,N+1):
    for j in range(M+1):
        if j >= A[i] and dp[i-1][j-A[i]]==True:
            dp[i][j]=True
        
        if dp[i-1][j]==True:
            dp[i][j]=True 

if dp[N][M]:
    print("Yes")
else:
    print("No")

    


