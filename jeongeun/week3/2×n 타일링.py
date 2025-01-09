n = int(input())

MOD = 10007

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(3)
    exit()

dp1, dp2 = 1, 3

for _ in range(3, n + 1):
    dp1, dp2 = dp2, (dp2 + 2 * dp1) % MOD

print(dp2)
