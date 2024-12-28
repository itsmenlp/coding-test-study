import math

m, n, k = map(int, input().split())
team_count = min(m // 2, n)
left = m - team_count * 2 + n - team_count

if left > k:
    print(team_count)
else:
    print(team_count - math.ceil((k - left) / 3))