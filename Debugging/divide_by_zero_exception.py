def divide(a,b):

	try:
		result = a/b
	except ZeroDivisionError:
		print("dont divide by a zero!")
	except TypeError as err:
		print("a and b must be ints or floats")
		print(err)
	else:
		print("{} divide by {} equals {}".format(a,b,result))
divide(1,2)
divide(1,'a')
