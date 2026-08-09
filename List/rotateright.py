# to rotate list elements to the right

lst = [2, 4, 6, 8, 10]
new = []
new.append(lst[len(lst)-1])

for i in range(len(lst)-1):
    new.append(lst[i])

print(new)

# time complexity --> O(n)
# space complexity --> O(n)