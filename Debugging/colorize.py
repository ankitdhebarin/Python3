def colorize(text,color):

	colors = ("red","yellow","magenta","purple","green","blue")

	if type(text) is not str:
		raise TypeError('text must be an instance of string')
	if type(color) is not str:
		raise TypeError('color must be an instance of string')
	if color not in colors:
		raise ValueError('color not in list of colors')
	print("text is {} and color is {}".format(text,color))

colorize("ankit",'purple')