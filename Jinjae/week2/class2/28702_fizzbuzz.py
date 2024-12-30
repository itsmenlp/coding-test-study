chk = 3
ans = 0

for _ in range(3):
    num = input()
    if num.isdigit():
        ans = int(num) + chk
    chk -= 1


if ans % 3 == 0:
    if ans % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if ans % 5 == 0:
        print("Buzz")
    else:
        print(ans)