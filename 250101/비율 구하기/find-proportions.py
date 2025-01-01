from sortedcontainers import SortedDict
n=int(input())

tree_map=SortedDict()

for _ in range(n):
    cmd=input()
    if cmd not in tree_map.keys():
        tree_map[cmd]=1
    else:
        tree_map[cmd]+=1

for k,v in tree_map.items():
    value=round((v/n)*100,5)
    print(f"{k} {value:.4f}")
