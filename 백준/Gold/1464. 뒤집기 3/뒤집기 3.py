from collections import deque
data=list(input())
N=len(data)

result=deque([])
s=[]
s.append(data[0])
for i in range(N-1):
    if s[-1] >= data[i+1]:
        s.append(data[i+1])
    else:
        result.appendleft(data[i+1])

result=list(result) + s
result.reverse()


for ch in result:
    print(ch,end='')
