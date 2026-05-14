numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]

print("Original List:", numbers)

print("First 4 elements:", numbers[:4])

print("Last 4 elements:", numbers[-4:])

print("Index 2 to 6:", numbers[2:7])

print("Every second elements:", numbers[::2])

print("Every third elements:", numbers[::3])

print("Reversed list:", numbers[::-1])

print("Reverse from index 7 to 3:", numbers[7:3:-1])

print("Except first two:", numbers[2:])

print("Except last two:", numbers[:-2])

copy_list = numbers[:]
print("Copied list:", copy_list)

print("Middle elements:", numbers[3:6])

print("Odd index elements:", numbers[1::2])

print("Even index elements:", numbers[::2])