from collections import deque

n, m = map(int, input().split())

data = []
zeros = []
for _ in range(n):
    data.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            zeros.append((i, j))

dx = [1, -1, 0, 0, ]
dy = [0, 0, 1, -1]
visited = [[False for _ in range(m)] for _ in range(n)]


def bfs_space_check(x, y):
    # x,y,그룹 번호 , 한 그룹의 0의 개수
    if visited[x][y]==True:
        return
    visited[x][y]=True
    result=[(x,y)]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny]=True
                result.append((nx,ny))
                q.append((nx,ny))
    return result

num=1
hash_map={}
for i in range(n):
    for j in range(m):
        if data[i][j]==0:
            points=bfs_space_check(i,j)
            if points:
                count=len(points)
                for x,y in points:
                    hash_map[(x,y)]=num,count # 그룹 번호 , 0의 개수
                num+=1


for i in range(n):
    for j in range(m):
        if data[i][j]==1:
            result=set()
            for k in range(4):
                nx= i + dx[k]
                ny= j + dy[k]
                if 0<=nx <n and 0<=ny<m and data[nx][ny]==0:
                    if (nx,ny) in hash_map.keys():
                        group_num , zero_count = hash_map[(nx,ny)]
                        result.add((group_num,zero_count))

            result_count=1
            for num,c in result:
                result_count+=c
            data[i][j]=result_count%10

for i in range(n):
    for j in range(m):
        print(data[i][j],end='')
    print()


