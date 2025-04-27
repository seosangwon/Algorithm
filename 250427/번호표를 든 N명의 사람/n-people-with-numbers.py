import heapq 
# T_max를 넘지 않는 선에서 K의 최솟값을 구해라
N, T_max = map(int, input().split())
d = [int(input()) for _ in range(N)]

left=0
right=10000
answer=int(1e9)

def is_possible(k): # 최대 k명이 무대위에 올라 갈 수 있고 , T_max 시간이 지나서는 안된다 
    q=d[:k]
    heapq.heapify(q)
        
    
    for i in range(k,N): # 끝 순서 까지 시간 계산 
        cur_time=heapq.heappop(q)
        heapq.heappush(q,cur_time+d[i])
    
    
    while q:
        end_time=heapq.heappop(q)

        if end_time > T_max:
            return False 
    
    return True 
    


while left<=right:
    mid=(left+right)//2


    if is_possible(mid): # 가능하다면은 k를 줄인다
        answer=min(answer,mid)
        right=mid-1
        
    
    else: # 불가능하다면은 k를 늘린다 
        left=mid+1
        


print(answer)


