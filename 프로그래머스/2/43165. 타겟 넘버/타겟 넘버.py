def solution(numbers, target):
    global answer
    answer=0
    len_=len(numbers)
    
    
    def dfs(idx,value):
        global answer
        if idx==len_ : # 종료 조건 
            if value==target: # 문제 조건 
                answer+=1
            return
        
        
        dfs(idx+1,value+numbers[idx])
        dfs(idx+1,value-numbers[idx])
            
            
    
    
    dfs(0,0)
                
                
    
    
    return answer