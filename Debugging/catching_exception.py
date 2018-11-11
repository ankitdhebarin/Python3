def get(d, key):

	try:
		return d[key]

	except KeyError:
		return None

d = {"name": "ankit"}

print(get(d, 'city'))