n=int(input())
data=list(map(int,input().split()))

dp=[[0,0] for _ in range(n)] # [증가 ,감소]
dp[0][0]=1
dp[0][1]=1
for i in range(1,n):
    dp[i][0]=1 # 이곳이 출발점이 될 수 있으니 매번 갱신 
    dp[i][1]=1
    for j in range(i):
        # 매번 증가
        if data[j]<data[i] :
            dp[i][0]=max(dp[i][0],dp[j][0]+1)
        
        #매번 감소 
        if data[j] > data[i] : 
            dp[i][1]=max(dp[i][1],dp[j][1]+1)
        
        dp[i][1]=max(dp[i][0],dp[i][1])

answer=0
for i in range(n):
    for j in range(2):
        answer=max(answer,dp[i][j])

print(answer)