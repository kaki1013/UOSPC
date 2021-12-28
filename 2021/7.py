# 메이데이
N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

sety = dict()
for i in range(N):
    temp = y[i] * (i+1)
    if temp in sety:
        sety[temp] += 1
    else:
        sety[temp] = 1

ans = 0
for i in range(N):
    goal = x[i] * (i+1)
    if goal in sety:
        if sety[goal] > 0:
            sety[goal] -= 1
            ans += 1
print(ans)
