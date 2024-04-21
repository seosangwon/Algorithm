from collections import deque
import copy
N,Q=map(int,input().split())
n=2**N
data=[]

for _ in range(n):
    data.append(list(map(int,input().split())))

q_list=list(map(int,input().split()))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

#회전 시키기
def rotate(l):
    len_=2**l
    global n
    c_data=copy.deepcopy(data)

    for i in range(0,n,len_):
        for j in range(0,n,len_):
            for r in range(len_):
                for c in range(len_):
                    data[i+r][j+c]=c_data[i+len_ -c -1][j+r]

def reduce():
    reduce_ice=[]
    global n
    for i in range(n):
        for j in range(n):
            count=0
            for k in range(4):
                nx= i+dx[k]
                ny= j+dy[k]
                if 0<=nx<n and 0<=ny<n and data[nx][ny]>=1:
                    continue
                count+=1

            if count>=2:
                reduce_ice.append((i,j))

    return reduce_ice


def count_ice(x,y):
    global g_count
    global max_ice
    global n
    visited[x][y]=True
    c=1
    q=deque([(x,y)])
    g_count+=data[x][y]

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and data[nx][ny]>=1:
                visited[nx][ny]=True
                g_count+=data[nx][ny]
                c+=1
                q.append((nx,ny))

    return c




for q in q_list:
    rotate(q)

    r_ice=reduce()
    for x,y in r_ice:
        if data[x][y]==0:
            continue
        data[x][y]-=1



visited=[[False for _ in range(n)] for _ in range(n)]
g_count=0
max_ice=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==False and data[i][j]>=1:
            value=count_ice(i,j)
            max_ice=max(max_ice,value)


print(g_count)
print(max_ice)
