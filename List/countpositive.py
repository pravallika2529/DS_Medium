# count positive, negative, and zero values

lst = [-1, -2, 5, 2, 8, 0, 4, -10]
neg = 0
pos = 0
zero = 0
for item in lst:
    if item < 0:
        neg = neg+1
    elif item > 0:
        pos = pos+1
    else:
        zero = zero + 1

print("Positive: ", pos)
print("Negative: ", neg)
print("Zero: ", zero)
