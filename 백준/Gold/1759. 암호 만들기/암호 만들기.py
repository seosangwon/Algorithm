from itertools import combinations

l,c = map(int,input().split())
data=list(input().split())
data.sort()
m_list=[]
j_list=[]
result=[]
#모음 자음 구분
for i in data:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        m_list.append(i)
    else:
        j_list.append(i)

comb_data=list(combinations(data,l))

for li in comb_data:
    m_count=0
    j_count=0

    for i in li:
        if i in m_list:
            m_count+=1
        else:
            j_count+=1

    if m_count>=1 and j_count>=2:
        result.append(li)

for i in result:
    print(''.join(i))
