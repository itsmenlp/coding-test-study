N = [int(i) for i in input()]
if sum(N) % 3 == 0 & 0 in N:
    N = [str(n) for n in N]
    print(''.join(sorted(N, reverse=True)))
else:
    print(-1)