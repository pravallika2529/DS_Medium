# remove the duplicates in a given list, while preserving the insertion order

n = int(input("Enter the no. of nums: "))
nums = []

print("Enter the numbers: ")
for i in range(n):
    num = int(input())
    nums.append(num)

new = []

for num in nums:
    if num not in new:
        new.append(num)

print("List after removing duplicates:", new)
