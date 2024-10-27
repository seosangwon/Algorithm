#겹치지 않게 가장 많은 수의 선분을 골라라 
#n은 최대 1000개
#각 좌표 : dp[i]는 안겹치는 최대 직선의 개수 값을 저장 
n=int(input())
MIN_INF=-int(1e9)
data=[]
for _ in range(n):
    x1,x2=map(int,input().split())
    data.append([x1,x2])

data.sort(key=lambda x: [x[0]]) # x1 오름차순으로 정렬 
dp=[0]*(1001)

for i in range(n): # 0,1,2,3,4...n번째 선분 
    dp[i]=1

    for j in range(i): # 처음부터 ~ n-1번 선분까지 순회
        x1_i,_=data[i] # target 선
        _,x2_j=data[j] # target 전 까지의 선들 
        if x2_j<x1_i:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))