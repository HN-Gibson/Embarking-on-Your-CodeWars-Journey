# Even or Odd
def even_or_odd(number):
    return "Odd" if number % 2 != 0 else "Even"

# Convert a Number to a String
def number_to_string(num):
    return str(num)

# Vowel Count
def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    return sum(sentence.count(vowel) for vowel in vowels)
