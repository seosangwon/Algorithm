# 모듈1 : 금 채굴 - K칸만 갈 수 있는 bfs로 계산 
# 모듈2 : 마름모 계산


#M은 금 가격
from collections import deque 
N,M = map(int,input().split())
data=[]
answer=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]



#k 만큼의 거리 까지만 탐지 가능 
def get_value(x,y,k,d): # d는 현재 거리
    visited=[[False]*N for _ in range(N)]
    q=deque([(x,y,d)])  
    visited[x][y]=True
    gold_cnt=data[x][y] # 현재 가치 

    if k==0:
        return (gold_cnt,gold_cnt * M)

    while q:
        x,y,d=q.popleft()

        if d>k: 
            continue 

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False:
                gold_cnt+=data[nx][ny]
                visited[nx][ny]=True
                q.append((nx,ny,d+1))
    
    return (gold_cnt,gold_cnt*M)
        




for _ in range(N):
    data.append(list(map(int,(input().split(" ")))))

debug_x,debug_y=0,0
max_value=0
#손해를 보지 않고 채굴해야함
for k in range(N*2+1):
    for i in range(N):
        for j in range(N):
            gold_cnt,gold_value = get_value(i,j,k,0)
            k_value=k**2+(k+1)**2
            value=gold_value-k_value
            if max_value < value:
                answer=gold_cnt


        
print(answer)
#print(debug_x,debug_y)



 
