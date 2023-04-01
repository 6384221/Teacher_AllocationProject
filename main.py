import random

# Define the number of courses and time slots
NUM_COURSES = 10
NUM_TIME_SLOTS = 5

# Define the list of courses and the list of time slots
courses = ["Course " + str(i) for i in range(1, NUM_COURSES + 1)]
time_slots = ["Monday 9:00-11:00", "Tuesday 9:00-11:00", "Wednesday 9:00-11:00", "Thursday 9:00-11:00", "Friday 9:00-11:00"]

# Define the timetable dictionary
timetable = {}

# Assign each course to a random time slot
for course in courses:
    time_slot = random.choice(time_slots)
    timetable[course] = time_slot
    time_slots.remove(time_slot)

# Print the timetable
print("Department Timetable:\n")
for course, time_slot in timetable.items():
    print(course + ": " + time_slot)
