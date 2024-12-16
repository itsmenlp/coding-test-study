if __name__ == "__main__":
    number = []
    for i in range(3):
        number.append(int(input()))

    print(number[0] + number[1] - number[2])
    print(int(str(number[0]) + str(number[1])) - number[2])
