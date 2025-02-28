import sys
n = int(input())

# Please write your code here.
answer=0
reminder=0
# 1. N을 5로 전부 나눈다 
answer+=(n//5)
reminder=(n%5)

#2. 나머지를 2로 전부 나눈다 
answer+=(reminder //2)
reminder = (reminder %2)

if reminder:
    print(-1)
else:
    print(answer)

