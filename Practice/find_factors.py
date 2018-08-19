def find_factors(num):

	nums = []

	for i in range(1,num+1):
		
		if num % i == 0:
			nums.append(i)

	return nums

find_factors(10)
find_factors(11)
find_factors(111)