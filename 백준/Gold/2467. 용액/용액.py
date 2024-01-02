n=int(input())
data=list(map(int,input().split()))
result=[]
start=0
end=n-1

def solutions(start,end,data):
    diff_zero=1e18
    result=()
    while(start<end):

        sum_value=data[start]+data[end]

        if sum_value==0:
            return (data[start],data[end])
        elif sum_value >0:
            end-=1
            if diff_zero>=abs(sum_value):
                diff_zero=abs(sum_value)
                result=(data[start],data[end+1])

        else:
            start+=1
            if diff_zero>=abs(sum_value):
                diff_zero=abs(sum_value)
                result=(data[start-1],data[end])



    return result



sol=solutions(start,end,data)
for i in sol:
    print(i,end=" ")