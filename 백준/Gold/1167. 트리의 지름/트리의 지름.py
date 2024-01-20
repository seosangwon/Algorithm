import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(cur_node,cur_cost):
    for next_node,next_cost in tree[cur_node]:
        if distance[next_node]==-1:
            distance[next_node]=cur_cost+next_cost
            dfs(next_node,next_cost+cur_cost)
    return distance









n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n):
    value=list(map(int,input().split()))
    node=value[0]
    for i in range(1, len(value), 2):
        if value[i] == -1:
            break
        else:
            #(node,cost)
            tree[node].append((value[i],value[i+1]))

distance=[-1 for _ in range(n+1)]
distance[1]=0
distance_1=dfs(1,0)
father_node=distance_1.index(max(distance_1))

distance=[-1 for _ in range(n+1)]
distance[father_node]=0
distance_result=dfs(father_node,0)
print(max(distance_result))