def RomanToInt(roman):

	roman_int = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
	total = 0
	i = 0

	for i in range(len(roman)):
		
		if i > 0 and roman_int[roman[i]] > roman_int[roman[i-1]]:
				
			total += roman_int[roman[i]] - 2 * roman_int[roman[i-1]]
				
		else:
				
			total += roman_int[roman[i]]		

	return total

print(RomanToInt('MCMXCIV'))

