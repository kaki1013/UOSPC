X, Y, D = map(int, input().split())

least = X*D//Y
N = int(input())
objs = [list(map(int, input().split())) for _ in range(N)] # 수량, 가격
