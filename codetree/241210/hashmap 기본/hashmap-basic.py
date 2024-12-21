n=int(input())
hash_map={}
for _ in range(n):
    li=list(input().split())
    command=str(li[0])
    
    
    if command=='add':
        k,v=int(li[1]) ,int(li[2])
        hash_map[k]=v
    elif command=='find':
        k=int(li[1]) 
        if k in hash_map.keys():
            print(hash_map[k])
        else:
            print("None")
    elif command=='remove':
        k=int(li[1]) 
        if k in hash_map.keys():
            hash_map.pop(k)


    
    