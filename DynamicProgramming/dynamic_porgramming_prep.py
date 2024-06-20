# The 1st Approach
"""
def dynamic_fib(n):
	assert n >= 0, "n must be a positive integer"
	if n == 0:
		return 0
	if n == 1:
		return 1
	if memo[n] is not None:
		return memo[n]

	memo[n] = dynamic_fib(n - 1) + dynamic_fib(n - 2)
	return memo[n]


memo = [None] * 1000
for i in range(6):
	print(dynamic_fib(i))  """

# The 2nd Approach - Top-Down - Time-complexity -> O(n) , Space-Complexity -> O(n)
"""
def topdown_fib(n, memo):
	assert n >= 0, "n ,must be a positive integer"
	if n == 0 or n ==1 :
		return n
	if memo[n] is not None:
		return memo[n]

	memo[n] = topdown_fib(n-1,memo) + topdown_fib(n-2,memo)
	return memo[n]

memo = [None] * 1000
results = topdown_fib(3,memo)
print(results)  """


# The 3rd Approach - Bottom-Up - Time-complexity -> O(n) , Space-Complexity -> O(1)

def bottomup_fib(n):
	assert n >= 0, "n must be a positive integers"
	if n == 0 or n == 1:
		return n
	first_num,second_num = 0,1
	for i in range(2, n + 1):
		fib = first_num + second_num
		first_num = second_num
		second_num = fib
	return  fib

print(bottomup_fib(9)) 

