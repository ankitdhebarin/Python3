def letter_counter(mystr):

	lowstr = mystr.lower()
	calc = {}
	count = 1
	for i in range(len(lowstr)):

		if lowstr[i] in calc:
			calc[lowstr[i]] += 1
		else:

			calc[lowstr[i]] = count

	return calc

print(letter_counter('amazing'))

	




