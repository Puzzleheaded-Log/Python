""" Exercise 1: 
Write a function called two_sum() that:
  - receives a list of numbers and a target value
  - finds two numbers whose sum is equal to the target
  - returns the indices of those two numbers. """

nums = [2, 11, 7, 15]
target = 9

def two_sum(numbers, target):
    seen_numbers = {}

    for index, number in enumerate(numbers):
        complement = target - number

        if complement in seen_numbers:
            return [seen_numbers[complement], index]

        seen_numbers[number] = index

print(two_sum(nums, target))



""" Exercise 2: 
Write a function called count_requests() that:
  - receives a list of timestamps (in seconds)
  - groups the requests by minute (timestamp // 60)
  - counts how many requests happen in each minute
  - returns a dictionary with the results.  """

logs = [10, 20, 35, 70, 80, 130]

def count_requests(logs):
    result = {}

    for timestamp in logs:
        minute = timestamp // 60

        if minute not in result:
            result[minute] = 0

        result[minute] += 1

    return result

print(count_requests(logs))



""" Exercise 3: 
Write a function called flatten() that:
  - receives a nested list (a list of lists)
  - converts it into a single flat list
  - returns the flattened list.   """

nums = [[1, 2], [3, 4], [5]]

def flatten(nested_list):
    flat_list = []

    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)

    return flat_list

print(flatten(nums))



""" Exercise 4:
Write a function called is_power_of_three() that:
  - receives an integer n
  - checks whether the number is a power of 3
  - returns True if it is a power of 3, otherwise returns False.   """

number = 27

def is_power_of_three(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        # As long as n is divisible by 3, keep dividing it
        # Example: 27 -> 9 -> 3 -> 1
        n = n // 3

    # If we end up with 1, it means the number is a power of 3
    return n == 1

print(is_power_of_three(number))



""" Exercise 5:
Write a function called roman_to_int() that:
  - receives a Roman numeral string
  - converts it into an integer
  - returns the integer value.   """


s = "MCMXCIV"

def roman_to_int(roman_string):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and values[roman_string[i]] < values[roman_string[i + 1]]:
            total -= values[roman_string[i]]
        else:
            total += values[roman_string[i]]

    return total

print(roman_to_int(s))

