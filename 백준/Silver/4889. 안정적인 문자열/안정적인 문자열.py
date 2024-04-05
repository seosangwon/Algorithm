idx=0
while True:
    idx+=1
    data=list(input())
    if data[0]== '-':
        break

    stack=[]
    count=0
    for i in range(len(data)):
        if data[i]=='{':
            stack.append('{')

        else:
            if stack:
                stack.pop()
            else:
                count+=1
                stack.append('{')
    count+=len(stack)//2

    print(f"{idx}. {count}")

