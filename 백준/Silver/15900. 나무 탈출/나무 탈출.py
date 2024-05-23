import sys

N = int(input())

adj = [[] for _ in range(N+1)]
for i in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

stack = [[1, 0]]
chk = [0] * (N+1)
chk[1] = -1


ls = []

while stack:
    cn, l = stack.pop()
    chk[cn] = 1

    if cn != 1 and len(adj[cn]) == 1:
        ls.append(l)
        continue

    for nn in adj[cn]:
        if chk[nn] == 0:
            stack.append([nn, l+1])

sum_ls = sum(ls)

if sum_ls % 2:
    print('Yes')
else:
    print('No')