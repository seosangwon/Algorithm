# N은 5만개 

N = int(input())
B=[]
A=set()

for _ in range(N):
    v=int(input())
    B.append(v)

for i in range(1,2*N+1):
    if i not in B:
        A.add(i)

B.sort()
answer=0

for card in B:
    cnt=1
    while True:
        if card+cnt in A: #A에 더 높은 카드가 있으면은 
            answer+=1
            A.remove(card+cnt)
            break 
        else:
            cnt+=1
        
        if card+cnt >2*N:
            break 

print(answer)







