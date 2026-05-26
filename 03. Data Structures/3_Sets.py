""" Exercise 1: Remove duplicates from a list using a set. """

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = set(numbers)
print(unique)



""" Exercise 2: Find first repeated event. """

events = ["click", "scroll", "click", "hover"]

seen = set()

for e in events:
    if e in seen:
        print("Repeated event:", e)
        break
    seen.add(e)



""" Exercise 3: Remove blocked users from active users. """

active_users = {"ana", "ion", "maria", "alex"}
blocked_users = {"alex", "ion"}

allowed = active_users - blocked_users

print(allowed)

