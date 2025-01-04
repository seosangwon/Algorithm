# 5명의 친구 관계가 얽혀있는지 확인하는 문제
# 양방향으로 친구를 저장 : 인접리스트
N,M=map(int,input().split())
friends=[[] for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

visited=[False] * N
def dfs(x,cnt): # x는 사람 , cnt는 누적 친구 수

    # 종료조건
    if cnt==5:
        print(1)
        exit() # 프로그램 종료

    for other in friends[x]:
        if not visited[other]: # 방문을 안한 친구라면은
            visited[other]=True
            dfs(other,cnt+1)
            visited[other]=False


for i in range(N):
    visited[i]=True
    dfs(i,1)
    visited[i]=False

print(0)
