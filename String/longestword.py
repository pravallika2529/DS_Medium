# to find the longest word in a string

string = input("Enter a string: ")
words = string.split()
max_length = 0
longest = words[0]
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest = word

print("The longest word is: ", longest)

# time complexity --> O(n)
# space complexity --> O(n)
# if two words have the same maximum length, the last one will be selected

