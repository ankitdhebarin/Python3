import re

def censor(input):

	censor_regex = re.compile(r'[fF](rack)(ing)?',re.I)
	res = censor_regex.sub("CENSOR", input)
	print(res)

censor("I hope you Fracking die")
censor("Frack you")
censor("You Fracking frack")
