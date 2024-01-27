n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
result=[]


def dfs(depth,idx):
    #중복처리 + depth
    if depth==m:
        print(' '.join(map(str,result)))
        return
    for i in range(idx,n):
        result.append(data[i])
        dfs(depth+1,i)
        result.remove(data[i])

dfs(0,0)



