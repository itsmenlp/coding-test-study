from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
unique_permutations = sorted(set(permutations(numbers, m)))

for perm in unique_permutations:
    print(" ".join(map(str, perm)))
