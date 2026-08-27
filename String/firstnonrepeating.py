# find the first non-repeating character in a string

word = input("Enter a word: ")
i = 0
for ch in word[i:]:
    if ch not in word[i+1:]:
        print(ch)
        break
    i = i + 1

# more efficient way :
# # find the first non-repeating character in a string
#
# word = input("Enter a word: ")
#
# d = {}
#
# for ch in word:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1
#
# for ch in word:
#     if d[ch] == 1:
#         print("First non-repeating character:", ch)
#         break
