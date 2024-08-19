from collections import defaultdict
def solution(tickets):
    answer = []
    N=len(tickets)
    hash_map=defaultdict(list)
    for start , end in tickets: #간선 저장 
        hash_map[start].append([end,False])
    
    result=[]
    def dfs(node , depth , course):
        if depth==N+1:
            result.append(course)
            return course
        
        len_=len(hash_map[node])
        
        for i in range(len_):
            if hash_map[node][i][1]==False:
                hash_map[node][i][1]=True # 항공권 소모 
                next=hash_map[node][i][0]
                dfs(next, depth+1 , course+[next])
                hash_map[node][i][1]=False # 백트래킹 
        


    dfs("ICN",1,["ICN"]) # 현재 node , depth , 경로 
    result.sort()
    answer=result[0]
    
    
    

    
    return answer