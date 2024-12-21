words = []
for i in range(int(input())):
    word = input()
    words.append((len(word), word))

[print(w[1]) for w in sorted(list(set(words)))]