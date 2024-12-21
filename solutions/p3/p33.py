nums = []
denoms = []

for a in range(10, 100):
    if a % 10 == 0: continue
    a_digits = [int(x) for x in str(a)]
    for b in range(a, 100):
        if b % 10 == 0: continue
        if a == b: continue # quotient = 1
        b_digits = [int(x) for x in str(b)]
        # print(b_digits)
        digits_in_both = set(a_digits) & set(b_digits)
        if not digits_in_both: continue
        for digit in digits_in_both:
            a_temp_digits = [x for x in a_digits]
            b_temp_digits = [x for x in b_digits]
            
            # print(b_temp_digits)
            a_temp_digits.remove(digit)
            b_temp_digits.remove(digit)
            # print(b_temp_digits)
            if b_temp_digits[0] == 0: continue
            if a_temp_digits[0] / b_temp_digits[0] == a / b:
                nums.append(a_temp_digits[0])
                denoms.append(b_temp_digits[0])

product = 1

for n, d in zip(nums, denoms):
    product *= (n/d)
    
print(round(1/product))
        