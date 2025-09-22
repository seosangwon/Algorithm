# s의 길이는 최대 1000
# 문자열을 자를 개수는 x , x의 최대 크기는 500
# 걍 완전탐색 
# 500 X 1000 = 5e5


def solution(s):
    answer = len(s)
    
    for x in range(1,len(s)//2+1):
        cmp_str=s[:x]   
        cnt=1
        numer=0
        value=0
        for idx in range(x,len(s),x):
            cur=s[idx:idx+x]
                
            if cmp_str==cur: # 중첩됨
                cnt+=1
            else: # 중첩안됨
                value += len(cmp_str) + (len(str(cnt)) if cnt > 1 else 0)
                cmp_str = cur
                cnt = 1
        
        #마지막 값 계산 
        value += len(cmp_str) + (len(str(cnt)) if cnt > 1 else 0)
        
        answer=min(answer,value)

    print(answer)
                
            
            
            
    return answer