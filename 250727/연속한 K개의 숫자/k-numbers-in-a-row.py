N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]

prefix_sum=[0] *(N+1)

for x in missing:
    prefix_sum[x]=1


for i in range(1,N+1):
    prefix_sum[i]+=prefix_sum[i-1]

answer=int(1e9)


for i in range(1,N-K+1):
    answer=min(answer, prefix_sum[i+K]-prefix_sum[i])

print(answer)







    
    
        
        
    
        
    


