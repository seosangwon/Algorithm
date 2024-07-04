def solution(s):
    answer = ''
    hash_map={'zero':'0','one':'1' , 'two':'2', 'three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    string_=""
    
    
    for ch in s:
        if not ('0'<=ch<='9'): # 숫자가 아니면은
            string_+=ch
            if string_ in hash_map.keys(): # key value를 찾아주자 
                answer+=hash_map[string_]
                string_='' # 찾았으면은 string은 다시 초기화 
        
        else: # 숫자 이면은 answer에 더해준다
            answer+=ch
        

    
    return int(answer)