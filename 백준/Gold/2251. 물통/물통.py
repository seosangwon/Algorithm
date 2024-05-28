from collections import deque
a,b,c=map(int,input().split())

visited=[[False for _ in range(b+1)] for _ in range(a+1)]

answer=[]
def bfs(x,y,z):
    global answer
    q=deque([[x,y,z]])
    while q:
        x,y,z=q.popleft()

        if visited[x][y]==True: # 이미 해본 경우의수라면 pass
            continue

        visited[x][y]=True

        if x==0: # A가 0이면은 경우의수+1
            answer.append(z)

        # A->B
        if x + y > b:  # a->b로 옮기는데 b에서 넘쳐남
            q.append([x + y - b, b, z])
        else:  # a->b로 옮기는데 b를 다 못채움
            q.append([0, x + y, z])

        # A->C
        if x + z > c:  # A->C로 옮기는데 C에서 넘쳐남
            q.append([x + z - c, y, c])
        else:  # A->C로 옮기는데 C를 다 못채움
            q.append([0, y, x + z])

        # B->C
        if y + z > c:  # B->C로 옮기는데 C에서 넘쳐남
            q.append([x, y + z - c, c])
        else:  # B->C로 옮기는데 C를 다 못채움
            q.append([x, 0, y + z])

        # B->A
        if y + x > a:  # B->A로 옮기는데 A에서 넘쳐남
            q.append([a, y + x - a, z])
        else:  # B->A로 옮기는데 A를 다 못채움
            q.append([y + x, 0, z])

        # C->A
        if z + x > a:  # C->A로 옮기는데 A에서 넘쳐남
            q.append([a, y, z + x - a])
        else:  # C->A로 옮기는데 A를 다 못채움
            q.append([x + z, y, 0])

        # C->B
        if z + y > b:  # C->B로 옮기는데 B에서 넘쳐남
            q.append([x, b, z + y - b])
        else:  # C->B로 옮기는데 B를 다 못채움
            q.append([x, z + y, 0])

    return


bfs(0,0,c)
answer.sort()

for i in answer:
     print(i,end=' ')