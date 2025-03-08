from itertools import combinations
# 오름차순으로 정렬 
# 시스템 응답 0~10 
def solution(n, q, ans):
    answer=0
    cmb_list=list(combinations(range(1,n+1),5))
    n=len(q)
    m=len(q[0])
    for li in cmb_list:
        flag=True
        for i in range(n): # 행 idx
            cnt=0
            if flag:
                for j in range(m): # 열 idx
                    if li[j] in q[i]:
                        cnt+=1
            if cnt != ans[i]:
                flag=False 
        
        if flag:
            answer+=1
            
                
    
    return answer