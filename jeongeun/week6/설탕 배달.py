N = int(input())

for five_kg in range(N // 5, -1, -1):
    remaining = N - (five_kg * 5)
    
    if remaining % 3 == 0:
        three_kg = remaining // 3
        print(five_kg + three_kg)
        break
    
else:
    print(-1)
