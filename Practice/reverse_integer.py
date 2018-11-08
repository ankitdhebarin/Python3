def reverse_integer(num):

	temp = ''

	for i in range(len(str(num))):

		rem = num % 10
		temp = temp + str(rem)
		num = num // 10

	return int(temp)

print((reverse_integer(123)))

