# 한 방향으로만 움직이는게 이득 // 시작지점은 미정이기 때문
# 최소는 0, 한칸만 켜진 경우 // 최대는 N-1
# 인접한 간격 모두 더하고 최대 인접 거리만 빼주면 됨
# 모두 꺼진 경우는 0 -> 체크
N = int(input())
bulb = list(map(int, input().split()))
dist = []

if 1 in bulb:
    for i in range(N):
        if bulb[i]:
            start = i
            end = i
            break

    for i in range(start, N):
        if bulb[i]:
            dist.append(i - end)
            end = i
    dist.append(N - (end - start))
    dist.sort()

    print(sum(dist) - dist[-1])
else:
    print(0)