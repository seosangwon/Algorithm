s = int(input())

# Write your code here!
right=int(1e9)
left=1

answer=[]

while left<=right:
    mid=(right+left)//2
    sum_=(mid+1)*mid //2

    if sum_ <=s:
        answer.append(mid)
        left=mid+1
    else:
        right=mid-1


print(max(answser))
        