# to split a given list of numbers into odd and even lists separately

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lst_even = []
lst_odd = []

for num in lst:
    if num % 2 == 0:
        lst_even.append(num)
    else:
        lst_odd.append(num)
print("Even numbers: ", lst_even)
print("Odd numbers: ", lst_odd)
