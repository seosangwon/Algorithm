from collections import deque
data=[0]
for _ in range(4):
    data.append(list(map(int,input())))
t=int(input())


def rotate(li,d):

    #시계방향
    if d==1:
        tmp=li[-1]
        for i in range(6,-1,-1):
            li[i+1]=li[i]
        li[0]=tmp

    #반시계방향
    else:
        tmp=li[0]
        for i in range(7):
            li[i]=li[i+1]
        li[-1]=tmp

dx=[1,-1]
def bfs(num,d): # 톱니바퀴 번호 , 방향
    visited=[False for _ in range(5)]
    q=deque([(num,d)])
    visited[num]=True # 방문 처리
    result=[(num,d)]

    while q:
        num,d=q.popleft()
        for i in range(2):
            next_n= num + dx[i]
            if 1 <= next_n <= 4 and visited[next_n]==False:
                if dx[i]==1:
                    if data[num][2]!=data[next_n][6]:
                        q.append((next_n,d*-1))
                        result.append((next_n,d*-1))
                        visited[next_n]=True
                else:
                    if data[num][6]!=data[next_n][2]:
                        q.append((next_n, d * -1))
                        result.append((next_n, d * -1))
                        visited[next_n] = True
    return result








for _ in range(t):
    num,d=map(int,input().split())
    r=bfs(num,d)
    for idx,direction in r:
        rotate(data[idx],direction)

s=0
for i in range(1,5):
    if i==1:
        if data[i][0]==1:
            s+=1
    elif i==2:
        if data[i][0]==1:
            s+=2
    elif i == 3:
        if data[i][0] == 1:
            s += 4
    elif i == 4:
        if data[i][0] == 1:
            s += 8

print(s)
