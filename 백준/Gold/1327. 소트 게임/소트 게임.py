from collections import deque

n,k=map(int,input().split())
data=input().split()


#문자열 data를 파라미터로 받은 뒤 list로 수정 후 flip 실행 후 다시 문자열로 변경해서 반환하자
def flip(node_str,index,k):
    temp=[node_str[i] for i in range(index,index+k)]
    j=k-1
    node_list=list(node_str)
    for i in range(index,index+k):
        #temp의 index는 0~k-1
        node_list[i]=temp[j]
        j-=1
    node_str=''.join(map(str,node_list))
    return node_str


data=''.join(map(str,data))
def bfs(data,k):
    q=deque([(data,0)])

    sorted_str=''.join(sorted(data))
    if data==sorted_str:
        return 0

    hash_map={}

    while q:
        node,flip_count=q.popleft()
        for i in range(len(node)-k+1):
            flip_node=flip(node,i,k)

            if flip_node == sorted_str:
                return flip_count+1

            if flip_node not in hash_map:
                hash_map[flip_node]=flip_count+1
                q.append((flip_node,flip_count+1))

    return -1


print(bfs(data,k))
