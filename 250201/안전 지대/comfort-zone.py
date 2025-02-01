# 1<=K<=100 
# K에 따라서 안전영역 개수를 구하는 DFS 로직 구현
# 1. K에 따라서 순회 
# 1-1. DFS를 실행시킨다 
# 2. DFS 로직이 끝나면은 결과 값을 answer 리스트에 [안전영역 수 , K]로 추가 
# 3. 안전영역수가 최대 , K는 작은순으로 정렬 
# 4. 정답 값 출력 

# DFS 
# K 값에 따라서 물에 잠긴 집을 업데이트 
# 물에 잠긴 집이면 pass 
# 물에 안잠긴 집이면은 근처 안잠기는 곳을 다 돌아다니면서 방문 체크 
# 모든 좌표를 돌아서 dfs를 실행 했을 때 

#BFS
# K=100 
# 50 X 50 X BFS 
# 시간초과 

# DFS 인데 K번 순회해서 끝 
#### 각 K별로 DFS가 1번만 수행해서 결과 값이 나와야 함 

from collections import deque 

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

dx=[1,-1,0,0,]
dy=[0,0,1,-1]
def bfs(x,y):
    visited[x][y]=True
    q=deque()
    q.append([x,y])
    while q: 
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and safe_zone[nx][ny]==True:
                visited[nx][ny]=True
                q.append([nx,ny])
    
    


visited=[[False]*m for _ in range(n)] # K가 증가할때마다 초기화 (메모리 초과 고려 )


safe_zone=[[True] * m for _ in range(n) ]
answer=[]
for k in range(1,101):
    for i in range(n): # 방문 처리 초기화 
        for j in range(m):
            visited[i][j]=False 


    cnt=0
    for i in range(n): # 매번 safe_zone 갱신 
        for j in range(m):
            if grid[i][j]<=k:
                safe_zone[i][j]=False
    
    for i in range(n): # bfs 실행 
        for j in range(m):
            if safe_zone[i][j] and visited[i][j]==False: # 안전하고 방문한 적이 없는 노드라면은 BFS 실행 
                bfs(i,j)
                cnt+=1 # BFS 실행시 safe_zone 1개 추가 
    
    answer.append((cnt,k))


answer.sort(key=lambda x : [-x[0] , x[1]]) # safe_zone의 개수가 크고 k는 작은 순서 
    
#print(answer)
print(answer[0][1],answer[0][0])
