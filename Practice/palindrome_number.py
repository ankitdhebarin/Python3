def palindrome_number(num):

	i = 0 
	temp = ''
	x = str(num)

	for i in range(len(str(num))):

		rem = str(num % 10)
		temp = temp + rem
		num = num / 10

	
	
		return True

	else:
		return False
		
print(palindrome_number(121))

