def solution(record):
    answer = []
    hash_map={}
    
    
    #닉네임 수정
    for r in record :
        command,user_id,nick_name='','',''
        value=''
        for i in range(len(r)):
            if r[i]==' ' and command=='':
                command=value
                value=''
            elif r[i]==' ' and command!='':
                user_id=value
                value=''
            elif i==len(r)-1 and user_id=='':
                user_id=value
                value=''
            elif i==len(r)-1 and user_id!='':
                value+=r[i]
                nick_name=value
            
            else:
                value+=r[i]
        
            
        if command=='Enter':
            hash_map[user_id]=nick_name

        elif command=='Leave':
            continue
            
        else:
            hash_map[user_id]=nick_name
            
    #print(hash_map)
    
    #닉네임 수정 완료
    for r in record:
        command,user_id,nick_name='','',''
        value=''
        for i in range(len(r)):
            if r[i]==' ' and command=='':
                command=value
                value=''
            elif r[i]==' ' and command!='':
                user_id=value
                value=''
            elif i==len(r)-1 and user_id=='':
                value+=r[i]
                user_id=value
                value=''
            elif i==len(r)-1 and user_id!='':
                value+=r[i]
                nick_name=value
            
            else:
                value+=r[i]
        
        #print(command,user_id)
        
        if command=='Enter':
            value=str(hash_map[user_id])
            value+='님이 들어왔습니다.'
            answer.append(value)
        elif command=='Leave':
            value=str(hash_map[user_id])
            value+='님이 나갔습니다.'
            answer.append(value)
        else:
            continue

    

    
    return answer