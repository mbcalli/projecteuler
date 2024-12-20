import sys
sys.path.append('..')

from helper import get_proper_factors

def is_abundant(n):
    return sum(get_proper_factors(n)) > n

not_abundant_nums = [x for x in range(1, 28_123 + 1) if not is_abundant(x)]

total = 0
for i, x in enumerate(not_abundant_nums):
    for j, y in enumerate(not_abundant_nums[i:]):
        total += x * y
        
print(total)