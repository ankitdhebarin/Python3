import re

def is_valid_time(input):
    time_regex = re.compile(r'^\d\d?:\d\d$')
    match = time_regex.search(input)
    if match:
        return True
    else:
        return False

print(is_valid_time("10:45"))
print(is_valid_time("1:23"))
print(is_valid_time("4.45"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("145:45"))