""" Exercise 1: Nested Tuples (Student Records). """

students = (
    ("Ana", 9),
    ("John", 7),
    ("Maria", 10)
)

for student in students:
    print(student[0], student[1])



""" Exercise 2: Find student with highest grade. """

students = (("Ana", 9), ("Ion", 7), ("Maria", 10))

best = students[0]

for s in students:
    if s[1] > best[1]:
        best = s

print(best)



""" Exercise 3: Print only coordinates that are in the Northern hemisphere (latitude > 0). """

coordinates = ((45.5, 26.1), (-12.3, 44.2), (60.0, -3.5), (-5.2, 10.0))

for lat, lon in coordinates:
    if lat > 0:
        print(lat, lon)

  
