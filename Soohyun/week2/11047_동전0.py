N, K = [int(i) for i in input().split()]
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
cnt = 0
for c in coins:
    if c <= K:
        cnt += K // c
        K %= c
        if K == 0: break
print(cnt)