# n은 최대 100
# 1번째 행은 선택 X 
# 현재 행렬의 위치가 (x,y) 라고 할 때 
# (x-1,y)가 0이면은 무조건 1로 바꿔줘야함 
# 마지막행에서 본인이 0인데 (x-1,y)가 1인 경우에는 절대 1로 바꿀 수 없음 -> -1 출력 

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]

#변수 
answer=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]

#함수
def flip(x,y):
    # print(x,y)
    if data[x][y]==0:
        data[x][y]=1
    elif data[x][y]==1:
        data[x][y]=0

    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if data[nx][ny]==0:
                data[nx][ny]=1
            elif data[nx][ny]==1:
                data[nx][ny]=0



# 그리디 
for i in range(1,n):
    for j in range(n):
        if data[i-1][j]==0:
            flip(i,j)
            # print(i,j)
            # for i in range(n):
            #     for j in range(n):
            #         print(data[i][j],end=' ')
            #     print()
            answer+=1
    


# 검수 
flag=True
for i in range(n):
    if data[n-1][i]==0:
        flag=False
        break

if flag:
    print(answer)
else:
    print(-1)
        


# 디버깅
# for i in range(n):
#     for j in range(n):
#         print(data[i][j],end=' ')
#     print()