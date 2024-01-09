import heapq
n,x=map(int,input().split())
result=0
max_diff=[]

num_A=(x-1000*n) // 4000


for _ in range(n):
    a,b=map(int,input().split())
    result+=b
    diff=a-b
    if diff > 0 :
        heapq.heappush(max_diff,(-diff,diff))

for _ in range(num_A):
    if max_diff:
        value=heapq.heappop(max_diff)
        result+=value[1]
        

print(result)


