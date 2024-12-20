strings = [input() for _ in range(3)]

answer_num = None
for i, string in enumerate(strings):
    if string.isdigit():
        answer_num = int(string) + (3-i)
        break
    
if answer_num % 3 == 0 and answer_num % 5 == 0:
    print('FizzBuzz')
elif answer_num % 3 == 0:
    print('Fizz')
elif answer_num % 5 == 0:
    print('Buzz')
else:
    print(answer_num)