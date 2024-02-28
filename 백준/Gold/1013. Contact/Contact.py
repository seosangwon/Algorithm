import re
n=int(input())

for _ in range(n):
    value=input()
    p=re.compile('(100+1+|01)+')
    m=p.fullmatch(value)
    if m:
        print('YES')
    else:
        print('NO')
