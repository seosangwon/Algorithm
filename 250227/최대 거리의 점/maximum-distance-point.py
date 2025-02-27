n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
# Please write your code here.
# N이 최대 2십만개이다. 
# 거리를 두고 M개만큼 설치 할 수 있는지를 확인한다 
# 설치 가능하다면은 거리를 늘리고 , 설치 불가능하다면은 거리를 줄인다 

left=1
right=int(1e9)
answer=-int(1e9)


def is_possible(dist):
    cnt=1
    last_idx=0
    for i in range(1,n):
        if arr[i] - arr[last_idx] >=dist:
            cnt+=1
            last_idx=i
    
    return cnt >= m
        
    
    






while left<=right:
    mid=(left+right)//2

    if is_possible(mid): # 설치 가능하면은 거리 늘리기 
        #print(left, right , mid)
        left=mid+1
        answer=max(answer , mid)
        
    else: # 설치 불가능하면 거리 줄이기 
        right=mid-1



print(answer)

