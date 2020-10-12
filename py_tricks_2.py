# Readability is important
# "Programs myst be written for people to read, and
# only incidentally for machines" - Hal Abelson.
#
# Avoid unuseful conditions. Like a long if & elif &
# else etc conditions

def is_leap(year):
    """The shortest, the easiest way to detect leap year"""
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
