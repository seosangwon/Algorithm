n,k=map(int,input().split())
data=[]
dp=[0 for i in range(k+1)]


for _ in range(n):
    data.append(int(input()))

data.sort()


dp[0]=1

for i in data:
    for j in range(i,k+1):
        dp[j]+=dp[j-i]

print(dp[-1])

