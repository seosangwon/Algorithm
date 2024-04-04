import sys
input = sys.stdin.readline
s = input()
n = int(input())
re = [[0]*26 for i in range(len(s))]
for i in range(len(s)):
    for j in range(26):
        if ord(s[i])-97==j:
            re[i][j] = re[i-1][j]+1 #한번 나왔으니 누적합 +1
        else:
            re[i][j] = re[i-1][j]#안 나왔으니 누적합
for _ in range(n):
    t,x,y = input().split()
    if int(x)==0:
        print(re[int(y)][ord(t)-97])#0~y번째까지니 그냥 [y]를 출력해주면 된다.
    else:
        print(re[int(y)][ord(t)-97]-re[int(x)-1][ord(t)-97])#x~y까지이니 [y]-[x-1]를 출력해주면 된다.