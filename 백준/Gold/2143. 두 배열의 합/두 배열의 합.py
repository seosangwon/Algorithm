import sys
input=sys.stdin.readline
t = int(input())
n = int(input())
A_list = list(map(int, input().split()))
m = int(input())
B_list = list(map(int, input().split()))
hash_map_a = {}
hash_map_b = {}


def check_sum(li, num, hash_map):
    for i in range(num):
        key_value = li[i]
        if key_value not in hash_map.keys():
            hash_map[key_value] = 1
        else:
            hash_map[key_value] += 1
        for j in range(i+1,num):
            key_value += li[j]
            if key_value not in hash_map.keys():
                hash_map[key_value] = 1
            else:
                hash_map[key_value] += 1
    return


check_sum(A_list, n, hash_map_a)
check_sum(B_list, m, hash_map_b)
hash_map_a=sorted(hash_map_a.items(),key=lambda x:x[0])
hash_map_b=sorted(hash_map_b.items(),key=lambda x:x[0])

count=0
start=0
end=len(hash_map_b)-1

while start<len(hash_map_a) and end >= 0:

    if hash_map_a[start][0] + hash_map_b[end][0] == t:
        count+=hash_map_a[start][1]*hash_map_b[end][1]
        start+=1
    elif hash_map_a[start][0] + hash_map_b[end][0] > t:
        end -= 1
    else:
        start += 1

print(count)
