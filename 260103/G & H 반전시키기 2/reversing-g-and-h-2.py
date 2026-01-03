# # greedy 
# # 1. 뒤에서 진행 하되, 지금 내가 0이라면은 무조건 뒤집어야 함 
# # 2. 0번째 인덱스의 값이 0이라면 실패 

# n=int(input())
# a=list(input())
# b=list(input())

# answer=0

# #전처리 
# a_int=[]
# b_int=[]

# for v in a:
#     if v=='G':
#         a_int.append(0)
#     else:
#         a_int.append(1)
    
# for v in b:
#     if v=='G':
#         b_int.append(0)
#     else:
#         b_int.append(1)

# # G=0, H=1

# def flip(i):
#     global a_int
#     a_int=a_int^1


# for i in range(n-1,-1,-1):
#     if a_int[i]!=b_int[i]:
#         flip(i)
#         answer+=1


# print(answer)
n = int(input().strip())
a = input().strip()
b = input().strip()

flip_parity = 0  # 0이면 그대로, 1이면 G<->H 뒤집힌 상태
ans = 0

for i in range(n - 1, -1, -1):
    cur = a[i]
    if flip_parity == 1:
        cur = 'H' if cur == 'G' else 'G'

    if cur != b[i]:
        ans += 1
        flip_parity ^= 1  # i까지 뒤집는 것 = 앞으로 볼 애들 상태가 반전됨

print(ans)


