N=int(input())
operand=list(map(int,input().split()))
operator=list(map(int,input().split()))
max_value=-int(1e9)
min_value=int(1e9)

def backtracking(depth,expression):
    global max_value
    global min_value
    if depth== N-1:
        value=eval(expression)
        max_value=max(max_value,value)
        min_value=min(min_value,value)
        return

    for i in range(4):
        if operator[i]==0:
            continue

        if i==0: # +
            operator[i]-=1
            backtracking(depth + 1,expression+ "+" + str(operand[depth+1]))
            operator[i] += 1

        elif i==1: # -
            operator[i] -= 1
            backtracking(depth + 1, expression + "-" + str(operand[depth+1]))
            operator[i] += 1

        elif i==2: # X
            operator[i] -= 1
            backtracking(depth + 1, expression + "*" + str(operand[depth+1]))
            operator[i] += 1

        elif i==3: # %
            operator[i] -= 1
            backtracking(depth + 1, expression + "//" + str(operand[depth+1]))
            operator[i] += 1
    return



backtracking(0,str(operand[0]))
print(max_value)
print(min_value)