# we have to find the key with the highest value in the dictionary

d = {'a': 5, 'c': 2, 'b': 4, 'd': 8, 'e': 1}
max_value = -9999
key = 0
for k in d:
    if d[k] > maxv:
        max_value = d[k]
        key = k

print(key)

# time complexity --> O(n)
# space complexity --> O(1)