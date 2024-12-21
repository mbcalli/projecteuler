import sys
sys.path.append('..')

from helper import get_proper_factors
from tqdm import tqdm

def is_abundant(n):
    return sum(get_proper_factors(n)) > n

possibles = set(i for i in range(1, 28_123))
abundant_nums = set(x for x in range(1, 28_123 + 1) if is_abundant(x))

for possible in tqdm(range(1, 28_123)):
    for abundant_num in abundant_nums:
        if abundant_num >= possible: break
        difference = possible - abundant_num
        if possible not in possibles: break
        if is_abundant(difference):
            possibles.remove(possible)
            
print(sum(possibles))