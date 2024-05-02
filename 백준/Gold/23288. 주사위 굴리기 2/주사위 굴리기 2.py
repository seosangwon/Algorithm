from collections import deque
N,M,K=map(int,input().split())
data=[[-1 for _ in range(M)] ]
for _ in range(N):
    data.append([-1]+list(map(int,input().split())))

dice=[4,1,3,6,2,5]


def dice_rotate(d):
    global dice
    temp=dice
    if d==0: # 동
        dice=[temp[3],temp[0],temp[1],temp[2],temp[4],temp[5]]

    elif d==1:#남
        dice=[temp[0],temp[4],temp[2],temp[5],temp[3],temp[1]]

    elif d==2:#서
        dice = [temp[1], temp[2], temp[3], temp[0], temp[4], temp[5]]

    elif d==3:#북
        dice = [temp[0], temp[5], temp[2], temp[4], temp[1], temp[3]]



dx=[1,-1,0,0]
dy=[0,0,1,-1]

def check(x,y,value):
    visited=[[False for _ in range(M+1)] for _ in range(N+1)]
    visited[x][y]=True
    q=deque([(x,y)])
    count=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=N and 1<=ny<=M and visited[nx][ny]==False and data[nx][ny]==value:
                visited[nx][ny]=True
                count+=1
                q.append((nx,ny))


    return count


def check_direct(x,y,d):

    #동,남,서,북
    A=dice[3]
    B=data[x][y]
    if A>B : # 90도 시계방향 회전
        d=(d+1)%4
    elif A<B:
        d-=1
        if d==-1:
            d=3

    return d




direct=0 # 시작은 동

d_x,d_y=1,1
score=0
for _ in range(K):



    if direct==0 :#동
        d_y += 1
        if not (1<=d_y<=M):
            d_y-=2
            direct=2



    elif direct==1:#남
        d_x += 1
        if not (1 <= d_x <= N):
            d_x -= 2
            direct = 3

    elif direct==2:#서
        d_y -= 1
        if not (1 <= d_y <=M):
            d_y += 2
            direct = 0


    elif direct==3:#북
        d_x -= 1
        if not (1 <= d_x <= N):
            d_x += 2
            direct = 1

    dice_rotate(direct)  # 주사위 굴리기

    count=check(d_x,d_y,data[d_x][d_y]) # 이동 가능한 칸 개수 구하기
   # print(count,data[d_x][d_y],(d_x,d_y),direct) # 디버깅

    score+=(count * data[d_x][d_y] ) # 점수 더하기

    direct=check_direct(d_x,d_y,direct)

print(score)

