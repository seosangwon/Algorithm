#n=2부터 가로 블록을 놓을 수 있다.  
#dp[2]=2
#dp[3]=3
#dp[4]=5
#dp[5]=

n=int(input())

dp=[0 for _ in range(n+1)]
dp[0]=1
dp[1]=1

if n==1:
    print(1)
else:
    for i in range(2,n+1):
        dp[i]=(dp[i-1]+dp[i-2]) %10007

    print(dp[n])