n=int(input())
data=[]
dp=[[0 for _ in range (3)]  for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

for i in range(1,n):
    data[i][0]=min(data[i-1][1],data[i-1][2])+data[i][0]
    data[i][1]=min(data[i-1][0],data[i-1][2])+data[i][1]
    data[i][2]=min(data[i-1][0],data[i-1][1])+data[i][2]

# print(min(dp[n]))
print(min(data[n-1]))

