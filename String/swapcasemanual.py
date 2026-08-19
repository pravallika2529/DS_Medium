# to swap uppercase abd lowercase characters in a string

string = input("Enter a sentence: ")
result = ""
print("After swapping of uppercase and lowercase letters: ")

for ch in string:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch
print(result)

# strings are immutable in python so we cannot directly modify 'string'
