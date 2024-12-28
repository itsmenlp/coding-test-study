N = int(input())
I = [[int(i) for i in input().split()] for _ in range(N)]
I.sort(key=lambda x:(x[1], x[0]))
now = 0
cnt = 0
for i in I:
    if i[0] >= now:
        cnt += 1
        now = i[1]
print(cnt)