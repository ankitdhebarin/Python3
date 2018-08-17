from functools import wraps
def log_function_data(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		""" I am a wrapper Function """
		print(f"you are about to call {fn.__name__}")
		print(f"Here is the documentation {fn.__doc__}")
		return fn(*args, **kwargs)
	return wrapper


@log_function_data
def add(n1,n2):
	""" Adds 2 numbers together """
	return n1 + n2

#print(add(10,20))

print(add.__name__)
print(add.__doc__)