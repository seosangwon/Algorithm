from collections import deque
n,m = map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]


def bfs():
    q=deque([(0,0)])
    ch = [[0 for _ in range(m)] for _ in range(n)]
    visited=[[False for _ in range(m)] for _ in range(n)]
    visited[0][0]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx  = x+dx[i]
            ny = y +dy[i]

            # 치즈이면은 치즈 스택 추가
            if 0<=nx<n and 0<= ny < m and data[nx][ny]!=0:
                data[nx][ny]+=1
                ch[nx][ny]+=1
            # 외부 공기이면은 이동
            elif 0<=nx<n and 0<= ny < m and data[nx][ny]==0 and visited[nx][ny]==False:
                visited[nx][ny]=True
                q.append((nx,ny))
    check=0
    for i in range(n):
        for j in range(m):
            if ch[i][j]>=2:
                data[i][j]=0
                check+=1
    if check == 0 :
        return False
    else:
        return True


result=0
while(True):
    if bfs():
        result+=1
    else:
        print(result)
        break

