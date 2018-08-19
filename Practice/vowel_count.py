def vowel_count(newstr):

	vowel = {}
	count = 1
	vow = ['a','e','i','o','u']

	size = len(vow)

	for i in range(size):
		
		for item in newstr.lower():

			if vow[i] == item:

				if vow[i] in vowel:
					vowel[item] += 1

				else:
					vowel[vow[i]] = count
	
	return vowel

print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))