mul = str(int(input()) * int(input()) * int(input()))
print("\n".join([str(mul.count(str(i))) for i in range(0, 10)]))