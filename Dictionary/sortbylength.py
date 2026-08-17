# to sort dictionary keys based on the key length

d = {"ramana": 1, "jhansy": 2, "pravallika": 3, "manasvi": 4}

keys = sorted(d, key=len)

for key in keys:
    print(key, d[key])

# keys = sorted(d, key=len) --> sorts the dictionary's keys acc to their length
# when you give a dictionary directly to sorted(), python sorts its keys
# key=len tells python to sort the keys according to length
