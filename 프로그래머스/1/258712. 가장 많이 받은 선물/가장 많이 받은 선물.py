def solution(friends, gifts):
    answer = 0
    n=len(friends)
    hash_name={}
    idx=0;
    for f in friends:
        hash_name[f]=idx
        idx+=1
    gift_data=[[0 for _ in range(n)] for _ in range(n)]
    
    results=[0 for _ in range(n)] # 각각 선물 받을 개수를 담은 리스트
    
    for str_ in gifts:
        a,b=str_.split()
        num_a=hash_name[a]
        num_b=hash_name[b]
        gift_data[num_a][num_b]+=1
    
    
    gift_jisu=[0 for _ in range(n)]
    for k in range(n):
        recieve=0
        send=0
        for i in range(n):
            send+=gift_data[k][i]
            recieve+=gift_data[i][k]
        gift_jisu[k]=(send - recieve)
    
    for i in range(n):
        for j in range(i,n):
            if i==j:
                continue
            if gift_data[i][j] > gift_data[j][i]:
                results[i]+=1
            elif gift_data[i][j] < gift_data[j][i]:
                results[j]+=1
            else:# 같을 때는 선물 지수로 비교 
                if gift_jisu[i] > gift_jisu[j]:
                    results[i]+=1
                elif gift_jisu[i] < gift_jisu[j]:
                    results[j]+=1
    answer=max(results)
        
    return answer