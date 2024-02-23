from collections import deque

n,m=map(int,input().split())
r,c,d=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))


#복 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#북->서 , 서->남 , 남->동 , 동-> 북
def change_direction(d):
    if d==0:
        return 3
    elif d==1:
        return 0
    elif d==2:
        return 1
    elif d==3:
        return 2


visited=[[False for _ in range(m)] for _ in range(n)]

# while문 들어가기 이전에
x,y=r,c
result=0
while True:
    check=False


    if data[x][y]==0 and not visited[x][y]:
        result+=1
        visited[x][y]=True
        #print('True')

    for _ in range(4):
        #현재 방향으로 한 칸 이동
        d = change_direction(d)
        nx=x+dx[d]
        ny=y+dy[d]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and data[nx][ny]==0:
            x+=dx[d]
            y+=dy[d] # 좌표 이동
            check=True # 주위에 빈칸이 있다는 것을 체크
        #    print('check=True')
            break
    
    #for문을 빠져나왔다는 것은 이동을 했거나 , 4방향에 빈칸이 없을 때
    if check==True : #4방향에 빈칸이 있었고 이동 했을 때
       # print("while문 실행")
        continue

    else: # 4방향에 빈칸이 없을 때 후진
        nx=x+dx[d]*-1
        ny=y+dy[d]*-1
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
            x = nx
            y = ny

        else:  #후진해서 벽에 부딪히면 작동중지
            print(result)
            exit()
