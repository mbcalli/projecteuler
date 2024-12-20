def get_words(x):
    ones = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    
    tens = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }
    
    output = ''
    
    if x >= 1000:
        x -= 1000
        output += 'one thousand'
    
    if x >= 100:
        y = x // 100
        x -= y * 100
        output += ' ' + ones[y] + ' hundred'
    
    if x >= 10:
        if 10 <= x < 20:  # Handle "teens" (10–19)
            output += ' ' + tens[x]
            x = 0
        else:  # Handle multiples of ten
            y = x // 10
            x -= y * 10
            output += ' ' + tens[y * 10]
    
    if x > 0:  # Handle units
        output += ' ' + ones[x]
    
    # Add "and" where applicable
    if 'hundred' in output and not output.endswith('hundred'):
        output = output.replace('hundred', 'hundred and')
    
    # Clean up any extra spaces
    return output.replace(' ','')


total = 0
for i in range(1, 1001):
    # print(get_words(i))
    total += len(get_words(i))
    
print(total)