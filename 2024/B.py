N = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]

dp = [[0, 0, 0, 0] for _ in range(N)]

# init
dp[0][0] = arr[0][0]
dp[0][2] = -10**100

dp[0][1] = dp[0][2] + arr[0][0]
dp[0][3] = dp[0][0] + arr[1][0]

# iter
for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][0], dp[i-1][3]) + arr[0][i]
    dp[i][2] = max(dp[i-1][3], dp[i-1][2], dp[i-1][1]) + arr[1][i]

    dp[i][1] = dp[i][2] + arr[0][i]
    dp[i][3] = dp[i][0] + arr[1][i]

# answer
print(max(dp[-1][1], dp[-1][2], dp[-1][3]))
