n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: x[1])

answer=1
idx=0
fin_time=meetings[0][1]

while idx<n-1:
    if fin_time <= meetings[idx+1][0] : # 바로 뒤 회의가 시작 될 수 있다면은 
        fin_time=meetings[idx+1][1] # 다음 회의 진행 
        answer+=1
        idx+=1
        
    else:
        idx+=1

print(answer)
    
        
    

