found = False
a, b = 3, 4

while not found:
    b += 1
    for a in range(1, b):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a * b * c)
            found = True