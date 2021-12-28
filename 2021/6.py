# 동아리 홍보제
from collections import deque

T, M, N = map(int, input().split())
club = dict()
for _ in range(M):
    l = input().split()
    temp = l[2:]
    for i in range(len(temp)):
        temp[i] = ord(temp[i]) - ord('a')
    club[ord(l[0])-ord('A')] = (int(l[1]), temp)
people = dict()
for _ in range(N):
    l = input().split()
    temp = l[2:]
    for i in range(len(temp)):
        temp[i] = ord(temp[i]) - ord('A')
    people[ord(l[0])-ord('a')] = [int(l[1]), deque(temp)]

selected = [False] * N

for _ in range(T):
    apply = [[] for _ in range(M)]
    for i in range(N):
        if not selected[i]:
            aply = people[i][1].popleft()
            apply[aply].append(i)
    for i in range(M):
        if len(apply[i]) <= club[i][0]:
            for a in apply[i]:
                selected[i] = True
        else:
            pass
