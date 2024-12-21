t = int(input())
for i in range(t):
    n, text = input().split()
    print("".join([t*int(n) for t in text]))