import sys

sys.path.append('..')

from helper import is_prime
from tqdm import tqdm

counts = dict()
primes = set()

for a in tqdm(range(-999, 1000)):
    for b in range(-1000, 1001):
        
        counts[(a, b)] = 0
        
        n = 0
        while True:
            val = (n**2) + (a * n) + b
            if val in primes or is_prime(val):
                counts[(a, b)] = counts[(a, b)] + 1
                n += 1
                primes.add(val)
            else:
                break
            
max_a, max_b = max(counts, key= lambda x: counts[x])
print(max_a, max_b, max_a * max_b)