from itertools import combinations

N, M = map(int, input().split())
numbers = range(1, N+1)

for combination in combinations(numbers, M):
    print(" ".join(map(str, combination)))
