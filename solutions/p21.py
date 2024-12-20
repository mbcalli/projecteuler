from helper import get_proper_factors

def d(n):
    return sum(get_proper_factors(n))

def amicable(a):
    b = d(a)
    if a == b: return False
    return d(b) == a

amicables = [i for i in range(2, 10_000) if amicable(i)]

print(amicables)
print(sum(amicables))

# print(d(6368))