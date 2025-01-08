A = int(input())
B = int(input())
C = int(input())

result = A * B * C

result_str = str(result)

counts = [0] * 10

for char in result_str:
    counts[int(char)] += 1
    
for count in counts:
    print(count)
