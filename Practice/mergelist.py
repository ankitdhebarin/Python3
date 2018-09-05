def mergelist(l1,l2):

	'''
	one way to do it:

	print(sorted(l1 + l2))
	'''

	i = 0
	res = []

	while l1 and l2:

		if l1[0] < l2[0]:

			res.append(l1.pop(0))

		else:

			res.append(l2.pop(0))
	
	return res + l1 + l2
	
l1 = [1,2,3]
l2 = [1,2,3]

print(mergelist(l1,l2))