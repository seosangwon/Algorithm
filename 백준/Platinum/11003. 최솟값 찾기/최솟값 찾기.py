import heapq

N,L=map(int,input().split())
arr=list(map(int,input().split()))

q=[]
for i in range(N):
    left=i-L+1
    while q and q[0][1]<left:
        heapq.heappop(q)

    heapq.heappush(q,(arr[i],i)) # 값 , idx
    print(q[0][0],end=' ')


