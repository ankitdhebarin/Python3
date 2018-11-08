import re

def password_checker():

	is_set = False

	while not is_set:
		inputstring = input("Enter a password: ")
		print("The input entered is: ", inputstring)

		if len(inputstring) < 8:
			print("Password should be a minimum of 8 characters in length")

		elif re.search(r'[A-Za-z]', inputstring) is None:
			print("Password should have A-Z or a-z")

		elif re.search(r'[0-9]', inputstring) is None:
			print("Password should contain digits 0-9")

		else:
			is_set = True
			print("Password is set. Congratulations!")

password_checker()