import sys

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())

arr = list(map(int, data[1].split()))

prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
result = []
for line in data[2:]:
    i, j = map(int, line.split())
    result.append(str(prefix_sum[j] - prefix_sum[i - 1]))
    
sys.stdout.write("\n".join(result) + "\n")
