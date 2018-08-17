import re

def parse_names(input):

	name_regex = re.compile(r'^(Mr\.|Ms\.|Mrs\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group("first"))
	print(matches.group("last"))

parse_names("Mr. Ankit Dhebar")