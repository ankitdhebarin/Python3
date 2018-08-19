def reverse_copy(file, new_file):

	with open('Script_copy.txt') as f:
		text = f.read()

	with open('Script.txt', 'w') as newcopy:
		newcopy.write(text[::-1])

reverse_copy('Script_copy.txt', 'Script.txt')