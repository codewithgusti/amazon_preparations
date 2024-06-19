# count Down to zero : Recursively
"""
def countdown(n):
	print(n)
	if n < 1:
		return   # Base Case
	else:
		countdown(n-1) # Recursive Case

countdown(5) """

# Write a recursive function that will sum all numbers from 1 to n.
"""
def sum(n):
	print(n)
	if n ==1:
		return 1 # Base Case
	else:
		return n + sum(n-1)

print(f"The sum of all numbers from 1 to 5 is : ", sum(5)) """

# Write a recursive function that will find the smallest number in a list.
"""
def findmin(Arr, n):
	if n == 1:
		return Arr[0] # Base case
	else:
		return min(Arr[n-1], findmin(Arr,n-1)) # Recursive Case

A = [3, 5, 1, 8, -2, -9, 10, 4]
n = len(A)

print(findmin(A,n))  """

# factorial  recursive
"""
def factorial(n):
	if n<0:
		return -1
	elif n < 2:
		return 1 # Base Case
	else:
		return n * factorial(n-1)

print(factorial(5)) """
"""
def factorial(n):
	return 1  if n <2 else n* factorial(n-1)
print(factorial(0)) """

# fibonacci  recursive
# 0,1,1,2,3,5,8,13,21,34  -> (n-1)+ (n-2)
"""
def fibonacci(n):
	if n <=0:
		return "input positive number"
	elif n ==1:
		return 0
	elif n==2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  """