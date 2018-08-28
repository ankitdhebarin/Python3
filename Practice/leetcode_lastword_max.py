def length_maxlastword(s):

	if len(s) == 0:
		return s

	else:
		l1 = s.split(' ')

	return len(l1[-1])

print(length_maxlastword("Hello World An kit Dheba r"))
