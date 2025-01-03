N = int(input())
P = list(map(int, input().split()))

P.sort()

total_time = 0
current_time = 0

for time in P:
    current_time += time
    total_time += current_time
    
print(total_time)
