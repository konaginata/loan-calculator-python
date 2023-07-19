phrase = input()
new_phrase = ''
for char in phrase:
    if char.isupper():
        new_phrase += '_' + char.lower()
    else:
        new_phrase += char
print(new_phrase)