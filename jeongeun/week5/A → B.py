A, B = map(int, input().split())

count = 0
while B > A:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break
    count += 1
    
print(count + 1 if B == A else -1)
