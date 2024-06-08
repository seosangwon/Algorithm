from collections import deque
def solution(places):
    answer = []
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    def bfs(x,y,data):
        visited=[[False for _ in range(5)] for _ in range(5)]
        visited[x][y]=True
        q=deque([(x,y,1,False)]) # x,y,cost,flag
        while q:
            x,y,cost,flag=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and cost==1 and visited[nx][ny]==False:
                    if data[nx][ny]=='P': # P이면은 바로 끝
                        return 0
                    elif data[nx][ny]=='X': # 파티션이라면
                        visited[nx][ny]=True # 방문처리
                        q.append((nx,ny,cost+1,False))
                    elif data[nx][ny]=='O': # 빈자리라면
                        visited[nx][ny]=True
                        q.append((nx,ny,cost+1,True))
                
                elif 0<=nx<5 and 0<=ny<5 and cost==2 and visited[nx][ny]==False: # cost가 2일때 
                    if data[nx][ny]=='P' and flag==True: # 맨해튼거리2에서 빈자리 -> 사람 이라면 탈락
                        return 0
            
        return 1
    
    for data in places: # places는 총 5개
        p_xy=[]
        for i in range(5):
            for j in range(5):
                if data[i][j]=='P':
                    p_xy.append((i,j))
        flag=False
        for x,y in p_xy: # P좌표들로 bfs실행
            if bfs(x,y,data)==0:
                answer.append(0)
                flag=True
                break
        
        if not flag: #무사히 통과했으면
            answer.append(1)
        
            
            
    
                    
                    
            
        
        
    
    
                
         
    
    
    
    
    
    
    return answer