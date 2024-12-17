import math

if __name__ == "__main__":
    participants = int(input())
    sizes = list(map(int, input().split()))
    t, p = map(int, input().split())

    shirt = 0
    for size in sizes:
        shirt += math.ceil(size / t)
    print(shirt)
    print(participants // p, participants % p)
