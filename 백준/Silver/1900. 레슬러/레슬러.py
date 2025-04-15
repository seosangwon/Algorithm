import sys

N = int(sys.stdin.readline())
player = list()
win = dict()

for i in range(N):
    player.append(list(map(int, sys.stdin.readline().split())))
    win[i] = 0

for i in range(N - 1):
    for j in range(i, N):
        a = player[i][0] + player[j][0] * player[i][1]
        b = player[j][0] + player[i][0] * player[j][1]

        if a > b:
            win[i] += 1
        elif a < b:
            win[j] += 1

win = sorted(win.items(), key=(lambda x: x[1]), reverse=True)
for i in range(len(win)):
    print(win[i][0] + 1)