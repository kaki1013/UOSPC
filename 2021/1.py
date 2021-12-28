#import sys
#sys.stdin.readline().strip()
#a, b = map(int, input().split())
N = int(input())
arr = [int(input()) for i in range(N)]
start, end = -1, -1
for i in range(N):
    if start == -1 and arr[i] != -1:
        start = i
        continue
    elif start != -1 and arr[i] != -1:
        end = i
        break
d = int((arr[end] - arr[start]) / (end - start))

a0 = arr[end] - d * end
for i in range(N):
    print(a0 + d * i)