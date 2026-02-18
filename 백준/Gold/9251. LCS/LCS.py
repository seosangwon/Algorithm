#Longes Common Subsequence
#n은 최대 1000

# 무슨 문자열이 공통 문자열인지를 모름
# 문자의 순서를 기억해야 함

# dp[i][j]의 값은 지금까지의 solution 값
# answer = dp[n][n]
# dp[i][j]=


s1=list(input())
s2=list(input())
n=len(s1)
m=len(s2)

dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]: # 서로 문자열이  같으면 +1
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]= max(dp[i-1][j],dp[i][j-1])


print(dp[n][m])







