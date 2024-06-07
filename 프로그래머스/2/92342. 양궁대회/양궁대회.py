from collections import defaultdict

def solution(n, info):
    answer = []
    result=[0 for _ in range(11)]
    hash_map=defaultdict(list)
    
    def dfs(depth, result,arrows):
        if depth==11:
            peach,lion=0,0
            if arrows >= 0 : # 남은 화살이 있다면은
                result[10]+=arrows
                
            for i in range(11):
                if info[i] >=1 and info[i]>= result[i]: # peach 승
                    peach+=(10-i)
                elif result[i]>=1 and info[i] < result[i]: # lion승
                    lion+=(10-i)

            
            if peach < lion: # lion이 이겼다면은 
                hash_map[lion-peach].append(result[:])
            
            result[10]-=arrows
                
            return 
        
        for i in range(2):
            if i==0 and arrows>info[depth]: #성공할 경우 
                result[depth]=info[depth]+1
                dfs(depth+1,result,arrows-(info[depth]+1))
                result[depth]=0
            else: # 실패일경우 
                dfs(depth+1,result,arrows)
    
        return 


    dfs(0,result,n)
    
    if not hash_map: # lion이 승리하지 못한다면 
        return [-1]
    
    max_value=max(hash_map.keys())
    result_list=hash_map[max_value]
    result_list.sort(key=lambda x: x[::-1] , reverse=True)
    answer=result_list[0]
    
                

    return answer