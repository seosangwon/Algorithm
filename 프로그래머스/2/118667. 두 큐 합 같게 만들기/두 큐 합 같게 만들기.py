def solution(queue1, queue2):
    answer = -2
    target=(sum(queue1) + sum(queue2))//2
    len_q1=len(queue1)
    left=0
    right=len_q1
    q=queue1+queue2
    result=0
    flag=False
    sum_=sum(q[left:right])

    
    
    
    while left<=right and right<len(q):
        
       
        if sum_ == target: 
            answer=result
            flag=True
            break
           
        if sum_ < target and right<len(q):
            sum_+=q[right]
            right+=1
            result+=1
            
        else:
            sum_-=q[left]
            left+=1
            result+=1
            
        
      

    if not flag : # 찾지 못했다면
        answer=-1
        
       

    
    return answer