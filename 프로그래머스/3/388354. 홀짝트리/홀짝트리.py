def solution(nodes, edges):
    import sys
    sys.setrecursionlimit(10**7)

    # 1) 노드 인덱싱: node -> idx 매핑
    n = len(nodes)
    node_to_index = {}
    for i, nd in enumerate(nodes):
        node_to_index[nd] = i

    # 2) 차수(deg) 계산 + Union-Find 준비
    parent = list(range(n))
    size = [1] * n
    deg = [0] * n  # 각 인덱스의 차수

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

    # 3) edges 처리하여 차수 증가 및 union-find
    for a, b in edges:
        ai = node_to_index[a]
        bi = node_to_index[b]
        deg[ai] += 1
        deg[bi] += 1
        union(ai, bi)

    # 4) 연결 요소별 match1 계산 (pID[u] == degp[u])
    compMatch1 = {}
    compSize = {}

    for i, nd in enumerate(nodes):
        # 노드 번호 홀짝
        pID = nd % 2
        # 차수 홀짝
        degp = deg[i] % 2
        # match1 여부
        m1 = 1 if pID == degp else 0

        r = find(i)
        if r not in compMatch1:
            compMatch1[r] = 0
            compSize[r] = 0
        compMatch1[r] += m1
        compSize[r] += 1

    # 5) 최종 각 트리(연결 요소)에 대해 홀짝/역홀짝 판별
    odd_even_count = 0      # 홀짝 트리가 될 수 있는 트리 개수
    rev_odd_even_count = 0  # 역홀짝 트리가 될 수 있는 트리 개수

    for r in compMatch1:
        m1 = compMatch1[r]
        csize = compSize[r]
        # 홀짝 트리 조건: m1 == 1
        if m1 == 1:
            odd_even_count += 1
        # 역홀짝 트리 조건: (csize - m1) == 1
        if (csize - m1) == 1:
            rev_odd_even_count += 1

    return [odd_even_count, rev_odd_even_count]