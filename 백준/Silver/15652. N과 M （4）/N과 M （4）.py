n,m=map(int,input().split())
nodes=[]

def dfs(depth,idx):
    if depth==m:
        print(' '.join(map(str,nodes)))
        return
    for i in range(idx,n+1):
        nodes.append(i)
        dfs(depth+1,i)
        nodes.remove(i)

dfs(0,1)
