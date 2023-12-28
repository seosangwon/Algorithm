n,m=map(int,input().split())

data=[]
for i in range(n):
    data.append(list(input()))


col_string=[]
for i in range(m):
    temp=""
    for j in range(n):
        temp+=data[j][i]
    col_string.append(temp)


#n-1번 반복
count=0
is_overlap=False
for i in range(n-1):
    hash_map={}
    for i  in  range(m):
        col_new=col_string[i][1:]
        col_string[i]=col_new
        if col_new not in hash_map.keys():
            hash_map[col_new]=1
        else:
            is_overlap=True
            break

    if not is_overlap:
        count+=1
    else:
        break

print(count)




