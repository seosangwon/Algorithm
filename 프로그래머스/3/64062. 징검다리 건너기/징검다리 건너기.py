def solution(stones, k):
    start=1
    end=max(stones)
    
    
    while start<=end:
        mid=(start+end)//2
        cnt=0
        
        for stone in stones:
            if stone-mid <=0:
                cnt+=1
                if cnt>=k: # 못건너는경우
                    end=mid-1 
                    break
            
            else:
                cnt=0
                
        else:
            start=mid+1
                

    return start

