from collections import deque


N,L,R=map(int,input().split())
data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))



dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    li=[(x,y)] # (x,y,value)... 저장
    visited[x][y]=True
    q=deque([(x,y)])
    total_value=data[x][y]
    count=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False and L<= abs(data[x][y]-data[nx][ny]) <=R:
                total_value+=data[nx][ny]
                count+=1
                visited[nx][ny]=True
                q.append((nx,ny))
                li.append((nx,ny))

    #마무리 작업

    if count>=2:
        value_list=[]
        v=total_value//count
        for x,y in li:
            value_list.append((x,y,v))
        return value_list



    return []



result=0
while True:
    m_li=[]
    visited=[[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]==False:
                l=bfs(i,j)

                if l:
                    m_li+=l


    if m_li: # m_li의 원소가 있으면
        for x,y,v in m_li:
            #print(x,y,v)
            data[x][y]=v
        result+=1

    else: # m_li의 원소가 없으면
        print(result)
        break

