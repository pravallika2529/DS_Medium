# to rotate list elements one position to the left

lst1 = [2, 4, 6, 8, 10]
lst2 = []

for i in range(0, len(lst1)):
    if i == len(lst1)-1:
        lst2.append(lst1[0])
    else:
        lst2.append(lst1[i+1])

print(lst2)

# time complexity --> O(n)
# space complexity --> O(n)

# for improving space complexity to O(1), without creating new list,

# lst1 = [2, 4, 6, 8, 10]
#
# first = lst1[0]
#
# for i in range(len(lst1) - 1):
#     lst1[i] = lst1[i + 1]
#
# lst1[-1] = first
#
# print(lst1)
