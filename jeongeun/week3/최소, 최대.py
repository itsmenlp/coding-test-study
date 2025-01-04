import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

numbers = list(map(int, data[1:]))

min_value = min(numbers)
max_value = max(numbers)

print(min_value, max_value)
