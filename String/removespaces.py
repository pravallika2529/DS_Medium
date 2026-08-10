# to remove the extra spaces between words

# to remove the extra spaces between words

string = input("Enter a sentence: ")
new = ""

for i in range(len(string)):
    if string[i] != " ":
        new = new + string[i]
    else:
        if i + 1 < len(string) and string[i + 1] != " ":
            new = new + string[i]

print(new)

# time complexity --> O(n)
# space complexity --> O(n)

# EASIER WAY with same TC and SC:

# string = input("Enter a sentence: ")
#
# new = " ".join(string.split())
#
# print(new)
