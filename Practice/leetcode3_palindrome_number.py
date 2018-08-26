def palindromenumber(num):

	i = 0
	temp = 0
	s = str(num)

	if len(s) == 1:
		return int(s)

	else:

		while i <= len(s)-1:
			rem = num % 10
			temp = temp * 10 + rem
			num = num // 10
			i += 1

	if temp == int(s):
		return True

	else:
		return False

print(palindromenumber(121))