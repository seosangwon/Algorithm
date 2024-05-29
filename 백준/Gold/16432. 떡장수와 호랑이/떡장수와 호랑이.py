N=int(input())
data=[[] for _ in range(N+1)]
for i in range(1,N+1):
    li=list(map(int,input().split()))
    for j in range(1,len(li)):
        data[i].append(li[j])

rice_cake=[]
# 방문 처리 배열 초기화
visited = [[False] * 10 for _ in range(N + 1)]


def dfs(depth,rc):

    if depth==N+1: # 무사히 마지막 날 까지 살아있다면 떡 출력 후 종료
        for dduk in rice_cake:
            print(dduk)
        exit()

    for i in range(len(data[depth])):
        if rc!=data[depth][i] and visited[depth][i] ==False: # 전날 준 떡이랑 같으면은 pass
            visited[depth][i]=True
            rice_cake.append(data[depth][i])
            dfs(depth+1,data[depth][i]) # 떡을 준다
            rice_cake.pop()


    return False


if not dfs(1,0):
    print(-1)

