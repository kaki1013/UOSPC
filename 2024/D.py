from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for i in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)


def classify(tree, N):
    # cond 1
    for edges in tree:
        if len(edges) not in (1, 3):
            return False, -1

    # cond 2 - bfs
    for i in range(N):
        if len(tree[i]) == 1:
            start = i
            break

    dist = [-1] * N
    prev = [-1] * N

    dist[start] = 0
    prev[start] = -1

    q = deque([(start, 0)])
    while q:
        curr, d = q.popleft()
        for nxt in tree[curr]:
            if dist[nxt] == -1:
                q.append((nxt, d+1))
                dist[nxt] = d+1
                prev[nxt] = curr

    end = curr

    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])

    dist_root = len(path)//2
    root = path[dist_root]

    # root로부터의 거리 - bfs
    dist = [-1] * N
    dist[root] = 0
    q = deque([(root, 0)])
    while q:
        curr, d = q.popleft()
        for nxt in tree[curr]:
            if dist[nxt] == -1:
                q.append((nxt, d + 1))
                dist[nxt] = d + 1

    for i in range(N):
        if len(tree[i]) == 1:
            if dist[i] != dist_root:
                return False, -1
    return True, root+1


b, root = classify(tree, N)
if b:
    print(1)
print(root)