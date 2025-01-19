from collections import deque
N,M=map(int,input().split())
data=[]

for _ in range(N):
    data.append(list(map(int,input().split())))

#필요한 변수들
dx=[1,-1,0,0]
dy=[0,0,1,-1]
answer=[] # (시간 , 삭제할 치즈 좌표 리스트의 길이)
cost=0

def bfs(x,y):
    global cost
    visited[x][y]=True
    q=deque([(x,y)])
    delete_ch=[]

    while q:
        x,y=q.popleft()


        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
                if data[nx][ny]==0: # 공기라면은
                    visited[nx][ny]=True
                    q.append((nx,ny))
                if data[nx][ny]==1: # 겉면이 치즈 발견
                    visited[nx][ny]=True
                    delete_ch.append((nx,ny))

    answer.append((cost,len(delete_ch))) # 결과 리스트에 추가하기
    return delete_ch



while True:
    visited = [[False] * M for _ in range(N)]
    to_delete_ch=bfs(0,0)
    if len(to_delete_ch) == 0 :
        break
    else:
        for x,y in to_delete_ch:
            data[x][y]=0
    cost+=1 # 시간 증가


hour,cheese=answer[-2]
print(hour+1)
print(cheese)












