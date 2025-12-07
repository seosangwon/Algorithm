# 1:1로 쌍을 이루었을 때, 최대 쌍의 개수 
# 시간제한 4초 
# C,N이 최대 1e5이므로 최소 ClongN
# 1. 2중 탐색 - O(N^2) X , 2.    
# 1.빨간공을 오름차순으로 순차탐색 
# 2.조건에 충족하는 검은공을 heapq에 넣는다.
# 3. heapq에서 b의 값이 가장 낮은 값을 꺼낸다. 



import heapq

C,N=map(int,input().split(" "))
red_q=[]
black_q=[]

for _ in range(C):
    red=int(input())
    red_q.append(red)


for _ in range(N):
    a,b=map(int,input().split(" "))
    heapq.heappush(black_q,(a,b))

red_q.sort()
answer=0
hq=[]

# sol
for red in red_q:
    
    # 조건에 충족하는 검정돌을 heapq에서 꺼내 heapq에 넣는다.

    while black_q and black_q[0][0] <= red:
        a, b = heapq.heappop(black_q)
        if red <= b:
            heapq.heappush(hq, (b, a))  # b가 작은 구간이 우선

    # while black_q:
    #     a=black_q[0][0]
    #     b=black_q[0][1]

    #     if a<=red<=b:
    #         heapq.heappush(hq,(b,a))
    #         heapq.heappop(black_q)
        
    #     if red < a:
    #         break 
    
    # heapq에서 가장 b 값이 낮은 원소를 꺼낸다. 
    while hq and hq[0][0] < red:
        heapq.heappop(hq)
    
    if hq:
        answer+=1
        heapq.heappop(hq)


    
            

print(answer)

    








    

    









    

