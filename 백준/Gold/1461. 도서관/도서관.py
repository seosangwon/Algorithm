from collections import deque

N,K=map(int,input().split())
data=list(map(int,input().split()))
data.sort()

plus=deque([])
minus=deque([])
last=True # last가 True이면 양수쪽이 더 크다
result=0

for i in range(N):
    if data[i]<0:
        minus.append(data[i])
    else:
        plus.append(data[i])


if not plus:
    last=False
elif not minus:
    last=True
elif plus[-1] > abs(minus[0]):
    last=True
elif plus[-1] < abs(minus[0]):
    last=False


if last==True and plus:
    result+=plus[-1]

    for _ in range(K):
        plus.pop()
        if not plus:
            break

elif last==False and minus:
    result+=abs(minus[0])
    for _ in range(K):
        minus.popleft()
        if not minus:
            break



#음수 처리
while True:
    if not minus:
        break

    if  len(minus)<=K:
        result+=abs(minus[0])*2
        break

    result+=abs(minus[0])*2
    for _ in range(K):
        minus.popleft()




#양수 처리
while True:
    if not plus:
        break

    if plus and len(plus) <=K:
        result+=plus[-1]*2
        break

    result+=plus[-1]*2
    for _ in range(K):
        plus.pop()


print(result)

