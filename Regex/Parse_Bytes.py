import re

def parse_bytes(input):

	parse_bytes = re.compile(r'[0|1]{8}')
	match = parse_bytes.findall(input)
	return match


print(parse_bytes("10110101 101 323"))
print(parse_bytes("my data is : 10110101 10001010"))
print(parse_bytes("asd"))
