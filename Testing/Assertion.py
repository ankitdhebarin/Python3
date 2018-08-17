def add_positive_numbers(x,y):
	assert x > 0 and y > 0, "Both numbers are positive"
	return x + y

print(add_positive_numbers(1,1)) # 2
add_positive_numbers(1,-1) # This will throw an assertion error