s = input()

digits = [ch for ch in s if ch.isdigit()]

if not digits:
    print("Nil")
else:
    digits.sort(reverse=True)

    # find the smallest even digit to place at the end
    even_digit = None
    for d in sorted(digits):
        if int(d) % 2 == 0:
            even_digit = d
            digits.remove(d)
            break

    if even_digit is None:
        print("Nil")
    else:
        print("".join(digits) + even_digit)
