from tqdm import tqdm

def is_pandigitial(a, b, c):
    s = str(a) + str(b) + str(c)
    if len(s) != 9:
        return False
    for n in range(1, 10):
        if str(n) not in s:
            return False
    return True

solutions = set()

for a in tqdm(range(1, 10_000_000)):
    s = str(a)
    counts = [s.count(str(i)) for i in range(1, 10)]
    if max(counts) > 1: continue
    la = len(s)
    needed_l = 9 - la
    lb = needed_l // 2
    for b in range(int(10**(lb-1)), int(10**lb)):
        product = a * b
        if product in solutions: continue
        if is_pandigitial(a, b, product): 
            solutions.add(product)
            # print(a, ' x ', b, ' = ', product)
        
print(sum(solutions))