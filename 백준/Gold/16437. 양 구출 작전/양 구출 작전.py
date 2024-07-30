import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in  range(n + 1)]

for i in range(2, n + 1):
    type, amount, root = input().split()
    amount, root = int(amount), int(root)
    if type == 'W':
        amount = -amount
    tree[root].append((i, amount))

def dfs(x, amount):
    for next, nextAmount in tree[x]:
        tmp = dfs(next, nextAmount)
        if tmp > 0:
            amount += tmp
    return amount

print(dfs(1, 0))