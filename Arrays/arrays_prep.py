# creating a python array

import array as arr
"""numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)
#print(numbers_array) """

# Access the elements in the array
""""
print("First element :", numbers_array[0])
print("Second element :", numbers_array[1])
print("Third element :", numbers_array[2])
print("Last element :", numbers_array[-1])
# Reverse the elements in the array
print("reverse the elements :", numbers_array[::-1]) """

# Slicing elements in the array
""""
# 3rd to 5th
print("3rd to 5th : ", numbers_array[2:5])
# beginning to 4th
print("beginning to 4th : ", numbers_array[:4])
# 6th to end
print("6th to end : ", numbers_array[6:])
# length of the array
print("Length : ", len(numbers_list) )
# beginning to end
print("beginning to end :", numbers_array[:len(numbers_list)]) """

# Changing and Adding Elements

""" numbers = arr.array('i',[1, 2, 3, 5, 7, 10])
# Changing the first element
numbers[0]= 0
print(numbers)
# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])
print(numbers)"""

# Adding Elements
""" # append
numbers = arr.array('i', [1, 2, 3])
numbers.append(4)
#print(numbers)

# extend
numbers.extend([3,4,5])
print(numbers) """

# Removing Python Array Elements
"""
number = arr.array('i', [1, 2, 3, 3, 4])
# deleting at index level
del number[3]
print(number)
# deleting the whole number
del number
print(number) """

"""
numbers = arr.array('i', [10, 11, 12, 12, 13])
numbers.remove(12)
print(numbers)

numbers.pop()
print(numbers) """