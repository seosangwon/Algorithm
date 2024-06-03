def dfs(idx,value,visited):
    global max_value
    if idx==11:
        max_value=max(max_value,value)
        return

    for i in range(11):
        if visited[i]==True or data[i][idx]==0:
            continue
        visited[i]=True
        dfs(idx+1,value+data[i][idx],visited)
        visited[i]=False






T=int(input())
for _ in range(T):
    data=[]
    max_value=0
    for _ in range(11):
        data.append(list(map(int,input().split())))

    visited=[False for _ in range(11)]
    dfs(0,0,visited)
    print(max_value)


