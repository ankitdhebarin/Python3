from time import time

def speed_test(fn):
	def wrapper(*args, **kwargs):
		start_time = time()
		res = fn(*args,**kwargs)
		end_time = time()
		print(f"Executing {fn.__name__}")
		print(f"Elapsed time: {end_time - start_time}")
		return res
	return wrapper

@speed_test
def sum_num_gens():
	return sum(x for x in range(700000))

@speed_test
def sum_num_lists():
	return sum([x for x in range(700000)])

print(sum_num_gens())
print(sum_num_lists())