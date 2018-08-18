from time import sleep

def delay(timer):
	def decorator(fn):
		def wrapper(*args, **kwargs):
			print(f"waiting {timer} secs before printing Hi!")
			sleep(timer)
			return fn(*args, **kwargs)
		return wrapper
	return decorator

@delay(3)
def say_hi():
	print("Hi!")

say_hi()