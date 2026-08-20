# to find all the keys having the maximum value

d = {'c': 4, 'a': 5, 'b': 8, 'd': 3, 'e': 8}

max_value = list(d.values())[0]

for key, value in d.items():
    if value > max_value:
        max_value = value

print("Maximum value:", max_value)

for key, value in d.items():
    if value == max_value:
        print(key)