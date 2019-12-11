# For Loops are used to repeat an action multiple times.

# Print the numbers 1 - 5
for i in range(1,6):
    print(i)
print('')

# Add the numbers 0 - 9 to a list.
numbers = []
for i in range(10):
    numbers += [i]

print(numbers)
print('')


# Add the numbers 0 - 19 to the list.
for i in range(20):
    numbers += [i]
print(numbers)
print('')

# numbers now contains 0-9 AND 0-19.
# Print how long the list numbers is using the len() function.
print('Length of numbers: ' + str(len(numbers)))
print('')


# Using the length, count how many times we see the number 9.
count = 0
for i in range(len(numbers)):
    if numbers[i] == 9:
        count += 1
print('Count is: ' + str(count))

# Certain data types allow you to directly access the elements (as opposed to using the index as shown above).
# Using the elements directly, count how many times we see the number 8.

count = 0
for num in numbers:
    if num == 8:
        count += 1
print('Count is: ' + str(count))
