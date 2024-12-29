n, m = map(int, input().split())

if n >= 3 and m >= 6:
    print(m - 2)
elif n == 2:
    print(min(4, (m - 1) // 2 + 1))
elif n == 1:
    print(1)
else:
    print(min(m, 4))