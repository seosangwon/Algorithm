n=int(input())
data=[]
max_value=0
hash_map={}

for i in range(n):
    a,b,c,d,e,f=map(int,input().split())
    data.append([(a,f),(b,d),(c,e)])

for i in range(n):
    for a,b in data[i]:
        hash_map[(i,a)]=b
        hash_map[(i,b)] = a



def find_max_value(node1,node2):
    dice=[1,2,3,4,5,6]
    dice.remove(node1)
    dice.remove(node2)
  
    return max(dice)



max_value=0


for a,b in data[0]:
    up=a
    down=b
    value=find_max_value(up,down)
    for i in range(1,n):
        down=up
        up=hash_map[(i,down)]
        value+=find_max_value(up,down)

    max_value=max(max_value,value)


for a,b in data[0]:
    up=b
    down=a
    value=find_max_value(up,down)
    for i in range(1,n):
        down=up
        up=hash_map[(i,down)]
        value+=find_max_value(up,down)

    max_value=max(max_value,value)





print(max_value)

