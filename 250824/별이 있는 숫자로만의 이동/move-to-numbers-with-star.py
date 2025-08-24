# N X N : N의 최대는 400
# K의 최대는 800
# 완전탐색 : 160000 X 160000 => 시간초과
# memoization이 필요 
# prefix sum을 구한 다음에 수식으로 계산한다. 


N,k=map(int,input().split())

data=[[0] *(N+1)]

for _ in range(N):
    li=list(map(int,input().split()))
    append_li=[0]+li
    data.append(append_li)
    


# for i in range(N+1):
#     for j in range(N+1):
#         print(data[i][j],end=' ')
#     print()
    
    
#prefix_sum

prefix_sum=[[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        prefix_sum[i][j]=prefix_sum[i][j-1]+data[i][j]


answer=0

for i in range(1,N+1):
    for j in range(1,N+1):
        sum_all=0
        for r in range(i-k,i+k+1):
            c=k-abs(i-r)
        
            if 1<=r and r<=N:
                sum_all+=prefix_sum[r][min(j+c,N)] - prefix_sum[r][max(j-c-1,0)]
        answer=max(answer,sum_all)


print(answer)
            
