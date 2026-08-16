# to find the shortest word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
length = len(words[0])
shortest = words[0]
for word in words:
    if len(word) < length:
        length = len(word)
        shortest = word

print("The shortest word is: ", shortest)

# time complexity --> O(n)
# space complexity --> O(n)

# SIMILAR WAY
# sentence = input("Enter a sentence: ")
# words = sentence.split()
#
# shortest = words[0]
#
# for word in words:
#     if len(word) < len(shortest):
#         shortest = word
#
# print("The shortest word is:", shortest)


