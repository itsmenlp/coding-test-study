import sys

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

result = []

def backtrack(start, sequence):
    if len(sequence) == M:
        result.append(tuple(sequence))
        return
    
    for i in range(start, N):
        backtrack(i, sequence + [numbers[i]])
        
backtrack(0, [])

for seq in sorted(set(result)):
    print(" ".join(map(str, seq)))
