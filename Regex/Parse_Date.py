import re

def Parse_Date(input):
	date_regex = re.compile(r'(?P<month>\d{2})[./,](?P<date>\d{2})[./,](?P<year>\d{4})')
	matches = date_regex.search(input)
	date = {}

	
	date['d'] = matches.group("date")
	date['m'] = matches.group("month")
	date['y'] = matches.group("year")

	return date

print(Parse_Date("Today's date is : 08/16/2018"))
