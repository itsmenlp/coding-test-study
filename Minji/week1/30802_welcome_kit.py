# 문제: https://www.acmicpc.net/problem/30802
# 소요시간: 5분
# 난이도: bronze 3

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum([(size-1)//t+1 for size in sizes]))
print(n//p, n%p)