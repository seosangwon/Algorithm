import sys 
# N개의 점 , M개의 선분 
N, M = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(M)]

# 가장 가까운 두 점의 거리의 최댓값을 출력해라 
left=0
right=int(sys.maxsize)

max_line = -int(1e9)
min_line=int(1e9)

for a,b in segments:
    max_line=max(max_line,b)
    min_line=min(min_line,a)

is_line=[False]*(max_line +1 )

for a,b in segments:
    for i in range(a,b+1):
        is_line[i]=True 





def is_possible(dist):
    cnt=1
    idx=min_line
    while idx <=(max_line-dist) :
        if is_line[idx+dist]: # 점을 놓을 수 있다면은 
            cnt+=1 
            idx+=dist 
        else:
            idx+=1 
        
    return cnt >= N 




while left<=right:
    mid=(left+right)//2 
    if is_possible(mid): # 만족하면은 거리 값을 늘려도 됨 
        left=mid+1 
    else: # 불만족하면은 거리 값을 줄여야 함 
        right=mid-1 


print(left-1)
        


