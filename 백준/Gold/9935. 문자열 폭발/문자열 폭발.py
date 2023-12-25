n=input()
bomb=input()
bomb_len=len(bomb)
stack=[]

for i in range(len(n)):
    stack.append(n[i])
    if ''.join(stack[-bomb_len:])==bomb:
        for i in range(bomb_len):
            stack.pop()

if not stack:
    print("FRULA")
else:
    for i in stack:
        print(i, end='')
