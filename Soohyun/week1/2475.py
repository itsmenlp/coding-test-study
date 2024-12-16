nums = [int(i)**2 for i in input().split()]
sum = 0
for n in nums:
    sum += n

print(sum % 10)