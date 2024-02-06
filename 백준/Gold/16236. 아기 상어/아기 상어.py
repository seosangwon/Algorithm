from collections import deque


n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

shark=2
fish=0
INF = int(1e9)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
result=0

for i in range(n):
    for j in range(n):
        if data[i][j]==9:
            x,y=i,j # 상어의 좌표 저장
            data[x][y]=0


def bfs(x,y,fish_x,fish_y):
    q=deque([(x,y,0)])
    visited=[[False for _ in range(n)] for _ in range(n)]
    visited[x][y]=True
    while q:
        x,y,cost=q.popleft()

        if x==fish_x and y == fish_y :
            return cost

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0<= ny < n and visited[nx][ny] == False and data[nx][ny] <= shark:
                visited[nx][ny]=True
                q.append((nx,ny,cost+1))
    return INF




def find_fish(x, y):
    min_dist = INF
    target = (-1, -1)
    for i in range(n):
        for j in range(n):
            if 0 < data[i][j] < shark:
                dist = bfs(x, y, i, j)
                if dist != INF and dist < min_dist:
                    min_dist = dist
                    target = (i, j)
                elif dist == min_dist:  # 거리가 같은 경우, 가장 위쪽, 가장 왼쪽에 있는 물고기를 선택
                    if target == (-1, -1) or i < target[0] or (i == target[0] and j < target[1]):
                        target = (i, j)

    return (*target, min_dist)  # Python의 unpacking을 사용하여 반환



#메인문은 물고기를 찾아내서 먹은 뒤 상어를 레벨 업 시킨다
while True:
    fish_x,fish_y,value = find_fish(x,y) # x,y는 현재 상어의 위치
    if value == INF  : # 먹을수 있는 물고기가 있는지 판단
        break
    result += value

    fish+=1 # 물고기 먹었음
    data[fish_x][fish_y]=0 #물고기 먹은 자리는 0으로 바꿔주기
    x,y=fish_x,fish_y #상어 위치 바꿔주기

    if shark == fish:  # 상어가 levelUp 되는지 판단
        shark += 1
        fish = 0

print(result)
