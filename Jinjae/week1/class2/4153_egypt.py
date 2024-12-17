if __name__ == "__main__":
    while True:
        numbers = sorted(list(map(int, input().split())))
        if numbers == [0, 0, 0]:
            break
        print("right" if numbers[0] ** 2 + numbers[1] ** 2 == numbers[2] ** 2 else "wrong")