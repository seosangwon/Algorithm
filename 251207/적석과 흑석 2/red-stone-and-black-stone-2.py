# 1:1로 쌍을 이루었을 때, 최대 쌍의 개수 
# 시간제한 4초 
# C,N이 최대 1e5이므로 최소 ClongN
# 1. 2중 탐색 - O(N^2) X , 2.    
# 빨간공 제일 값이 작은거 부터 처리한다.
# 1. 검은공 순차탐색 2. 조건에 충족한 빨간공이 있으면 +1 3. 조건에 충족한 빨간공이 없으면 빨간공 큐에서 제거 

import heapq

C,N=map(int,input().split(" "))
red_q=[]
black_q=[]

for _ in range(C):
    red=int(input())
    red_q.append(red)

for _ in range(N):
    a,b=map(int,input().split(" "))
    black_q.append((a,b))

black_q.sort(key=lambda x: (x[0],x[1]))
heapq.heapify(red_q)
answer=0

for a,b in black_q:

    while red_q:
        
        if red_q[0] > b: # red중에 제일 작은 값인데 b 보다 커버리면 이 후 원소들 모두 조건 불충족 
            break

        if red_q[0] < a :  # 조건 미충족시 원소 제거 후 다시 로직을 탄다.
            heapq.heappop(red_q)
            continue 
        
        if a<=red_q[0]<=b: # 조건 충족시 원소 제거 후 break
            answer+=1
            heapq.heappop(red_q)
            break
        

print(answer)
        
        







    

