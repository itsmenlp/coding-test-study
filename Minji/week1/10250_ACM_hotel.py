# 문제: https://www.acmicpc.net/problem/10250
# 소요시간: 5분
# 난이도: bronze 3

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    y = str(h) if n%h==0 else str(n%h)
    x = (n-1)//h + 1
    x = str(0)+str(x) if x//10==0 else str(x)
    print(y+x)