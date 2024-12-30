import heapq

N = int(input())
arr = list(map(int, input().split()))
S = sum(arr)

heapq.heapify(arr)

while True:
    if -S <= min(arr):
        break

    old_S = S
    S -= heapq.heappop(arr)

    heapq.heappush(arr, -old_S)
    S -= old_S

print(S)