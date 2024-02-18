import sys
input = sys.stdin.readline

dp = [[0 for _ in range(1001)] for _ in range(1001)]
a = input().strip()
b = input().strip()

len_a, len_b = len(a), len(b)
for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len_a][len_b])