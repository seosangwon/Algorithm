# 1. 현재 종료시간을 알아야 함 
# 2. 대기 큐에 입장 가능한 사람들을 우선순위로 정렬 
# 3. 입장 가능하면은 입장 
# 4. 종료시간 갱신 
# 5. 최고 오래 기다린 시간 갱신 
# 6. 대기 큐에 더 이상 사람이 없으면 실행 종료 

# trouble : 입장 시각이 cur_time 보다 늦는경우 

import heapq
from collections import deque
N=int(input())
a=[]
t=[]
for i in range(N):
    s,e=map(int,input().split())
    a.append([s,i]) # [입장 시각 , idx]
    t.append(e) # 소요시간 저장 

a=deque(sorted(a))
s_q=[] # 대기 큐 
f_start,f_idx=a.popleft()
heapq.heappush(s_q,[f_idx , f_start]) # 첫번째 사람 대기열에 넣기 


cur_time=f_start
answer=0

#debug=[]

while s_q: # 대기 큐에 더이상 대기자가 없으면 종료 
    cur_idx , cur_start = heapq.heappop(s_q)
    answer=max(answer , (cur_time-cur_start))
    debug.append((cur_idx,cur_time - cur_start))
    cur_time+=t[cur_idx] # 소요 시간 더해주기 

    del_count=0
    if a: # 아직 입장 안한 사람들이 있다면은 
        for a_time , idx in a:  #[입장시각 , idx]
            if a_time <= cur_time: # 입장 가능하면은 
                heapq.heappush(s_q,[idx,a_time])
                del_count+=1
            else:
                break
    
    for _ in range(del_count):
        a.popleft()
    
    if a and not s_q : # trouble
        a_time , idx = a.popleft()
        cur_time=a_time 
        heapq.heappush(s_q,[idx,a_time])
    
    

print(answer)

#print(debug)





    
    








