#전위순회 : 부모 - 왼쪽 자식 - 오른쪽 자식
#중위순회 : 왼쪽자식 - 부모 - 오른쪽 자식
#후위순회 : 왼쪽자식 - 오른쪽자식 - 부모 
n=int(input())
left,right={},{}

for _ in range(n):
    x,l,r=input().split()
    left[x]=l 
    right[x]=r


def pre_order(node):
    if node=='.':
        return
    
    print(node,end="")
    pre_order(left[node])
    pre_order(right[node])

def in_order(node):
    if node=='.':
        return 
    
    in_order(left[node])
    print(node,end="")
    in_order(right[node])

def post_order(node):
    if node=='.':
        return 
    
    post_order(left[node])
    post_order(right[node])
    print(node,end="")


pre_order('A')
print()
in_order('A')
print()
post_order('A')
