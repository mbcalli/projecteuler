import sys
sys.path.append('..')

from helper import is_prime

primes_below_2_million = [x for x in range(1, 2_000_000) if is_prime(x)]

print(sum(primes_below_2_million))