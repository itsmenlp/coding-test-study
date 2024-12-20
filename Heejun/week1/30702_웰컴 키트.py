import math

N = int(input())
num_sizes = list(map(int, input().split()))
T, P = map(int, input().split())

max_size = max(num_sizes)

answer_T = 0
for num_size in num_sizes:
    answer_T += math.ceil(num_size / T)

answer_P_quitient = N // P
answer_P_remainder = N % P

print(answer_T)
print(answer_P_quitient, answer_P_remainder)
