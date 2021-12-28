# 전구끄기(HARD)
# 켜진 전구 최대한 많이 지나야 함 & 꺼진 전구를 지나는 경우는 그 이상의 켜진 전구를 지나는 경우
# 가장 길게 연속적으로 켜져있는 전구열에서 시작
from collections import deque
import heapq
N = int(input())
bulb = list(map(int, input().split()))

on_off = []
prev = bulb[0]
temp = 0
for i in range(N):
    if bulb[i] == prev:
        temp += 1
    else:
        on_off.append(temp)
        temp = 1
    prev = bulb[i]
on_off.append(temp)

if len(on_off) > 1 and bulb[0] == bulb[-1]:
    temp = on_off.pop()
    on_off[0] += temp

count_state_idx = []
state = bulb[0]
for idx in range(len(on_off)):
    count_state_idx.append((on_off[idx], state, idx))
    state = 1 - state
# count_state_idx : [(3, 1, 0), (1, 0, 1), (1, 1, 2), (2, 0, 3)] (예제 1)
max_on_idx = 0  # 전부 0 인 경우
for cnt, st, idx in sorted(count_state_idx):
    if st == 1:
        max_on_idx = idx

ans = 0
if 1 in bulb:
    # 오른쪽으로 쭉 더함
    on_off1 = deque(on_off)
    for i in range(max_on_idx):
        temp = on_off1.popleft()
        on_off1.append(temp)
    candidate1 = [(-on_off1.popleft(), 0)]
    i = 0
    while len(on_off1) > 1:
        i += 2
        temp = -candidate1[-1][0]
        temp -= on_off1.popleft()
        temp += on_off1.popleft()
        candidate1.append((-temp, i))
    # 왼쪽으로 쭉 더함
    on_off2 = deque(on_off)
    for i in range(max_on_idx):
        temp = on_off2.popleft()
        on_off2.append(temp)
    candidate2 = [(-on_off2.popleft(), 0)]
    i = 0
    while len(on_off2) > 1:
        i += 2
        temp = -candidate2[-1][0]
        temp -= on_off2.pop()
        temp += on_off2.pop()
        candidate2.append((-temp, i))
    print(on_off)
    print(candidate1)
    print(candidate2)
    # 최대힙에 넣고 양쪽에서 겹치지 않으면서, 최대로 할 수 있는 경우 체크
    heapq.heapify(candidate1)
    heapq.heapify(candidate2)
    for i in range(2*N):
        if candidate1:
            max1, idx1 = -candidate1[0], candidate1[0][1]
            max2, idx2 = -candidate2[0][0], candidate2[0][1]
            if idx1+idx2 <= len(on_off):
                ans = max1 + max2 - on_off[0]
            else:
                pass
        else:
            pass

    print(candidate1 + candidate2)
print(ans)