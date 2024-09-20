#이모티콘 플러스 서비스 가입자를 최대한 늘릴 것
#이모티콘 판매액을 최대한 늘릴 것 

# 각 이모티콘의 할인율을 설정해서 위 조건을 만족시켜 최적의 결과를 출력 할 것 
#사용자가 하는일 
#1. 할인율 넘는 이모티콘 다 삼 
#2. 이모티콘 구매 비용이 제한 값을 넘기면은 서비스를 가입함 

#시간복잡도 
# 유저의 최대 수 100 , 이모티콘의 최대 수 7 , 할인율 [10,20,30,40]
#4**7 * 100 = 2^14 * 100 -> 브루트포스 됨 


def solution(users, emoticons):
    answer = []
    n_e=len(emoticons)
    n_u=len(users)
    
    comb_list=[]
    def dfs_comb(n,li):
        if n==n_e:
            comb_list.append(li)
            return 
        
        for i in range(1,5):
            dfs_comb(n+1,li+[i*10])
        
    dfs_comb(0,[])
    
    # (2**14) * (100) * (7)
    results=[]
    for comb in comb_list: # 할인 조합 
        result=[0,0]
        for user in users:
            cost=0 # 구매 금액 
            for i in range(n_e): # 이모티콘 순서 
                if comb[i] >= user[0]: # 할인율 조건이 맞으면 산다 
                    cost+=emoticons[i] * ((100-comb[i])/100)
                    
            if user[1] <= cost:
                result[0]+=1
            else:
                result[1]+=cost
        results.append(result)
    results.sort(key=lambda x : [-x[0],-x[1]])
    
    answer=results[0]
    

    
    
    return answer