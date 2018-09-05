def count_letters_word(st):

	unique = {}
	count = 0

	for i in range(len(st)):
		
		if st[i] in unique:

			unique[st[i]] += 1

		else:
			unique[st[i]] = 1

	return unique

print(count_letters_word("amazing"))