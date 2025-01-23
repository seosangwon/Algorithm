import heapq
N = int(input())
arr = list(map(int, input().split()))

# Write your code here!
# arr 순회 : O(N)
# log(N)으로 평균 값 계산 
answer=-int(1e9)
q=[]
sum_val=arr[N-1]
max_val=-int(1e9)
heapq.heappush(q,arr[N-1])

for i in range(N-2,0,-1):
    heapq.heappush(q,arr[i]) # k개가 제거되고 난 후의 바로 오는 값을 heapq에 넣는다 
    sum_val+=arr[i] 
    min_v = q[0] # 현재 힙큐의 최솟 값 

    max_val=max(max_val , (sum_val - min_v) / (N-i-1) )

print("{:.2f}".format(max_val))




    
    



