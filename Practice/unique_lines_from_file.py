def file_reader():

	txt = file('data.txt').read()
	print(txt)
	print("---")
	txt = txt.lower()
	return '\n'.join(set(txt.splitlines()))

print(file_reader())