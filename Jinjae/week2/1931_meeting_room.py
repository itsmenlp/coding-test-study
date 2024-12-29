n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))

answer = 0
end_time = -1

for t in times:
    if t[0] >= end_time and t[1] >= end_time:
        answer += 1
        end_time = t[1]

print(answer)