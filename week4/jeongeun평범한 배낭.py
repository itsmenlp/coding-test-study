N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K+1)

for W, V in items:
    for k in range(K, W-1, -1):
        dp[k] = max(dp[k], dp[k - W] + V)
        
print(dp[K])
