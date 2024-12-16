if __name__ == "__main__":
    number = list(map(int, input().split()))
    print(sum([num ** 2 for num in number]) % 10)