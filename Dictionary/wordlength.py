# store words as keys and their lengths as values in a dictionary

d = {}
n = int(input("Enter the no. of words: "))

for i in range(n):
    word = input("Word: ")
    d[word] = len(word)

print(d)
