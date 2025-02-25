# 1,2,5의 합으로 나타내는 방법의 수 
N=int(input())
dp=[0]*(10001)
dp[0]=1
numbers=[1,2,5]


for i in range(1,N+1):
    for j in range(3):
        if i>=numbers[j]:
            dp[i]=(dp[i]+dp[i-numbers[j]])%10007

print(dp[N])

        
