# 1:1로 쌍을 이루었을 때, 최대 쌍의 개수 
# 시간제한 4초 
# C,N이 최대 1e5이므로 최소 ClongN
# 1. 2중 탐색 - O(N^2) X , 2.    
# 빨간공 제일 값이 큰 애 부터 검은공  A,B에 끼워 넣는다. 
# 1. 검은공 순차탐색 2. 조건에 충족한 빨간공이 있으면 +1 3. 조건에 충족한 빨간공이 없으면 빨간공 큐에서 제거 

import heapq

C,N=map(int,input().split(" "))
red_q=[]
black_q=[]

for _ in range(C):
    red=int(input())
    red_q.append(red*-1)

for _ in range(N):
    a,b=map(int,input().split(" "))
    black_q.append((a,b))

black_q.sort(key=lambda x: -x[0])

answer=0
heapq.heapify(red_q)

# business logic 
for a,b in black_q:
    
    # red_q를 순차탐색 
    while red_q:
        red=red_q[0]*-1

        # 조건을 충족한다면 
        if a<=red<=b:
            answer+=1
            heapq.heappop(red_q)
            break 
        
        #조건 미충족시 
        else:
            heapq.heappop(red_q)


print(answer)









    

