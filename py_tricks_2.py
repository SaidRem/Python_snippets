# Readability is important
# "Programs myst be written for people to read, and
# only incidentally for machines" - Hal Abelson.
#
# Avoid unuseful conditions. Like a long if & elif &
# else etc conditions

def is_leap(year):
    """The shortest, the easiest way to detect leap year"""
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


# Never mix tabs and spaces
# A line break between functions
# Two line breaks between classes
# Add a space after ','
# after ':' in dictionaries but not before.

# In Python the best way to use multiple assignment in one line.


a, b = 3, 5
b, a = a, b
a, b, c = ['apple', 'orange', 'cherry']

user = ['Mike', 'Gibson', 12345]
people = [user, ['Bob', 'Fox', 55555]]
for (name, last, tel) in people:
    print(name, tel)

# The generator expressions calculate one value at a time, when necessary.
# Generator saves memory.

total = sum(num**2 for num in range(100))

# Use a list comprehension when the expected result is the list.
# Use a generator expression when the list is only an intermediate result.
