import re

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
print("Protocol :", match.group(1))
print("Domain :", match.group(2))
print("Everything else :", match.group(3))
print("Groups :", match.groups())
print("Group :", match.group())