from itertools import combinations
import sys
input=sys.stdin.readline

n,s=map(int,input().split())
data=list(map(int,input().split()))

left=[]
right=[]

#2그룹으로 나누기
for i in range(n):
    if i<n//2:
        left.append(data[i])
    else:
        right.append(data[i])

#n의 개수에 따라서 합과 경우의 수 구하기
left_hash={}
right_hash={}

left_hash[0]=1
right_hash[0]=1

#왼쪽 그룹 작업
for i in range(1,len(left)+1):
    comb=list(combinations(left,i))
    for n in comb:
        su=sum(n)
        if su not in left_hash.keys():
            left_hash[su]=1
        else:
            left_hash[su]+=1

#오른쪽 그룸 작업
for i in range(1,len(right)+1):
    comb=list(combinations(right,i))
    for n in comb:
        su=sum(n)
        if su not in right_hash.keys():
            right_hash[su]=1
        else:
            right_hash[su]+=1


#각 해쉬의 값을 이용해서 합이 s인 경우의 수를 찾자

result=0


for l_key, l_count in left_hash.items():
    r_key = s - l_key
    if r_key in right_hash:
        result += l_count * right_hash[r_key]

# s가 0일 경우, 아무것도 선택하지 않는 경우(0, 0)를 제외해야 합니다.
if s == 0:
    result -= 1


print(result)
