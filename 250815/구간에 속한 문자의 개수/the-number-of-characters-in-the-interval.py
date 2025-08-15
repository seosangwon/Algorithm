N,M,K=map(int,input().split())

data=[]

for _ in range(N):
    li=list(input())
    data.append(li)


dp=[[[0,0,0] for _ in range(M+1)] for _ in range(N+1)]
value=[[[0,0,0] for _ in range(M+1)] for _ in range(N+1)]

#dp에 초기 값 채워주기

for i in range(N):
    for j in range(M):
        if data[i][j]=='a':
            value[i+1][j+1][0]=1
        if data[i][j]=='b':
            value[i+1][j+1][1]=1
        if data[i][j]=='c':
            value[i+1][j+1][2]=1





def calculate(x1,y1,x2,y2):
    a = dp[x2][y2][0]-dp[x1-1][y2][0]-dp[x2][y1-1][0]+dp[x1-1][y1-1][0]
    b = dp[x2][y2][1]-dp[x1-1][y2][1]-dp[x2][y1-1][1]+dp[x1-1][y1-1][1]
    c = dp[x2][y2][2]-dp[x1-1][y2][2]-dp[x2][y1-1][2]+dp[x1-1][y1-1][2]

    return a,b,c

# memoization
for i in range(1,N+1):
    for j in range(1,M+1):
        for k in range(3):
            dp[i][j][k]=dp[i-1][j][k]+dp[i][j-1][k]-dp[i-1][j-1][k]+value[i][j][k]
            


# # 누적합 점검 
# for i in range(N+1):
#     for j in range(M+1):
#         print(dp[i][j],end=' ')
#     print()


# main
for _ in range(K):
    li=list(map(int,input().split()))
    x1,y1,x2,y2=li[0],li[1],li[2],li[3]
    result = calculate(x1,y1,x2,y2)
    for r in result:
        print(r,end=' ')
    print()













