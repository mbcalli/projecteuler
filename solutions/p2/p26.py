longest = -1
longest_d = None

for d in range(2, 1000):
    seen = set()
    n = 1
    while True:
        r = n % d
        print(r)
        if r in seen:
            # print(seen)
            break
        seen.add(r)
        n = r * 10
    length = len(seen)
    if length > longest:
        longest = length
        longest_d = d
        
print(longest, longest_d)