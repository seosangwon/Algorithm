#알파벳 하나는 지게차로 , 알파벳2개가 연속인 것은 크레인을 사용해서 모든 컨테이너를 꺼낸다 
# n,m은 최대 50개 
# 지게차일경우 , 해당 알파벳이 외부랑 접해있는지 확인
# 크레인일경우 , 해당 알파벳을 전부 제거 
import sys 
sys.setrecursionlimit(int(1e6))


def remove_c(a,data):
    n=len(data)
    m=len(data[0])
    remove_cnt=0
    
    for i in range(n):
        for j in range(m):
            if data[i][j]==a:
                data[i][j]=""
                remove_cnt+=1
    
    return remove_cnt 

def remove_j(a,data):
    n=len(data)
    m=len(data[0])
    remove_cnt=0
    visited=[[False]*(m) for _ in range(n)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    def dfs(x,y):
        nonlocal remove_cnt 
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and (data[nx][ny]=="" or data[nx][ny]==a):
                visited[nx][ny]=True 
                if data[nx][ny]=="":
                    dfs(nx,ny)
                
                if data[nx][ny]==a:
                    remove_cnt+=1
                    data[nx][ny]=""
        
        
    
    
    
    visited[0][0]=True 
    dfs(0,0)
    return remove_cnt
                
    
    


            
                    
    


def solution(storage, requests):
    n=len(storage)
    m=len(storage[0])
    answer = n*m
    
    #빈벽을 가로세로 하나씩 늘리자 
    for i in range(n):
        storage[i]=[""]+list(storage[i])+[""]
    
    storage=[[""]*(m+2)] + storage + [[""]*(m+2)]
    
    
    
    for i in range(n+2):
        for j in range(m+2):
            print(storage[i][j],end=' ')
        print()
    
    
    for r in requests:
        r_block=0
        if len(r)==1:
            #지게차로 해당 알파벳 제거 
            r_block=remove_j(r[0],storage)
        if len(r)==2:
            #크레인으로 해당 알파벳 제거 
            r_block=remove_c(r[0],storage)
        answer-=r_block 
    
    
    return answer