import heapq
n=int(input())
data=[]
room=[]
for _ in range(n):
    start,end = map(int,input().split())
    data.append((start,end))

data.sort()
#첫 수업의 끝나는 시간을 heapq에 넣는다
heapq.heappush(room,data[0][1])
count=1

for i in range(1,n):
    if data[i][0] < room[0]:
        #강의실을 생성한다면 강의에 끝나는 시각의 값을 넣는다
        heapq.heappush(room,data[i][1])
        count+=1
    else:
        heapq.heappop(room)
        heapq.heappush(room,data[i][1])

print(count)


