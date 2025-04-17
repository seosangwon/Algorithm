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

def is_possible(dist):
    cnt=0
    last_x= - MAX_NUM
    for a,b in lines:
        while last_x + dist <=b :
            cnt+=1
            last_x=max(a,last_x+dist)

            if cnt>=N:
                break
    
    return cnt>=N 


while left<=right:
    mid=(left+right)//2

    if is_possible(mid): # 해당 거리로 가능하다면은 거리를 늘려준다 
        left=mid+1 
        answer=max(answer,mid)
        
    
    else: # 불가능하다면은 거리를 줄여준다 
        right=mid-1 



print(int(answer))


