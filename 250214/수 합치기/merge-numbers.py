import heapq
N = int(input())
arr = list(map(int, input().split()))

# N의 최대 수는 1e5
# 결국 가장 작은 수 2개를 계속해서 합하면 된다 
heapq.heapify(arr)


answer=0
while arr:
    if len(arr)==1:
        break

    f=heapq.heappop(arr)
    s=heapq.heappop(arr)
    answer+=(f+s)
    heapq.heappush(arr,(f+s))

print(answer)
    



