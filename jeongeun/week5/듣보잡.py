import sys

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
not_heard = set(data[1:N+1])
not_seen = set(data[N+1:N+1+M])

not_heard_and_seen = sorted(not_heard & not_seen)

print(len(not_heard_and_seen))
print("\n".join(not_heard_and_seen))
