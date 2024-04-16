r,c,k=map(int,input().split())
A=[]
for _ in range(3):
    A.append(list(map(int,input().split())))

def RC():
    global A

    result_A=[[] for _ in range(len(A))]
    row=0
    for li in A:
        s=set()
        hash_map={}
        for o in li: #o는 원소 하나하나
            if o==0:
                continue
            s.add(o)
        for o in s:
            hash_map[o]=0

        for i in li:
            if i==0:
                continue
            hash_map[i]+=1


        l=list(hash_map.items())
        l.sort(key=lambda x:(x[1],x[0]))

        for a,b in l:
            result_A[row]+=[a,b]
        row+=1



    # 0 채워주기
    max_len=0
    for i in result_A:
        max_len=max(max_len,len(i))

    for i in result_A:
        if len(i)!=max_len:
            for _ in range(max_len - len(i)):
                i.append(0)

    A=result_A

    return

count=0
while count<=100:
    if len(A) > r-1 and len(A[0]) > c-1 and A[r-1][c-1] == k:
        print(count)
        break

    if len(A) >= len(A[0]):
        RC()

    else:
        A=list(zip(*A))
        RC()
        A=list(zip(*A))

    count+=1


if count==101:
    print(-1)
