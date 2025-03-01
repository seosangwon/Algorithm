m = int(input())
edges = []
nodes = set()  # 실제 노드 집합

for _ in range(m):
    s, e = map(int, input().split())
    edges.append([s, e])
    nodes.add(s)
    nodes.add(e)

# 최대 노드 번호 대신 실제 노드 개수에 기반한 인덱스 재구성 (노드 번호가 연속적이지 않을 수 있음)
max_node = max(nodes)

# in_edges, out_edges 초기화: 0부터 max_node까지 생성 (노드가 존재하지 않더라도 공간 확보)
in_edges = [[] for _ in range(max_node + 1)]
out_edges = [[] for _ in range(max_node + 1)]
for s, e in edges:
    in_edges[e].append(s)
    out_edges[s].append(e)

def find_root(nodes, in_edges):
    root_node = -1
    cnt = 0
    # nodes 집합에 있는 노드만 확인
    for i in nodes:
        if len(in_edges[i]) == 0:
            root_node = i 
            cnt += 1
        if cnt >= 2:
            break 
    if cnt != 1:
        return -1 
    return root_node

# 방문 체크를 위해 실제 노드에 대해서만 관리
visited = {node: False for node in nodes}
flag = True

def dfs(node):
    global flag
    visited[node] = True  # 노드 방문 처리 
    for next_node in out_edges[node]:
        if next_node in visited:  # next_node가 실제 노드인지 확인
            if visited[next_node]:  # 이미 방문했다면 사이클
                flag = False 
            else:
                dfs(next_node)

def is_tree():
    root_node = find_root(nodes, in_edges)
    if root_node == -1:  # 루트 노드가 여러 개거나 없음
        return 0
    
    dfs(root_node)
    
    if not flag:  # 사이클 발생
        return 0 

    # 실제 노드 집합의 모든 노드가 방문되었는지 확인
    if not all(visited[node] for node in nodes):
        return 0 
    
    return 1 

print(is_tree())
