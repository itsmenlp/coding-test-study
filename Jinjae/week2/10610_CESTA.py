num = input()

chk = 0
flag = 0
for n in num:
    chk += int(n)
    if n == '0':
        flag += 1

if chk % 3 != 0 or flag == 0:
    print(-1)
else:
    print(''.join(sorted(num, reverse=True)))