import bisect

n=int(input())
data=list(map(int,input().split()))


def lis(li):
    LIS=[li[0]]

    for i in range(1,n):
        pos=bisect.bisect_left(LIS,li[i])
        
        if pos == len(LIS):
            LIS.append(li[i])

        else:
            LIS[pos]=li[i]


    return len(LIS)


print(lis(data))

