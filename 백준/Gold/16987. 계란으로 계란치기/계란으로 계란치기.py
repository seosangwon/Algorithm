N=int(input())
data=[]
for _ in range(N):
    a,b=map(int,input().split()) # 내구도 , 무게
    data.append([a,b])

max_value=0
visited=[False for _ in range(N)]


def dfs(idx,broken_egg): # idx는 손에든 계란
    global max_value
    max_value = max(max_value, broken_egg)  # 깨진 계란의 수는 항상 매 턴마다 계산해야 한다

    if idx==N :# 최근에 든 계란이 제일 오른쪽 계란이였을 때
        return

    count=0
    for i in range(N):   # 더 이상 깰 계란이 없을 때
        if i==idx:
            continue
        if visited[i]==True:
            count+=1

        if count == N-1:
            return



    if visited[idx]==True: # 손에든 계란이 깨지고 오른쪽 한 칸의 계란도 깨져있을 때는 그 다음 칸으로 넘어간다
        dfs(idx+1,broken_egg)
        return



    for i in range(N):
        if i==idx: # 손에 든 계란은 pass
            continue
        if visited[i]==False: # 깨지지 않은 계란이라면 손에 든 계란으로  친다
            data[i][0]-=data[idx][1]
            data[idx][0]-=data[i][1] # 계란 부딪히기

            if data[i][0] <= 0 and data[idx][0]>0: # i번째 계란은 깨지고 손에 든 계란은 안깨졌을 때
                visited[i]=True
                dfs(idx+1,broken_egg+1)
                visited[i]=False # 원상복구
                data[i][0] += data[idx][1]
                data[idx][0] += data[i][1]

            elif data[idx][0] <= 0  and data[i][0]>0: # 손에든 계란만 깨졌다면은
                visited[idx]=True
                dfs(idx+1,broken_egg+1)
                visited[idx]=False # 원상복구
                data[i][0] += data[idx][1]
                data[idx][0] += data[i][1]

            elif data[idx][0] <= 0 and data[i][0] <= 0 : # 둘 다 깨졌으면
                visited[idx]=True
                visited[i]=True
                dfs(idx+1,broken_egg+2)
                visited[idx]=False # 원상복구
                visited[i]=False
                data[i][0] += data[idx][1]
                data[idx][0] += data[i][1]
            else : # 둘 다 깨지지 않았다면은
                dfs(idx+1,broken_egg)
                data[i][0] += data[idx][1] # 원상복구
                data[idx][0] += data[i][1]






dfs(0,0)
print(max_value)
