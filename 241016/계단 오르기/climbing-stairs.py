# 2계단 혹은 3계단으로만 올라갈 수 있다.
# n층 까지 올라가는 경우의 수를 출력해라

n=int(input())
dp=[0 for _ in range(n+1)]
dp[2]=1

if n==2:
    print(1)

else:
    dp[3]=1
    for i in range(4,n+1):
        dp[i]=(dp[i-2]+dp[i-3])
        

    print(dp[n])