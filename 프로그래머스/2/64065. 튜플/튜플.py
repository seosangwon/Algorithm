def solution(s):
    answer=[]
    s=s[2:-2] # {{ }} 떼버리기
    s=s.split("},{") # split하면 list가 됨 
    list_s=[]
    for part_s in s: # 
        list_s.append(list(map(int,part_s.split(','))))
    list_s.sort(key=lambda x: (len(x))) # 각 원소의 길이를 기준으로 정렬 오름차순 
    
    
    for li in list_s: # 작은 길이의 리스트 먼저 순서대로 대입
        for value in li: # value 값을 차례대로 뽑아냄 
            if value not in answer:
                answer.append(value)
    
    

    return answer