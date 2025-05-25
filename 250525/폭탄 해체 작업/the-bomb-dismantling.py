#각 폭탄은 1시간의 해체시간이 걸린다
# N의 최대 개수는 10,000
# 점수 _ 시간제한
# 시간제한이 넘으면 폭탄은 터진다 

#힙큐사용 (제한시간 , - 점수)

import heapq

N=int(input())
hq=[]

for _ in range(N):
    p,t=map(int,input().split(" "))
    heapq.heappush(hq,(t,-p))


c_time=0
answer=0

while hq:
    bomb_t,bomb_p=heapq.heappop(hq)
    
    if c_time >= bomb_t:
        continue 
    
    #폭탄헤제 
    c_time+=1
    answer+=bomb_p

print(-answer)



