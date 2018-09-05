def reverse_integer(num):

	i = 1
	temp = ''

	for i in range(len(str(num))):

		rem = num % 10
		temp = temp + str(rem)
		num = num // 10

	return int(temp)

print(type(reverse_integer(123)))

