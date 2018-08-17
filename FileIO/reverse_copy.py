def reverse_copy(file, new_file):

	with open('Script.txt') as f:
		text = f.read()

	with open('Script_copy.txt', 'w') as newcopy:
		newcopy.write(text[::-1])

reverse_copy('Script.txt', 'Script_copy.txt')