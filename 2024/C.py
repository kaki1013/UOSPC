d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

N, K = map(int, input().split())

obj = set()
for _ in range(N):
    x, y = map(int, input().split())
    obj.add((x, y))

xx, yy = (0, 0)
cmd = input()
for c in cmd:
    dir = d[c]
    x_, y_ = xx + dir[0], yy + dir[1]
    if (x_, y_) not in obj:
        xx, yy = x_, y_

print(xx, yy)
