import heapq
N,K=map(int,input().split())
data=list(map(int,input().split()))

idx=0
result=[]
while True:
    if idx + K > N:
        break

    temp=data[idx:idx+K]
    q=[]
    for i in range(len(temp)):
       heapq.heappush(q,(temp[i],-i)) #(값, -인덱스)

    value,index=heapq.heappop(q)
    index*=-1
    result.append(value)
    idx=idx+index+1

#print(result)
print(max(result))
