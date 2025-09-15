# 보석이 총 N개 가방이 K개
# N과 K의 최대 개수는 3e5
# N개의 줄에 무게 M과 가격 V가 주어진다.
# K개의 가방의 무게가 주어진다

# 조건만 통과하면 되는게 아니라 최적화를 해야 하는게 관건
# 단순하게 생각하면 담을 수 있는 무게가 낮은 가방 순을 정렬해서 순서대로 가장 value가 높은 보석을 가져간다
# O(N * logN )
# logN으로 현재 가방의 무게에 따라서 value가 제일 높은 보석을 가져갸아 함 ->  heapq
# 무게가 K(i) 이하이면서 value가 높은 순서대로 heapq에 정렬되어있어야 함
# 무게가 k 이하인 보석들 중 가장 좋은 보석 고르는 법: 무게순으로 보석들을 미리 정렬해놓은 뒤 -> 리스트를 잘라서 -> heapq로 변환 -> 제일 값 높은 보석 pop -> index -=1
# 관건은 현재 가방의 무게 이하의 보석들을 어떻게 찾아내냐.
# heapq를 2개 둔다. A는 (무게,보석idx) , B는(value,idx)
# 현재 가방의 무게 보다 낮은 가방들을 전부 B heapq에다가 넣는다.
# N 순차 탐색하면서 A에서 가장 value가 높은 보석을 꺼내간다.



import heapq

#입력
N,K=map(int,input().split())

j_list=[]
for _ in range(N):
    m,v=map(int,input().split())
    j_list.append((m,v))


bags=[]
for _ in range(K):
    x=int(input())
    bags.append(x)

#무게순 정렬
#j_list.sort(key=lambda x: x[0])
bags.sort()

# heapq_B에다가 (무게,idx) 순으로 저장
q_B=[]

for i in range(N):
    heapq.heappush(q_B,(j_list[i][0],i))



# N차 탐색 하기
q_A=[]
answer=0

for i in range(K):
    bag_kg=bags[i]
    while q_B:
        # print(f"최상단 : {q_B[0]}, 현 가방 무게: {bag_kg}  ")
        if q_B[0][0] <= bag_kg: # heapq의 최상단이 bag_kg보다 낮다면은 q_A에다 옮긴다.
            t=heapq.heappop(q_B)
            m=t[0]
            idx=t[1]
            # print(f"현 보석의 가치: {j_list[idx][1]} ")
            heapq.heappush(q_A,(-j_list[idx][1]))
        else:
            break


    if q_A:
        top_value=heapq.heappop(q_A)
        answer+=(top_value)*-1
        # print(top_value)


print(answer)


























