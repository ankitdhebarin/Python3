import re

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	else:
		return None


def extract_allphones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)
	
#print(extract_phone("Call me at 657 203-4838"))
#print(extract_allphones("Call me at 657 203-5736 or Call me at 657 203-5737"))
#print(extract_allphones("Call me at 657 20"))
#print(extract_phone("657 203-5736"))


def is_valid_phone(input):
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
	match = phone_regex.search(input)
	if match:
		return True
	else:
		return False


# def is_valid_phone(input):
# 	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
# 	match = phone_regex.fullmatch(input)
# 	if match:
# 		return True
# 	else:
# 		return False



print(is_valid_phone("563 284-9357"))
print(is_valid_phone("563 284 9357phone"))
print(is_valid_phone("hello 563 284 9357 world "))