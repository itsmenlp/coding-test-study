# 소요시간 : 20분
# 시간복잡도 : O(2^N)? (재귀)
# 난이도 골드 5, 레벨 3
# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def solve(n, a, b):
    if n == 0:
        return 0
    else:
        return (2 * (a%2) + (b%2)) + (4 * solve(n-1, (a//2), (b//2)))
    
print(solve(n, r, c))
