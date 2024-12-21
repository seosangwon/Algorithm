#n=1 일 때 , 
n=int(input())
dp=[0 for _ in range(1001)]
dp[1]=2
dp[2]=7

if n==1:
    print(dp[1])
elif n==2:
    print(dp[2])
else:
    for i in range(3,n+1):
        dp[i]=(2*(dp[i-1]*dp[i-2])) % 1000000007
    
    print(dp[n])