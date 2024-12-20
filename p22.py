with open('data/0022_names.txt', 'r') as file:
    names = file.read()
    
names = [x.lower() for x in names.replace('"', '').split(',')]
names = sorted(names)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_index = {letter: i+1 for i, letter in enumerate(alphabet)}

score = 0
for i, name in enumerate(names):
    word_score = 0
    for letter in name:
        word_score += alphabet_index[letter]
    score += (i+1) * word_score

print(score)