import sys
n=int(input())
data=list(map(int,input().split()))
MIN_INF=-int(1e9)
dp=[MIN_INF] * n 
dp[0]=1

for i in range(1,n):#dp[i]는 점프 될 곳 
    for j in range(0,i): # dp[j]에서 점프해서 dp[i]로 가자
        if dp[j]==MIN_INF:
            continue
        
        if data[j]<data[i]:
            dp[i]=max(dp[i],dp[j]+1) # dp[j]를 거치는 경우, 안거치는 경우 

print(max(dp))