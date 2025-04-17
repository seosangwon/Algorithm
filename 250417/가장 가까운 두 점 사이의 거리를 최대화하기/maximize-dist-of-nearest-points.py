#N의 최댓값은 1e5 
N=int(input())
lines=[]
for _ in range(N):
    s,e=map(int,input().split())
    lines.append((s,e))

lines.sort()

left=0
right=1e9
answer=0
MAX_NUM=1e9

# def is_possible(x):
#     pos=lines[0][0]
#     for idx in range(1,N):
#         print(pos ,x )
#         if lines[idx][0]<= pos+x <= lines[idx][1]:
#             pos+=x
#         else:
#             return False 
#     return True 


def is_possible(mid):
    curr_x, _ = lines[0]            # 최적의 점의 위치를 구해줍니다.
    for x1, x2 in lines[1:]:
        if x2 < curr_x + mid:          # 최소 거리를 더했는데 구간을 벗어난다면
            return False               # 불가능한 경우입니다.
        curr_x = max(curr_x + mid, x1) # 최적의 점의 위치를 갱신합니다.
    
    return True  

while left<=right:
    mid=(left+right)//2

    if is_possible(mid): # 해당 거리로 가능하다면은 거리를 늘려준다 
        left=mid+1 
        answer=max(answer,mid)
        
    
    else: # 불가능하다면은 거리를 줄여준다 
        right=mid-1 



print(int(answer))


