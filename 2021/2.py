# 중도지키미
N, M = map(int, input().split())
seats = [list(input()) for _ in range(N)]

ans = 0

sitable = [[True]*M for _ in range(N)]
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(M):
        if seats[i][j] in ['.', 'W']:
            sitable[i][j] = False

for i in range(N):
    for j in range(M):
        if seats[i][j] == 'P':
            sitable[i][j] = False
            for dx, dy in dxdy:
                sitable[i+dx][j+dy] = False
# 현재: 처음 사람 있던 자리, 그와 인접한 자리, 벽 있는 자리, 빈 자리 False
# 즉 나머지는 내가 맘대로 할 수 있는 자리
# 그래프로 바라보고 각 구성요소를 구성하는 격자(자리)의 개수 카운트하여 최대자리 개수 카운트(홀짝성의 원리?, 흑백 색칠하듯)
# 아니었고요~
ans = 0
for i in range(N):
    for j in range(M):
        if sitable[i][j]:
            ans += 1
print(ans)