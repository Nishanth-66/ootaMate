# Square of number without list comprehenaion

sqr = [1, 2, 3, 4, 5]
new_sqr = []

for n in sqr:
    new_sqr.append(n * n)
    print(new_sqr)

# Square of number with list comprehenaion
lcnew_sqr = [n * n for n in sqr]
print(lcnew_sqr)

 

# odd numbers only without list comprehenaion
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
        print(odd_numbers)

# odd numbers only with list comprehenaion
lcodd_numbers = [num for num in numbers if num % 2 != 0]
print(lcodd_numbers)

# convert string to uppercase without list comprehenaion
names = ["ram", "sam", "john"]
upper_names = []

for name in names:
    upper_names.append[name.upper()]

print(upper_names)

# convert string to uppercase with list comprehenaion
lcupper_names = [name.upper() for name in names]
print(lcupper_names)

# number greater than 10 without list comprehenaion
gnumbers = [5, 12, 8, 20, 3]
result = []

for num in gnumbers:
   if num > 10:
      result.append(num)
print(result)

# number greater than 10 with list comprehenaion
lcgnumber = [num for num in numbers if num > 10]
print(result)

# replace negative number with 0 without list comprehenaion
nenumbers = [2, -3, 5, -1, 7]
result = []

for num in nenumbers:
   if num < 0:
       result.append(0)
   else:
       result.append(num)
print(result)
      

# replace negative number with 0 with list comprehenaion
lcresult = [0 if num < 0 else num for num in numbers]
print(lcresult)

# length of each word without list comprehenaion
words = ["apple", "banana", "kivi"]
length = []

for word in words:
    length.append(len(word))
print(length)

# length of each word with list comprehenaion
lclength = [len(word) for word in words]
print(lclength)