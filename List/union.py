# find the union of two lists without duplicates

l1 = [2, 4, 6, 2]
l2 = [1, 2, 3, 4, 5]
union = []

for i in l1:
    if i not in union:
        union.append(i)
for i in l2:
    if i not in union:
        union.append(i)

print("Union of two lists: ", union)

# since union is a list, python has to search through the list
# time complexity --> O(n+m)^2
# space complexity --> O(n+m)


# OPTIMIZED WAY
# using set()

# l1 = [2, 4, 6, 2]
# l2 = [1, 2, 3, 4, 5]
#
# union = list(set(l1 + l2))
#
# print("Union of two lists:", union)
