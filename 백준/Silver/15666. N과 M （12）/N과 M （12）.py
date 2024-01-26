import sys
sys.setrecursionlimit(10000)
n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
numbers=[]
hash_map={}


def dfs(depth,index):
    if depth==m:
        k=' '.join(map(str,numbers))
        if k not in hash_map.keys():
            hash_map[k]=True
            print(k)
        return
    for i in range(index,n):
        numbers.append(data[i])
        dfs(depth+1,i)
        numbers.pop()

dfs(0,0)