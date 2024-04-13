a=list(input())
b=list(input())


dp=[[0 for _ in range(len(a))] for _ in range(len(b))]
answer=0
for i in range(len(b)):
    for j in range(len(a)):
        if a[j]==b[i] :
            if i==0 or j==0:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+1
        answer=max(answer,dp[i][j])

print(answer)