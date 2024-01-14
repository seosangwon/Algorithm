def solutions(data,start,end,count):
    while start<end:
        if data[start] == data[end]:
            start+=1
            end-=1
        else:
            #왼쪽 문자열을 제거
            if data[start+1] == data[end]:
                temp=data[:start]+data[start+1:]
                if temp[::]==temp[::-1]:
                    return 1

            #오른쪽 문자열을 제거
            if data[start] == data[end-1]:
                temp=data[:end]+data[end+1:]
                if temp[::]==temp[::-1]:
                    return 1
            return 2
    return 0





n=int(input())

for _ in range(n):
    data=input()
    start=0
    end=len(data)-1
    print(solutions(data,start,end,0))


