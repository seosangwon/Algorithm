import heapq
N=int(input())
data=[]

for _ in range(N):
    a,b,c=map(int,input().split()) # 강의번호 , 시작시각 , 종료시각
    data.append((b,c))

data.sort(key=lambda x : x[0]) # 강의 시작 순서대로 정렬

q=[]
heapq.heappush(q,data[0][1]) # 첫뻔째 시작하는 강의에 종료시간을 넣는다
for i in range(1,N):
    if data[i][0] < q[0] : # 다음강의의 시작시간이 현재 q에 들어가있는 종료시간 보다 빠르다면 : 즉 강의실이 겹친다면
        heapq.heappush(q,data[i][1])
    else: # 강의실이 겹치지 않는다면 , q에 들어가 있는 강의종료 시각 보다 늦게 시작한다면
        heapq.heappop(q) # 가장 작은거 제거
        heapq.heappush(q,data[i][1])

print(len(q))
