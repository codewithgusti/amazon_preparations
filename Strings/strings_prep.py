
# Concatenation
"""
firstname = 'Augustine '
lastname = 'Shokane'

fullnames = firstname + lastname + '!'
checkname = firstname not in lastname
print(fullnames)
print(checkname)"""

# Indexing
# String called apple -> ['a:0','p:1','p:2','l:3','e:4']
"""
fruit = 'apple'
print(fruit[-1])
print(fruit[2])
print(fruit[0]) """

# Slicing
# String called apple -> ['a:0', 'p:1', 'p:2', 'l:3', 'e:4']
"""
fruit = 'apple'
# [starts:ends(excluding)]
# [:2] -> [0:2]
print(fruit[:2]) # prints 'ap' -> starts at index 0 and  end with index 1, :excluding index 2
print(fruit[2:])"""


# Case Conversion
# capitalize
""" 
fruit = 'apPlE'
capitalize_fruit = fruit.capitalize()
print(capitalize_fruit)
# lowercase
lowercase_fruit = fruit.lower()
print(lowercase_fruit)
# uppercase
uppercase_fruit = fruit.upper()
print(uppercase_fruit)
# swapcase
swapcase_fruit = fruit.swapcase()
print(swapcase_fruit)"""


# Find and Replace

# count occurrence of substrings
status = "Hi , i am preparing for amazon online assessment interview".count("a")
print(status)

# endwith
message = "I am coding for 2 hours everyday"
end_with_substring = message.endswith("everyday")
print(end_with_substring)
# find and indexOf
find_substring = message.find("coding")
indexof_substring = message.index("coding")
print(find_substring)
print(indexof_substring)
# startswith
starts_with_substring = message.startswith("coding")
print(starts_with_substring)
