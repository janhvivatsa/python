n = list(input("Enter the words: ").split())

found = False

for i in n:
    if len(i) > 5:
        print(i)
        found = True

if not found:
    print("NIL")
