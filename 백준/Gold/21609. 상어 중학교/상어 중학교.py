from collections import deque


N,M=map(int,input().split()) # N by N , M은 색상의 개수
data=[]

for _ in range(N):
    data.append(list(map(int,input().split())))



dx=[1,-1,0,0]
dy=[0,0,1,-1]


def bfs(x,y,color): # 좌표 , 블럭 색상
    visited=[[False for _ in range(N)] for _ in range(N)]
    visited[x][y]=True


    visit_color[x][y]=True

    q=deque([(x,y,1)]) # 좌표 , 블럭 개수 count
    li=[(x,y,color)]

    while q:
        x,y,count=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False  and (data[nx][ny]==0 or data[nx][ny]==color):
                visited[nx][ny]=True
                q.append((nx,ny,count+1))
                li.append((nx,ny,data[nx][ny]))
                if data[nx][ny]!=0:
                    visit_color[nx][ny]=True

    return li

#검은 블록을 제외한 모든 블록이 행의 큰 칸으로 내려간다
def gravity():
    for i in range(N-2,-1,-1):
        for j in range(N):
            if data[i][j]>=0:
                row=i+1
                while True:
                    if data[row][j]!=-2: # 밑에 블럭이 있다면은
                        break

                    if row==N-1 and data[row][j]==-2: # 맨 밑 바닥이 빈칸이라면
                        data[row][j]=data[i][j]
                        data[i][j]=-2
                        break

                    if data[row][j]==-2 and data[row+1][j]!=-2: # gravity
                        data[row][j]=data[i][j]
                        data[i][j]=-2
                        break

                    row+=1






score=0
#main
while True:
    block_group = []
    visit_color = [[False for _ in range(N)] for _ in range(N)]

    normal = []
    for i in range(N):
        for j in range(N):
            if data[i][j] >= 1:
                normal.append((i, j, data[i][j]))

    for x,y,k in normal:
        if visit_color[x][y]==True:
            continue

        li=bfs(x,y,k) # k는 일반 블록의 color

        if len(li)<=1:
            continue

        count=len(li)
        rainbow=0
        min_row=1e9
        min_col=1e9

        #(개수 , 무지개 개수 , 가장 큰 행 , 가장 큰 열 )
        for li_x,li_y,li_color in li:
            if li_color==0:
                rainbow+=1
            if li_color!=0:
                min_row=min(min_row, li_x)
                min_col=min(min_col,li_y)

        block_group.append((count,rainbow,min_row,min_col,li))



    if not block_group:
        break


    #block_group 람다 정렬 후 제일 큰 그룹 찾기
    block_group.sort(key=lambda x : (-x[0],-x[1],-x[2],-x[3]))
    group=block_group[0][4]



    # 점수 계산
    #print(block_group[0][0]**2)
    score+=block_group[0][0]**2

    #그룹 제거
    for x,y,k in group:
        data[x][y]=-2 # -2로 값을 적용해서 제거 시키자

    #중력
    gravity()

    #90도 회전
    temp=[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp[i][j]=data[j][N-i-1]

    data=temp

    gravity()


    # for i in range(N):
    #     for j in range(N):
    #         print(data[i][j],end=' ')
    #     print()



print(score)

