import heapq
N, M = map(int, input().split()) # 보석의 개수 , 담을 수 있는 무게 
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Write your code here!
# w는 보석의 무게 , v는 보석의 가치
# 무게별 가치가 높은 보석들을 우선으로 담는다 
# N의 최대 크기는 1e5
q=[]
for i in range(N):
    heapq.heappush(q,(-v[i]/w[i] , i)) # 무게별 가치 , 보석 번호 

cur_m=0
answer=0
while cur_m<M:
    if not q:
        break
    t,i=heapq.heappop(q) # 가치가 제일 높은 보석 꺼내기
    #print(f"cur_m :{cur_m} , answer:{answer}")
    if M-cur_m >= w[i]: # 보석을 전부 담을 수 있다면은 
        answer+=v[i]
        cur_m+=w[i]
    else:
        answer+=(M-cur_m)*(-t)
        cur_m+=(M-cur_m)


print(f"{answer:.3f}")
        





