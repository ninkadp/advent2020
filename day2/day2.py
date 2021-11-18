def get_min(entry: str):
    return int(entry.split('-')[0])

def get_max(entry: str):
    return int(entry.split('-')[1].split(' ')[0])

def get_letter(entry: str):
    letter = entry.split(' ')[1]
    letter = letter[0]
    return letter
    

def get_pwd(entry: str):
    return entry.split(' ')[2]

def validate_pwd(pwd: str, letter: str, min: int, max:int):
    count_letter = 0

    for i in pwd:
        if i == letter:
            count_letter += 1

    if count_letter in range(min, max+1):
        return True
    else:
        return False


strings = []

count = 0

with open(r'input.txt') as f:
    for entry in f.readlines():
        strings.append((entry.strip()))

for string in strings:
    if validate_pwd(get_pwd(string), get_letter(string), get_min(string), get_max(string)):
        count += 1

print(count)
