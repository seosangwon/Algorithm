import sys
sys.setrecursionlimit(100000)
n,l,r,x = map(int,input().split())
data=list(map(int,input().split()))
data.sort()
ans=0
visited=[False for _ in range(n)]


# def dfs(index,depth,sum_value,max_value,min_value):
#     global ans
#     if depth>=n:
#         return
#
#     if l <= sum_value <=r and (max_value-min_value) >=x:
#         ans+=1
#         print(visited,sum_value)
#         return
#     for i in range(index,n):
#         visited[i]=True
#         # new_max_value=-1e9
#         # new_min_value=1e9
#         # for j in range(n):
#         #     if visited[j]==True:
#         #         if new_min_value > data[j]:
#         #             new_min_value=data[j]
#         #         if new_max_value < data[j]:
#         #             new_max_value=data[j]
#         new_max_value = max(max_value, data[i]) if depth > 0 else data[i]
#         new_min_value = min(min_value, data[i]) if depth > 0 else data[i]
#         dfs(i+1,depth+1,sum_value+data[i],new_max_value,new_min_value)
#         visited[i]=False
#
# dfs(0,0,0,0,0)
# print(ans)
#

def dfs(index, depth, sum_value, max_value, min_value):
    global ans
    # 적어도 두 문제를 선택했을 때만 조건을 검사
    if depth >= 2 and l <= sum_value <= r and (max_value - min_value) >= x:
        ans += 1

    for i in range(index, n):
        # 최대값과 최소값을 업데이트
        new_max_value = max(max_value, data[i]) if depth > 0 else data[i]
        new_min_value = min(min_value, data[i]) if depth > 0 else data[i]

        # 재귀 호출
        dfs(i + 1, depth + 1, sum_value + data[i], new_max_value, new_min_value)

# 초기 호출
dfs(0, 0, 0, 0, sys.maxsize)
print(ans)

