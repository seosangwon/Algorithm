#N명의 사람 , G개의 그룹 
#그룹 인원수 , 해당 그룹에 속하는 사람의 번호가 G개 만큼 차례대로 주어진다 
# 1번째 사람은 무조건 초대를 받는다 
# k-1번 째 까지 사람을 받으면은 마지막 사람도 초대장을 받는다 


# groups : 각 그룹에 초대장을 받지 못한 사람들을 set으로 관리 
# people_groups : n번의 사람이 어느 그룹에 속해있는지 인접 리스트로 관리  
# invites : 초대 받았으면 True , 아니면 False
# 사람은 1번부터 시작 , 그룹은 0번 부터 시작 

from collections import deque

N, G = map(int, input().split())
invites=[False] * (N+1)
groups=[set() for _ in range(G)] 
people_groups = [[] for _ in range(N+1)]

q=deque()
answer=0

for i in range(G):
    li=list(map(int,input().split()))
    first=li[1]
    people_groups[first].append(i)
    
    if invites[first]==False:
        q.append(first)
        invites[first]=True
        answer+=1 # queue에 한번 들어간 사람은 초대 받은 사람 

    for e in li[2:] :
        people_groups[e].append(i)
        if invites[e]==False:
            groups[i].add(e)


#queue에 들어가있다는 것은 초대를 받았다는 것 

while q:
    num=q.popleft()

    for g in people_groups[num]: # 그 사람이 속한 그룹의 초대가 안된 set을 하나씩 본다 
        no_invited=groups[g]
        if len(no_invited)==1:
            nip=no_invited.pop()
            if invites[nip]==False: # 초대를 안받았다면 queue에 추가 
                q.append(nip)
                invites[nip]=True
                answer+=1
    


print(answer)


        

    




    
    

            
        
        




    



