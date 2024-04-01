N,M=map(int,input().split())
data=[0]+list(map(int,input().split()))
sum_li=[0 for _ in range(N+1)]

for i in range(1,N+1):
    sum_li[i]=sum_li[i-1]+data[i]


for _ in range(M):
    i,j=map(int,input().split())
    print(sum_li[j]-sum_li[i-1])

