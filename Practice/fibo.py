def NumberPalin(num):

	rev = 0

	while num > 0:
		remainder = num % 10
		rev = rev * 10 + remainder
		num = num // 10

	return rev

num = 121
res = NumberPalin(121)

if res == num:
	print("palindrome")
else:
	print("not a palindrome")