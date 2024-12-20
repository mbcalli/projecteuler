import sys
sys.path.append('..')

from helper import is_prime
from math import sqrt

def largest_prime_multiple(n):
    
    largest_multiple = None
    
    for i in range(int(sqrt(n)+1), 2, -1):
        if n % i == 0:
            largest_multiple = i
            if is_prime(i):
                return largest_multiple

print(largest_prime_multiple(600851475143))