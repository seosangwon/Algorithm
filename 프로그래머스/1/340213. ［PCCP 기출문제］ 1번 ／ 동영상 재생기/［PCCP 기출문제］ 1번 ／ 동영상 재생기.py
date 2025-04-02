#전부 초로 바꾸기 
#command 계산 
#result로 돌려놓기 
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def change_min_to_second(v):
        m,s=map(int,v.split(":"))
        return m*60 +s
    
    def change_second_to_min(v):
        m=v//60
        s=v%60
        minute=""
        second=""
        
        if m<=9:
            minute="0"+str(m)
        else:
            minute=str(m)
        
        if s<=9:
            second="0"+str(s)
        else:
            second=str(s)
        
        return minute+":"+second
    
    #초로 변환 
    video_len_s=change_min_to_second(video_len)
    pos_s=change_min_to_second(pos)
    op_start_s=change_min_to_second(op_start)
    op_end_s=change_min_to_second(op_end)
    
    
    current=pos_s # 현재 시각
    
    for command in commands:
        if op_start_s <= current <= op_end_s:
            current=op_end_s
        
        if command == "next":
            if current+10 > video_len_s:
                current=video_len_s
            else:
                current+=10
            
        
        if command == "prev":
            if current-10 < 0 :
                current=0
            else:
                current-=10
            
        
        if op_start_s <= current <= op_end_s:
            current=op_end_s
        
        
    
        
    answer=change_second_to_min(current)
    

    
    return answer