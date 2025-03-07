from itertools import combinations
# 오름차순으로 정렬 
# 시스템 응답 0~10 
def solution(n, q, ans):
    answer=0
    lst=[i for i in range(1,n+1)]
    index=list(filter(lambda i : ans[i] == 0 , range(len(ans))))
    m=len(ans)
    
    for i in index:
        for j in q[i]:
            try: lst.remove(j)
            except: pass
    for c in combinations(lst,5):
        for i in range(m):
            cnt=0
            for j in q[i]:
                if j in c:
                    cnt +=1
            if cnt != ans[i]:
                break
        else:
            answer+=1
                
    
    return answer