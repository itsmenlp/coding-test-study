S = input()
answer = []
for i in range(ord("a"), ord("z")+1):
    if chr(i) in S: answer.append(str(S.find(chr(i))))
    else: answer.append(str(-1))
print(" ".join(answer))