# Teacher_allocation 
In this program, we first define the number of courses and time slots, and then create lists of courses and time slots with the specified number. We then create an empty dictionary called timetable.
# Define a list of available teachers
teachers = ["Mr. Smith", "Ms. Jones", "Mrs. Brown", "Mr. Lee", "Ms. Kim"]

# Define a list of classes to be taught
classes = ["Math", "Science", "English", "History", "Art"]

# Create an empty dictionary to store teacher assignments
assignments = {}

# Assign teachers to classes
for c in classes:
    # Find a teacher who hasn't been assigned a class yet
    for t in teachers:
        if t not in assignments.values():
            # Assign the teacher to the class
            assignments[c] = t
            # Remove the teacher from the available teachers list
            teachers.remove(t)
            break

# Print out the assignments
print("Teacher Assignments:")
for c, t in assignments.items():
    print(c + ": " + t)
