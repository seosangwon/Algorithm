n=int(input())
hash_map={}
for _ in range(n):
    str_=input()
    if not str_ in hash_map:
        hash_map[str_]=1
    else:
        hash_map[str_]+=1

print(max(hash_map.values()))
