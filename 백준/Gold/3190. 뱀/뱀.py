from collections import deque

#x가 행 y가 열
def change_direction(x,y,direction):
    if (x,y)== (0,1) :
        if  direction=="D":
            x,y=1,0
        else:
            x,y=-1,0
    elif (x,y) == (1,0):
        if direction=='D':
            x,y=0,-1
        else:
            x,y=0,1

    elif (x,y) == (0,-1):
        if direction=='D':
            x,y=-1,0
        else:
            x,y=1,0

    else:
        if direction=='D':
            x,y=0,1
        else:
            x,y=0,-1
    return x,y


def move(nx,ny,sneak_queue):
    #꼬리 칸 지우기
    x,y=sneak_queue.popleft()
    graph[x][y]=0
    #머리 칸 추가하기
    sneak_queue.append((nx,ny))
    graph[nx][ny]=1

def apple_move(nx,ny,sneak_queue):
    sneak_queue.append((nx,ny))
    graph[nx][ny]=1

#nx,ny는 새로운 칸 dx,dy를 더한 칸 들이다

n=int(input())
graph=[[0 for _ in range(n)] for _ in range(n)]

k=int(input())
apple=[]
for _ in range(k):
    x,y=map(int,input().split())
    apple.append((x-1,y-1))

l=int(input())
direction_data=deque()
for _ in range(l):
    time,direction=input().split()
    time=int(time)
    direction_data.append((time,direction))

#사과 정보 넣기
for x,y in apple:
    graph[x][y]=2

#시작은 (0,0)에서 1
graph[0][0]=1

def bfs(direction_data):
    q=deque()
    q.append((0,0,0))
    sneak=deque()
    sneak.append((0,0))
    change_time, cur_direction = direction_data.popleft()
    #디폴트 진행 방향
    dx,dy=(0,1)
    while q:
        x,y,time=q.popleft()


        if time!=change_time:
            #방향전환 안하고 이동하는데 사과가 있다면은
            if 0<=x+dx<n and 0<= y+dy <n and graph[x+dx][y+dy]==2:
                apple_move(x+dx,y+dy,sneak)
                q.append((x+dx,y+dy,time+1))
            #방향전환 안하고 이동하는데 사과가 없다면
            elif 0<=x+dx<n and 0<=y+dy<n and graph[x+dx][y+dy]==0:
                move(x+dx,y+dy,sneak)
                q.append((x+dx,y+dy,time+1))
            else: #벽에 부딪히거나 자기 몸에 부딪히면은
                return time
        else: #방향전환을 해야 할 때
            dx,dy=change_direction(dx,dy,cur_direction)
            if direction_data:
                change_time, cur_direction = direction_data.popleft()
            if 0<=x+dx<n and 0<= y+dy <n and graph[x+dx][y+dy]==2:
                apple_move(x+dx,y+dy,sneak)
                q.append((x+dx,y+dy,time+1))
            #방향전환 안하고 이동하는데 사과가 없다면
            elif 0<=x+dx<n and 0<=y+dy<n and graph[x+dx][y+dy]==0:
                move(x+dx,y+dy,sneak)
                q.append((x+dx,y+dy,time+1))
            else: #벽에 부딪히거나 자기 몸에 부딪히면은
                return time

result=bfs(direction_data)
print(result+1)
