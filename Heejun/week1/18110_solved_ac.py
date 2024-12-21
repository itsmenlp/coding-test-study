import sys, math

n = int(sys.stdin.readline().strip())
if n == 0:
    print(0)

else:
    difficulty_level = [int(sys.stdin.readline().strip()) for _ in range(n)]
    difficulty_level.sort()

    cut_n = int((n * 0.15) + 0.5)
    difficulty_level = difficulty_level[cut_n:n-cut_n]

    avg = sum(difficulty_level) / len(difficulty_level)
    print(int(avg + 0.5))