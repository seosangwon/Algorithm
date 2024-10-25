#(1,1)에서 출발 
# 점점 증가 해야함 
# 적어도 오른쪽으로 한칸 , 아래로 한칸은 이동 되어 있어야 함 
n,m=map(int,input().split())
MIN_INF=-int(1e9)
data=[[0]*(m+1)]

for _ in range(n):
    data.append([0]+list(map(int,input().split())))


dp=[[MIN_INF]*(m+1) for _ in range(n+1)]

dp[1][1]=1



for i in range(2,n+1):
    for j in range(2,m+1): # dp[i][j]는 현재 좌표 
        for k in range(1,i):
            for p in range(1,j): # dp[k][p]는 이전 좌표 
                if k<i and p<j: # 무조건 위로 한칸 , 왼쪽으로 한칸 이상이어야 함 
                    if dp[k][p]==MIN_INF:
                        continue
                    
                    if data[k][p] < data[i][j]:
                        dp[i][j]=max(dp[i][j],dp[k][p]+1)

answer=1
for i in range(1,n+1):
    for j in range(1,m+1):
        answer=max(answer, dp[i][j])

print(answer)



# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(dp[i][j],end=' ')
#     print()