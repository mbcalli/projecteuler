def is_prime(n):
    import math
    
    if n < 2:
        return False
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def get_factors(n):
    from functools import reduce

    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
def get_proper_factors(n):
    factors = get_factors(n)
    factors.remove(n)
    return factors

def is_perfect_number(n):
    return sum(get_proper_factors(n)) == n