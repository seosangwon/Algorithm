# 이전거가 0이면 뒤집는다. 
# 전부 뒤집었을 때, 맨 마지막이 0이면 실패 

n=int(input())
arr=list(map(int,input().split(" ")))
answer=0

for i in range(1,n):
    if arr[i-1]==0: # i-1,i,i+1 를뒤집는다 
        if i==n-1: # 맨 끝인경우
            for idx in (i-1,i):
                if arr[idx]==0:
                    arr[idx]=1
                elif arr[idx]==1:
                    arr[idx]=0
        
        else: # 맨 끝이 아닌 경우 
            try:
                for idx in (i-1,i,i+1):
                    if arr[idx]==0:
                        arr[idx]=1
                    elif arr[idx]==1:
                        arr[idx]=0
            
            except:
                print(f"idx: {idx}")
        answer+=1
        #print(answer,i,arr[i-1],arr[i])
    # print(arr)
        


if arr[-1]==0:
    print(-1)

if arr[-1]==1:
    print(answer)
    





