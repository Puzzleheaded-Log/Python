""" Check if a word is a palindrome. """

word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
  
