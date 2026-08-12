# to find the common elements between two arrays

# BRUTE FORCE WAY
l1 = [2, 5, 3, 7, 8, 4]
l2 = [3, 7, 4, 5, 1, 0]
common = []
for i in l1:
    if i in l2:
        common.append(i)
print(common)

# time complexity --> O(nxm) or O(n2) if both have same size
# space complexity --> O(k) --> no. of common elements

# OPTIMIZED APPROACH
# l1 = [2, 5, 3, 7, 8, 4]
# l2 = [3, 7, 4, 5, 1, 0]
#
# s = set(l2)
# common = []
#
# for i in l1:
#     if i in s:
#         common.append(i)
#
# print(common)

# the only difference is, we use a set in the optimized method
# this is because sets use hashing, so we can find element in O(1) time
