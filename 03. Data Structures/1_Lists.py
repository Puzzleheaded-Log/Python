""" Exercise 1: Filter Positive Numbers. """

numbers = [-3, 4, -1, 8, 0, -5]

for n in numbers:
    if n > 0:
        print(n)



""" Exercise 2: Replace Negative Numbers with 0. """

numbers = [-2, 5, -7, 10]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(numbers)



""" Exercise 3: List Slicing Operations. """

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:3])
print(numbers[2:])
print(numbers[::-1])



""" Exercise 4: Even and Odd Separation. """

numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(even)
print(odd)



""" Exercise 5: List Comprehension + Filtering. """

numbers = [2, 6, 8, 3, 10, 1]

filtered = [n for n in numbers if n > 5]

print(filtered)
