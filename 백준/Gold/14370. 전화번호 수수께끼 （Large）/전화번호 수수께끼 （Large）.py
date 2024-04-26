from collections import defaultdict
A=[('Z','ZERO',0),('X','SIX',6),('G','EIGHT',8),
('S','SEVEN',7),('V','FIVE',5),('F','FOUR',4),
('I','NINE',9),('W','TWO',2),('R','THREE',3),
('O','ONE',1)]
for t in range(int(input())):
    d=defaultdict(int)
    arr=[0]*10
    for c in input():d[c]+=1
    for k,v,i in A:
        if d[k]>0:
            arr[i]=d[k]
            for c in v: d[c]-=arr[i]
        arr[i]=str(i)*arr[i]
    print(f"Case #{t+1}: {''.join(arr)}")