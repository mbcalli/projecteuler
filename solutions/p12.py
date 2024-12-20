from helper import get_factors

trianges = [1]
while True:
    next = (len(trianges) + 1) + trianges[-1]
    trianges.append(next)
    
    factors = get_factors(next)
    
    if len(factors) > 500:
        break
    
print(trianges[-1])