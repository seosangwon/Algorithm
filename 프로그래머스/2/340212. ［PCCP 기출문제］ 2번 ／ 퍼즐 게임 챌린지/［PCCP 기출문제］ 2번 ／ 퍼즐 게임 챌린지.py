#출력 조건 : 숙련도의 최솟값을 return 
#diff - level번 틀린다. 틀릴 때 마다, time_cur 만큼의 시간을 사용
# (diff - level) * (time_cur + time_prev) + time_cur
#이전 퍼즐을 다시 풀 때는 퍼즐의 난이도에 상관없이 틀리지 않는다 
#시간 복잡도 : 문제의 최대 개수는 3e5 , 최고 diff는 1e5
#알고리즘 : 최소 난이도를 찾는 이분탐색 


def solution(diffs, times, limit):
    answer = 0
    n=len(diffs)
    left=1
    right=max(diffs)
    
    
    while left<=right:
        
        level=(left+right)//2
        
        time=0
        
        
        for i in range(n):
            if time > limit:
                break
                
            
            if diffs[i] <=level:    
                time+=times[i]
            else:
                time+=(diffs[i] - level) * (times[i]+times[i-1]) + times[i]
        
        
            
        
        if time > limit: # limit 초과
            left=level+1
        elif time < limit:
            right=level-1
        else:
            return level
            
            
    
    answer=left
    
        
    
    
    
    return answer