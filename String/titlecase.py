# to convert the first letter of every word of a sentence to uppercase

string = input("Enter a sentence: ")
new = ""
for i in range(len(string)):
    if i == 0 or string[i - 1] == " ":
        if 'a' <= string[i] <= 'z':
            new = new + chr(ord(string[i]) - 32)
        else:
            new = new + string[i]
    else:
        new = new + string[i]

print(new)

# time complexity --> O(n2) --> loops and conditionals
# space complexity --> O(n) --> because inserting chars into a new string
