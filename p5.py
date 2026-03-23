text = input("Enter a sentence: ").lower().split()

freq = {}

for word in text:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word, count in freq.items():
    print(word, ":", count)
