n = input().split()

result = []

for i in n:
    if len(i) % 2 != 0:
        result.append(i)

print(",".join(result))
