import heapq
N = int(input())
arr = list(map(int, input().split()))

# Write your code here!
# arr 순회 : O(N)
# log(N)으로 평균 값 계산 
answer=-int(1e9)

sum_=sum(arr)
prefix_sum=[0] * N
prefix_sum[0]=arr[0]
for i in range(1,N):
    prefix_sum[i]+=prefix_sum[i-1]+arr[i]

need_sum=[0]*N

for i in range(N):
    need_sum[i]=sum_ - prefix_sum[i]

#print(need_sum)
for i in range(1,N-1): # k는 1 ~ N-2
    q=arr[i:]
    heapq.heapify(q)
    min_v = heapq.heappop(q)
    #print(f"q : {q} , min_v : {min_v} , need_sum: {need_sum}")
    value = ((need_sum[i-1]- min_v) // (N-i-1))
    answer=max(answer , value)

print("{:.2f}".format(answer))





