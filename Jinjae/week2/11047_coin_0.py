n, k = map(int, input().split())
n_list = []
for i in range(n):
    n_list.append(int(input()))

ans = 0
for coin in n_list[::-1]:
    if k - coin >= 0:
        ans += k // coin
        k %= coin

print(ans)