# insert an element into an already sorted list

# AVG WAY - Not great
lst = [2, 6, 8, 10, 15]
num = int(input("Enter a number: "))

for i in range(len(lst)):
    if lst[i] < num < lst[i+1]:
        lst.insert(i+1, num)

print(lst)

# above program won't work if num is smaller than first, or bigger than last
# index goes out of range for ending
# following will work:

# lst = [2, 6, 8, 10, 15]
# num = int(input("Enter a number: "))
#
# for i in range(len(lst)):
#     if num < lst[i]:
#         lst.insert(i, num)
#         break
# else:
#     lst.append(num)
#
# print(lst)
