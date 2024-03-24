N,L=map(int,input().split())
data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))


def check(li):
    hash_map = {}
    for k in range(N):
        hash_map[k] = False

    for i in range(N-1):
        #높이가 2칸 차이 나면은 False
        if abs(li[i]-li[i+1]) >=2 :
            return False

        if li[i]-li[i+1] == 1  :


            for k in range(1,L):
                if  i+1+k >=N or li[i+1]!=li[i+1+k]:
                    return False

            for k in range(L):
                if hash_map[i+1+k]==True:
                    return False
                hash_map[i+1+k]=True

        if li[i+1]-li[i]==1 :
            if hash_map[i]==True:
                return False

            for k in range(1,L):
                if 0>i-k or  li[i]!=li[i-k]:
                    return False

            for k in range(L):
                if hash_map[i-k]==True:
                    return False

                hash_map[i-k]=True

    #print(hash_map)
    return True



result=0
c=1
#행 작업
for li in data:
    if check(li):
        result+=1
    #     print(c)
    # c+=1

#열 작업
for j in range(N):
    temp=[]
    for i in range(N):
        temp.append(data[i][j])
    if check(temp):
        result+=1
    #     print(c)
    # c+=1

print(result)






# print(check([3,2,2,2,3,3]))

