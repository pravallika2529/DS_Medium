# if aaabbcc is the string, we have to compress it to a3b2c2

string = input("Enter a string: ")

d = {}
letters = string

for letter in letters:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

for key, value in d.items():
    print(key, end="")
    print(value, end="")
