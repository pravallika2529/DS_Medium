# merge two dictionaries by adding the values of common keys

dct1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dct2 = {'b': 4, 'd': 8, 'f': 6}
dct = {}
for k1, v1 in dct1.items():
    for k2, v2 in dct2.items():
        if k1 == k2:
            dct[k1] = v1 + v2
            break
    else:
        dct[k1] = v1

for k2, v2 in dct2.items():
    if k2 not in dct:
        dct[k2] = v2
print(dct)

# time complexity --> O(n*m)
# space complexity --> O(n + m)

# BETTER WAY:
# dct1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dct2 = {'b': 4, 'd': 8, 'f': 6}
#
# dct = dct1.copy()
#
# for k, v in dct2.items():
#     if k in dct:
#         dct[k] += v
#     else:
#         dct[k] = v
#
# print(dct)

# time complexity --> O(n + m)
# space complexity --> O(n) --> for the result dictionary
