import sys

def cal(a, b, visited):
    x = b // a
    x += 1 if b % a != 0 else 0
    while x in visited:
        x += 1
    return x

N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    x = b
    visited = set()
    if a != 1:
        while True:
            x = cal(a, b, visited)
            a = (a * x) - b
            b = b * x
            visited.add(x)
            if a == 0:
                break
    print(x)