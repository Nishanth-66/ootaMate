#Lists - collection of multiple values stored in a single variable and is heterogenous
# ordered, mutable, allows duplicates

nums = [10, 20, 30, 40]
print(nums)

data = [10, 34.5, "Nishanth", True]
print(data)

# Accessing data - index starts form 0
print(data[2])

data[2] = "Gamana"
print(data)

#Adding Elements 
numbers = [10, 20, 30, 40]
print(numbers)
numbers.append(60) #adds 60 at end
print(numbers)
numbers.insert(1, 70) # insert method is allowed with index value
print(numbers)

#Remove the elements
numbers.remove(30)
numbers.pop(4)  # pop method is allowed with index value
print(numbers)

print(len(numbers))

for num in numbers:
    print(num)  

numbers.append(100)
for num in numbers:
    print(num, end=" ")

# extend()
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)  

list3 = [4, 6, 3, 1, 9]
list3.sort()
list3.reverse()
print(list3)

