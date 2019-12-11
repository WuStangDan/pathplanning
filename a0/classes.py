# Classes are used to group functions and variables together.
class Counter():
    # The init or initializer function is where you declare variables.
    def __init__(self, count):
        # Preface all variables with "self."
        self.count = count

    # Member functions can be defined below.
    # Be sure to also include the self in the arguments.
    def increase(self):
        self.count += 1

    def decrease(self):
        self.count -= 1

# Classes must be instantiated before being used.
# Create a class called students and set it to 10.
students = Counter(10)

# Create a class called students and set it to 3.
teachers = Counter(3)

# One student dropped out so decrease the number of students.
students.decrease()

# One teacher was hired so increase the number of teachers.
teachers.increase()

# Print the number of students and teachers.
print('Students: ' + str(students.count))
print('Teachers: ' + str(teachers.count))

