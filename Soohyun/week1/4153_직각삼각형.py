while True:
    lengths = [int(i) for i in input().split()]
    if lengths == [0, 0, 0]: break

    a = max(lengths)
    lengths.remove(a)
    
    if lengths[0]**2 + lengths[1]**2 == a**2:
        print("right")
    else:
        print("wrong")