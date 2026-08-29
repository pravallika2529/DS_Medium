# find the keys in one dictionary but not the other


d1 = {'a': 2, 'b': 4, 'c': 3}
d2 = {'b': 5, 'e': 6, 'c': 7}

print("To find the keys present in d1 but not in d2:")
print()
keys = []
for k in d1:
    if k not in d2:
        keys.append(k)
print(keys)
