from collections import defaultdict
def solution(clothes):
    answer = 1
    hash_map=defaultdict(list)
    
    for value,key in clothes:
        if value not in hash_map[key]:
            hash_map[key].append(value)
    
    
    for li in hash_map.values():
        answer*=(len(li)+1)
    
    answer-=1
            
    
    
    return answer