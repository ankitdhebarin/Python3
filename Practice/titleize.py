def titleize(mystr):
	
	return ' '.join(s[0].upper() + s[1:] for s in mystr.split(' '))

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
