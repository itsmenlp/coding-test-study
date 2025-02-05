from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
result = sorted(set(permutations(numbers, M)))

for sequence in result:
    print(" ".join(map(str, sequence)))
