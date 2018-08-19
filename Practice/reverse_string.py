def reversemystring(newstr):

	if len(newstr) == 1:
		return newstr

	else:
		return newstr[-1] + reversemystring(newstr[:-1])


ogstr = "ankit"
rstr = reversemystring(ogstr)
print(rstr)