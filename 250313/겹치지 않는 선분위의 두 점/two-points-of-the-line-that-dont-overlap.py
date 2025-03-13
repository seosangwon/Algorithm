import sys 
# N개의 점 , M개의 선분 
N, M = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(M)]

# 가장 가까운 두 점의 거리의 최댓값을 출력해라 
left=0
right=int(sys.maxsize)

MAX_NUM=1e18

def is_possible(dist):
    cnt=0
    last_x= - MAX_NUM
    for a,b in segments:
        while last_x + dist <=b :
            cnt+=1
            last_x=max(a,last_x+dist)

            if cnt>=N:
                break
    
    return cnt>=N 

segments.sort()

answer=0
while left<=right:
    mid=(left+right)//2 
    if is_possible(mid): # 만족하면은 거리 값을 늘려도 됨 
        left=mid+1 
        answer=max(answer,mid)
    else: # 불만족하면은 거리 값을 줄여야 함 
        right=mid-1 


print(answer)
        


