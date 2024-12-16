T = int(input())
for t in range(T):
    H, W, N = [int(i) for i in input().split()]
    if N % H == 0:
        floor = H
        step = N // H
    else:
        floor = N % H
        step = N // H + 1
    print((floor)*100 + step)