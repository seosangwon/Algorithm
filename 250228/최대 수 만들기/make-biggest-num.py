from functools import cmp_to_key

n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!


def compare(a,b):
    if str(a)+str(b) > str(b)+str(a):
        return -1 # 순서가 맞음 
    if str(a) + str(b) < str(b) + str(a):
        return 1 # 순서를 바꿔야 함 
    return 0





arr.sort(key=cmp_to_key(compare))
print("".join(map(str,arr)))
