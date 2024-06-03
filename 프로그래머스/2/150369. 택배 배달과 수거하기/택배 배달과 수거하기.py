def solution(cap, n, deliveries, pickups):
    answer = 0
    d=0
    p=0
    
    for i in range(n-1,-1,-1):
        cnt=0
        while d<deliveries[i] or p < pickups[i]: # 배달 , 수거 할게 남아있다면은
            cnt+=1
            d+=cap
            p+=cap
        d-=deliveries[i]
        p-=pickups[i]
        answer+=(i+1)*cnt
    
    return answer *2
  


