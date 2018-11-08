def two_list_dictionary(l1,l2):

	temp = {}

	is_equal = False

	while not is_equal:

		if len(l1) == len(l2):
			is_equal = True

		else:
			if len(l1) > len(l2):
				l2.append('None')
			else:
				break
	
	print(l1)
	print(l2)

	for i in range(len(l1)):

		temp[l1[i]] = l2[i]


	return temp


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]))
print(two_list_dictionary(['x', 'y', 'z']  , [1,2]))