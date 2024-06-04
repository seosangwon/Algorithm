def solution(users, emoticons):
    answer = []
    len_e=len(emoticons)
    visited=[False for _ in range(len_e)]
    discount=[0 for _ in range(len_e)]
    result=[]
    
    def dfs(idx,discount):
        if idx==len_e:
            cal(discount)
           
            return
        
    
        visited[idx]=True # 방문처리 
        for j in range(10,41,10):
            discount[idx]=j
            dfs(idx+1,discount)
            discount[idx]=0
        visited[idx]=False # 백트래킹 
            

    def cal(discount):
        total=0
        free_users=0
        for user in users:
            fee=0
            flag=False
            for i in range(len_e): # 이모티콘 순회 
                if user[0] <= discount[i]: # 할인율이 높으면 이모티콘을 삼
                    
                    fee+=emoticons[i]* (1 - discount[i]/100)
                
                if fee>=user[1]: # 계산 중에 이모티콘 플러스 서비스 가입 할 조건이 성사되면 
                    free_users+=1
                    flag=True
                    break
            if not flag: # 가입을 하지 않았다면은\
                total+=int(fee)
                
        result.append([free_users,total])
        return 
                    
    
    
    
    dfs(0,discount) # idx
    result=sorted(result , key= lambda x : (-x[0] , -x[1]) )
    answer=result[0]
    
    
    
    
    
    
    return answer