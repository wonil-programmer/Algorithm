n = int(input())
dp = [0] * 12

dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

print(dp)

for _ in range(n):
    print(dp[int(input())])