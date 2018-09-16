import re

def regex_password(password):

	if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=])[\w\d@#$%^&+=]{6,}',password):
		return "valid password"
	else:
		return "invalid password"

print(regex_password("A$a2aS#7"))
print(regex_password("Aash4a2"))