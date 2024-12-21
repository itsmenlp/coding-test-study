T = int(input())
for t in range(T):
    result = input()
    before = 0
    total = 0
    for r in result:
        if r == 'O':
            before += 1
            total += before
        else:
            before = 0
    print(total)