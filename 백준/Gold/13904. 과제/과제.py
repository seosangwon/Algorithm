import heapq
n=int(input())
max_heap=[]
for _ in range(n):
    deadline,point=map(int,input().split())
    heapq.heappush(max_heap,(-point,point,deadline))

days=[(0,0) for _ in range(1001)]
result=0

while max_heap:
    temp,point,deadline=heapq.heappop(max_heap)
    while (deadline > 0):
        if days[deadline] == (0,0):
            days[deadline] = (point,deadline)
            break
        else:
            deadline -= 1

for i in range(1,1001):
    result += days[i][0]

print(result)


