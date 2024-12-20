# 문제: https://www.acmicpc.net/problem/1546
# 소요시간: 1분
# 난이도: bronze 1

n = int(input())
raw_scores = list(map(int, input().split()))
max_score = max(raw_scores)
new_scores = [score/max_score*100 for score in raw_scores]
print(sum(new_scores)/n)