def enforce(*types):
	def decorator(fn):
		def wrapper(*args, **kwargs):
			return fn(*args, **kwargs)
		return wrapper
	return decorator

@enforce(float,float)
def divide(a,b):
	print(a/b)

divide('1','4')
