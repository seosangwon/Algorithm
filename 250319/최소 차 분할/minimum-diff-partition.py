N=int(input())
arr=[0]+list(map(int,input().split(" ")))
M=sum(arr)

dp=[[False]*(M+1) for _ in range(N+1)]
dp[0][0]=True

for i in range(1,N+1):
    for j in range(M+1):
        if j>=arr[i] and dp[i-1][j-arr[i]]: # 값을 추가하는 경우 
            dp[i][j]=True
        else: # 값을 추가하지 않는 경우 
            dp[i][j]=dp[i-1][j]

answer=int(1e9)

for j in range(1,M+1):
    if dp[N][j]:
        #print(j,end=" ")
        answer=min(answer , abs((M-j)-j))

print(answer)

