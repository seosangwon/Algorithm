from collections import deque
def solution(progresses, speeds):
    answer = []
    q=deque()
    for i in range(len(progresses)):
        q.append([progresses[i],speeds[i]])
    while q:
        count=0
        for i in range(len(q)):
            q[i][0]+=q[i][1]
        while(q and q[0][0]>=100):
            q.popleft()
            count+=1
        if count>0:
            answer.append(count)



    return answer


