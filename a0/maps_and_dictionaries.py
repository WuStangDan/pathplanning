# Dictionaries (called Maps in other programming langugues) are used to store and look up items with O(1) complexity. Dictionaries have two main components. The first is a called the Key and the second is called the Value. If you enter the Key into a dictionary, it will return it's value.

# Create a blank dictionary. In this dictionary the Key will be a string (a students name) and the Value will be a number (the students test score).
students = {}

# Add a few students test scores.
students['Andre'] = 95
students['Ryan'] = 67
students['Alex'] = 85
students['Ted'] = 75

# Now print Ted's test score.
print('Teds test score is: ' + str(students['Ted']))
print('')

# See if we have a test score for a student named Gage.
if 'Gage' in students:
    print('Gage took the test.')
else:
    print('Gage did not take the test.')
print('')

# Sort all students in alphabetical order and print out their name and test score.
sorted_alphabetical = sorted(students)
for key in sorted_alphabetical:
    print(key + ' scored ' + str(students[key]))
print('')

# Sort all students in reverse alphabetical order and print out their name and test score.
sorted_alphabetical = sorted(students, reverse=True)
for key in sorted_alphabetical:
    print(key + ' scored ' + str(students[key]))
print('')

# Sort all test scores lowest to highest and print them out.
sorted_alphabetical = sorted(students, key=students.get, reverse=False)
for key in sorted_alphabetical:
    print(key + ' scored ' + str(students[key]))
print('')

# Lets try something a little weird. Store a 10x10 matrix in a dictionary and if the row equals the column (for example [2,2]) store the product, otherwise store the number 0.
matrix = {}

# Can we store an array as a Key in a dictionary? Lets find out.
try:
    matrix[[2,2]] = 2*2
    print('It worked!')
except:
    print('It did not work!')

# Instead we can transform the array into a string and store that.
try:
    matrix[str([2,2])] = 2*2
    print('It worked!')
except:
    print('It did not work!')
print('')

# Now clear matrix, and fill in all numbers for a 10x10 matrix.
for r in range(10):
    for c in range(10):
        if r == c:
            matrix[str([r,c])] = r*c
        else:
            matrix[str([r,c])] = 0

# To ensure we did everything correctly print out the 15 largets numbers by Value.
count = 1
for key in sorted(matrix, key=matrix.get, reverse=True):
    print(key + ': ' + str(matrix[key])) 
    if count >= 15:
        break
    count += 1
print('')


# Popping is when you simultanously get the value from a Dictionary, and remove that key from the matrix.
rc = [2,2]
rc_str = str(rc)
if str(rc_str) in matrix:
    print('2,2 is in the matrix')
else:
    print('2,2 is not in the matrix')

value = matrix.pop(rc_str)
print('The value of 2,2 is: ' + str(value))

if str(rc_str) in matrix:
    print('2,2 is in the matrix')
else:
    print('2,2 is not in the matrix')

try:
    value = matrix.pop(rc_str)
    print('Got a value')
except:
    print('Did not get a value')
print('')
