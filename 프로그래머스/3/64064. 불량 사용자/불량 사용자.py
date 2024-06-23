from itertools import permutations


def check(user,ban): # 순열 조합 중 하나의 리스트 , ban 리스트
    n=len(ban)
    
    for idx in range(n): # idx
        for i in range(len(ban[idx])):
            if len(ban[idx])!= len(user[idx]): # 길이가 다르다면 False
                return False
            
            if ban[idx][i]=='*': # *은 pass
                continue
            
            if ban[idx][i] != user[idx][i]: # 일치하지 않는다면
                return False
    
    return True
                


def solution(user_id, banned_id):
    answer = 0
    u_len=len(user_id)
    b_len=len(banned_id)
    
    per_list=list(permutations(user_id,b_len))
    hash_map={} # 검수 리스트 해시맵으로 생성
    
    for p_list in per_list: # 하나씩 체크
        if check(p_list,banned_id): # 체크 통과가 되면 
            
            li=list(p_list)
            li.sort()
            tuple_li=tuple(li)
            if tuple_li not in hash_map.keys() : 
                hash_map[tuple_li]=True
                answer+=1
            
            
            
        
    return answer