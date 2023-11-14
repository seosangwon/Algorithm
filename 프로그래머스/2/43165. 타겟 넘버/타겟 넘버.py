from collections import deque
def solution(numbers, target):
    answer = 0
    start=0
    directions=[1,-1]
    index=0
    q=deque()
    q.append((numbers[0],start,index))
    while(q):
        node,cur,cur_index=q.popleft()
        for i in range(2):
            next_cur=cur+(node*directions[i])
            if cur_index==len(numbers)-1 and next_cur == target:
                answer+=1
            elif cur_index < len(numbers)-1 :
                 q.append((numbers[cur_index+1],next_cur,cur_index+1))
                
    return answer