powers = {str(i): i**5 for i in range(0, 10)}

nums = set()
i = 2

# no upper bound specified for this problem
# limit chosen by trial and error
while len(nums) < 6:
    if sum(powers[letter] for letter in str(i)) == i:
        nums.add(i)
    i += 1
    
print(nums)
print(sum(nums))