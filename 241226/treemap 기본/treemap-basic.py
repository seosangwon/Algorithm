from sortedcontainers import SortedDict
n=int(input())
tree_map=SortedDict()

for _ in range(n):
    command_list=list(input().split())
    command=command_list[0]
    for i in range(1,len(command_list)):
        command_list[i]=int(command_list[i])
    
    if command=="add":
        tree_map[command_list[1]]=command_list[2]
    elif command=="find":
        if command_list[1] in tree_map.keys():
            print(tree_map[command_list[1]])
        else:
            print("None")
    elif command=="print_list":
        if tree_map:
            for key,value in tree_map.items():
                print(value,end=' ')
            print()
        else:
            print("None")

    elif command=="remove":
        if command_list[1] in tree_map.keys():
            tree_map.pop(command_list[1])

    
