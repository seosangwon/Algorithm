from collections import deque
N=int(input())


def D(A):
    if A*2>9999:
        return A*2%10000
    else:
        return A*2

def S(A):
    if A==0:
        return 9999
    else:
        return A-1

def L(A):
    return (A % 1000) * 10 + A // 1000



def R(A):
    return (A//10)+(A%10)*1000




def bfs(A,B):
    visited[A]=True
    com=""
    q=deque([(A,com)])
    while q:
        A,com=q.popleft()

        for  i in range(4):
            a=D(A)
            if a==B:
                return com+'D'
            elif visited[a]==False and a!=B:
                visited[a]=True
                q.append((a,com+'D'))
            a=S(A)
            if a==B:
                return com+'S'
            elif visited[a] == False and a!=B:
                visited[a] = True
                q.append((a, com + 'S'))
            a=L(A)
            if a==B:
                return com+'L'
            elif visited[a] == False and a!=B:
                visited[a] = True
                q.append((a, com + 'L'))
            a=R(A)
            if a==B:
                return com+'R'
            elif visited[a] == False and a!=B:
                visited[a] = True
                q.append((a, com + 'R'))





for _ in range(N):
    visited = [False for _ in range(10001)]
    A,B=map(int,input().split())
    answer=bfs(A,B)
    print(answer)
    #print(A,B)
