N, M, K = [int(i) for i in input().split()]
teams = 0
while N+M > K: 
    N -= 2
    M -= 1
    if N+M<K or N<0 or M<0:
        break
    else:
        teams += 1
print(teams)