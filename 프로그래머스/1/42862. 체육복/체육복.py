def solution(n, lost, reserve):
    answer=0
    #0번은 없는 사람 치고 1번부터 count
    people=[1]*(n+1)
    for i in lost:
        people[i]-=1
    for i in reserve:
        people[i]+=1
    #data 저장 완료
    for i in range(n+1):
        if people[i]==2:
            if 0<=i-1<=n and people[i-1]==0:
                people[i-1]=1
                people[i]=1
            elif 0<=i+1<=n and people[i+1]==0:
                people[i+1]=1
                people[i]=1
                
    for i in people[1:]:
        if i==1 or i==2:
            answer+=1
    #print(people)
    return answer